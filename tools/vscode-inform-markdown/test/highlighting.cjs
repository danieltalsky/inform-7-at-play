/* Exercise the actual VS Code tokenizer, including its installed Markdown grammar. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const [vscodeApp, informExtension, moduleRoot] = process.argv.slice(2);
if (!vscodeApp || !informExtension) {
  throw new Error('Usage: node test/highlighting.cjs VSCODE_RESOURCES_APP INFORM_EXTENSION [MODULE_ROOT]');
}
const dependency = name => moduleRoot
  ? require(path.resolve(moduleRoot, name, 'package')) : require(name);
const textmate = dependency('vscode-textmate');
const oniguruma = dependency('vscode-oniguruma');
const extensionRoot = path.resolve(__dirname, '..');
const json = file => JSON.parse(fs.readFileSync(file, 'utf8'));
const definitions = new Map();
const injections = new Map();

function addExtension(root) {
  const manifest = path.join(root, 'package.json');
  if (!fs.existsSync(manifest)) return;
  for (const contribution of json(manifest).contributes?.grammars || []) {
    definitions.set(contribution.scopeName, path.join(root, contribution.path));
    for (const scope of contribution.injectTo || []) {
      if (!injections.has(scope)) injections.set(scope, []);
      injections.get(scope).push(contribution.scopeName);
    }
  }
}

for (const folder of fs.readdirSync(path.join(vscodeApp, 'extensions'))) {
  addExtension(path.join(vscodeApp, 'extensions', folder));
}
addExtension(informExtension);
addExtension(extensionRoot);

async function registry(inject) {
  const result = new textmate.Registry({
    onigLib: Promise.resolve({
      createOnigScanner: sources => new oniguruma.OnigScanner(sources),
      createOnigString: value => new oniguruma.OnigString(value),
    }),
    loadGrammar: async scope => {
      const file = definitions.get(scope);
      return file ? textmate.parseRawGrammar(fs.readFileSync(file, 'utf8'), file) : null;
    },
    getInjections: scope => (injections.get(scope) || []).filter(
      name => inject || name !== 'markdown.inform7.injection'),
  });
  return result.loadGrammar('text.html.markdown');
}

function tokenize(grammar, text) {
  let state = textmate.INITIAL;
  return text.split(/\r?\n/).map(line => {
    const result = grammar.tokenizeLine(line, state);
    assert.equal(result.stoppedEarly, false);
    state = result.ruleStack;
    return result.tokens;
  });
}

const hasScope = (tokens, scope) => tokens.some(token => token.scopes.includes(scope));

async function main() {
  const onigRoot = moduleRoot
    ? path.resolve(moduleRoot, 'vscode-oniguruma/package')
    : path.dirname(require.resolve('vscode-oniguruma/package.json'));
  const wasm = fs.readFileSync(path.join(onigRoot, 'release/onig.wasm'));
  await oniguruma.loadWASM(wasm.buffer.slice(wasm.byteOffset, wasm.byteOffset + wasm.byteLength));
  const highlighted = await registry(true);
  const baseline = await registry(false);
  let checks = 0;

  for (const fixture of [
    {name: 'backticks', open: '```inform7', close: '```'},
    {name: 'tilde fences', open: '~~~inform7', close: '~~~'},
    {name: 'case and alias', open: '```I7', close: '```'},
    {name: 'longer closing fence', open: '```inform7', close: '`````'},
    {name: 'indented fence', open: '  ```inform7', close: '  ```', prefix: '  '},
    {name: 'blockquote', open: '> ```inform7', close: '> ```', prefix: '> '},
  ]) {
    const prefix = fixture.prefix || '';
    const lines = ['Prose before.', '', fixture.open,
      prefix + 'The description is "A blue room.".', prefix + '[An Inform comment]',
      fixture.close, '', '**Prose after.**'];
    const tokens = tokenize(highlighted, lines.join('\n'));
    assert(hasScope(tokens[3], 'source.inform7'), fixture.name + ': Inform scope ' + JSON.stringify(tokens));
    assert(hasScope(tokens[3], 'string.quoted.double.inform7'), fixture.name + ': string color');
    assert(tokens[4].some(token => token.scopes.some(scope => scope.startsWith('comment.'))),
      fixture.name + ': comment color');
    assert(!hasScope(tokens[7], 'source.inform7'), fixture.name + ': no leak');
    assert.deepEqual(tokens[7], tokenize(baseline, '**Prose after.**')[0]);
    checks++;
  }

  for (const body of ['The description is "An unfinished string.', '[An unfinished comment',
                      '"A story title"']) {
    const tokens = tokenize(highlighted, ['```inform7', body, '```', '', 'Normal prose.'].join('\n'));
    assert(!hasScope(tokens[4], 'source.inform7'), 'Unclosed Inform construct leaked');
    checks++;
  }

  for (const text of [
    '# Heading\n\nOrdinary "prose" and [a link](https://example.com).',
    '```text\n```inform7\nThe description is "Uncolored".\n```',
    '```python\nprint("hello")\n```\n\nProse.',
    '````markdown\n```inform7\nThe description is "An example".\n```\n````',
    '```inform6\nprint "Inform 6";\n```',
    'Inline `inform7` and `The description is "not source".`',
  ]) {
    assert.deepEqual(tokenize(highlighted, text), tokenize(baseline, text),
      'Unrelated Markdown changed: ' + text);
    checks++;
  }

  const nested = tokenize(highlighted,
    '````inform7\n[A comment]\n```\nThe description is "Still Inform".\n````\nProse.');
  assert(hasScope(nested[3], 'string.quoted.double.inform7'), 'Short fence closed longer block');
  assert(!hasScope(nested[5], 'source.inform7'));
  checks++;

  const root = path.resolve(extensionRoot, '../..');
  for (const name of ['README.md', 'places/README.md', 'prototype/generated.md']) {
    const lines = fs.readFileSync(path.join(root, name), 'utf8').split(/\r?\n/);
    const tokens = tokenize(highlighted, lines.join('\n'));
    let inform = false;
    for (let index = 0; index < lines.length; index++) {
      if (/^```inform7\s*$/.test(lines[index])) inform = true;
      else if (/^```\s*$/.test(lines[index])) inform = false;
      else if (inform && lines[index].trim()) {
        assert(hasScope(tokens[index], 'source.inform7'), `${name}:${index + 1}: missing Inform`);
      } else if (!inform) {
        assert(!hasScope(tokens[index], 'source.inform7'), `${name}:${index + 1}: leaked Inform`);
      }
    }
    checks++;
  }
  console.log(`PASS ${checks} highlighting cases, including the actual project Markdown files`);
}

const timeout = setTimeout(() => { console.error('Tokenizer tests timed out'); process.exit(1); }, 30000);
main().then(() => clearTimeout(timeout)).catch(error => {
  clearTimeout(timeout);
  console.error(error);
  process.exitCode = 1;
});

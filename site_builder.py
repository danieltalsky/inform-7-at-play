"""Export the chapter Markdown through a selectable Jinja theme."""
import argparse
from html import escape
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit, unquote

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent
PAGES = [('', 'Home', ''), ('getting-started', 'Started', 'Getting'),
         ('places', 'Places', 'Going'),
         ('things', 'Things', 'Making'), ('actions', 'Actions', 'Doing'),
         ('people', 'People', 'Lifelike'), ('setup', 'When play begins', ''),
         ('naming', 'Naming things', ''),
         ('mistakes', 'Common mistakes', '')]


def highlight(source):
    """Small presentation lexer: strings, nested comments, phrases and kinds."""
    pattern = re.compile(r'"(?:[^"\\]|\\.)*"|\[|\b(?:The description of|The description|There is|There are|It is|is a|is an|is|are|has|can be|Instead of|When play begins|Every turn|After|Before|Check|Carry out|Report|Understand|room|thing|person|container|supporter|edible|scenery|portable|fixed in place|here|north|south|east|west)\b', re.I)
    result, at = [], 0
    while match := pattern.search(source, at):
        result.append(escape(source[at:match.start()]))
        token = match.group()
        end = match.end()
        if token == '[':
            depth = 1
            while end < len(source) and depth:
                depth += (source[end] == '[') - (source[end] == ']')
                end += 1
            token, kind = source[match.start():end], 'comment'
        elif token.startswith('"'):
            kind = 'string'
        elif token.lower() in ('room', 'thing', 'person', 'container', 'supporter', 'edible', 'scenery', 'portable', 'fixed in place', 'here', 'north', 'south', 'east', 'west'):
            kind = 'kind'
        else:
            kind = 'keyword'
        result.append(f'<span class="{kind}">{escape(token)}</span>')
        at = end
    result.append(escape(source[at:]))
    return ''.join(result)


def hide_todos(tokens):
    """Strip editorial paragraphs and unfinished heading sections before rendering.

    Only Markdown headings/paragraphs are markers: literal examples and fenced
    source containing @TODO are left alone. A section ends at the next heading
    of the same or a higher rank.
    """
    removed = set()
    todo_positions = set()
    sections = []
    for i, token in enumerate(tokens):
        if token.type == 'heading_open' and token.level == 0:
            rank = int(token.tag[1:])
            end = next((j for j in range(i + 3, len(tokens))
                        if tokens[j].type == 'heading_open' and tokens[j].level == 0
                        and int(tokens[j].tag[1:]) <= rank), len(tokens))
            sections.append((i, end, rank))
            if '@TODO' in tokens[i + 1].content:
                removed.update(range(i, end))
                todo_positions.add(i)
        elif token.type == 'paragraph_open' and token.level == 0:
            if any('@TODO' in child.content and child.type == 'text'
                   for child in tokens[i + 1].children or []):
                removed.update(range(i, i + 3))
                todo_positions.add(i)
    for start, end, rank in reversed(sections):
        if start in removed or rank == 1:
            continue
        had_todo = any(start <= position < end for position in todo_positions)
        meaningful = any(
            i not in removed and (tokens[i].type in ('inline', 'fence', 'code_block')
                or (tokens[i].type == 'html_block' and
                    re.sub(r'<!--.*?-->', '', tokens[i].content, flags=re.S).strip()))
            for i in range(start + 3, end))
        if had_todo and not meaningful:
            removed.update(range(start, end))
    return [token for i, token in enumerate(tokens) if i not in removed]


def render_chapter(text, slug, md, env):
    # Existing generated HTML transcripts are converted back to semantic content;
    # their inline styles must not override the selected theme.
    tokens = hide_todos(md.parse(text))
    soup = BeautifulSoup(md.renderer.render(tokens, md.options, {}), 'html.parser')
    heading = soup.find('h1')
    title = heading.get_text() if heading else 'Inform 7 at Play'
    if heading:
        heading.decompose()
    for figure in list(soup.select('figure.if-terminal')):
        output = ''.join(str(node) for node in figure.select('pre, kbd'))
        inner = BeautifulSoup(output, 'html.parser')
        for command in inner.select('kbd'):
            command.name = 'p'
            command['class'] = 'command'
            command.insert(0, '> ')
        for node in inner.find_all(True):
            node.attrs.pop('style', None)
        replacement = BeautifulSoup(env.get_template('transcript.html').render(output=str(inner)), 'html.parser')
        figure.replace_with(replacement)
    # Handwritten transcripts remain exactly where their author put them.
    for quote in list(soup.find_all('blockquote')):
        for code in quote.find_all('code'):
            code['class'] = 'command'
        for strong in quote.find_all('strong'):
            previous = strong.find_previous_sibling()
            if strong.get_text().lstrip().startswith('>') or (
                previous and previous.get_text().strip() == '>'
            ):
                strong['class'] = 'command'
        for string in list(quote.find_all(string=True)):
            if '>' in string:
                chunks = str(string).split('>')
                replacement = BeautifulSoup('<span class="prompt">&gt;</span>'.join(escape(c) for c in chunks), 'html.parser')
                string.replace_with(replacement)
        replacement = BeautifulSoup(env.get_template('transcript.html').render(output=quote.decode_contents()), 'html.parser')
        quote.replace_with(replacement)
    used = set()
    for heading in soup.find_all(re.compile('^h[2-6]$')):
        base = re.sub(r'[^a-z0-9]+', '-', heading.get_text().lower()).strip('-') or 'section'
        anchor, n = base, 2
        while anchor in used:
            anchor, n = f'{base}-{n}', n + 1
        heading['id'] = anchor
        used.add(anchor)
    # Explicit index.html URLs work both from disk and on a subdomain/subdirectory.
    for link in soup.find_all('a', href=True):
        url = urlsplit(link['href'])
        if url.scheme or url.netloc or not url.path:
            continue
        path = url.path
        if path.endswith('README.md'):
            path = path[:-len('README.md')] + 'index.html'
        elif path.endswith('/'):
            path += 'index.html'
        link['href'] = path + (f'#{url.fragment}' if url.fragment else '')
    return title, str(soup)


def validate_export(output):
    errors = []
    for page in output.rglob('*.html'):
        soup = BeautifulSoup(page.read_text(encoding='utf-8'), 'html.parser')
        for node in soup.select('a[href], link[href], script[src], img[src]'):
            href = node.get('href', node.get('src', ''))
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            target = (page.parent / unquote(url.path)).resolve() if url.path else page
            if target.is_dir():
                target /= 'index.html'
            if not target.exists():
                errors.append(f'{page.relative_to(output)}: missing {href}')
            elif url.fragment and target.suffix == '.html':
                dest = BeautifulSoup(target.read_text(encoding='utf-8'), 'html.parser')
                if not dest.find(id=unquote(url.fragment)):
                    errors.append(f'{page.relative_to(output)}: missing anchor {href}')
    if errors:
        raise ValueError('\n'.join(errors))


def build(output, theme):
    theme_dir = ROOT / 'themes' / theme
    if not theme_dir.is_dir():
        raise ValueError(f'Unknown theme: {theme}')
    if output.resolve() == ROOT or ROOT.is_relative_to(output.resolve()):
        raise ValueError('Output must not be the project directory or its ancestor')
    env = Environment(loader=FileSystemLoader(theme_dir / 'templates'), autoescape=True,
                      undefined=StrictUndefined)
    md = MarkdownIt('commonmark', {'html': True, 'typographer': False})

    def fence(tokens, idx, options, environment):
        token = tokens[idx]
        if token.info.strip().lower() in ('inform7', 'i7'):
            return env.get_template('code.html').render(source=highlight(token.content))
        return '<pre><code>' + escape(token.content) + '</code></pre>\n'

    md.renderer.rules['fence'] = fence
    output.mkdir(parents=True, exist_ok=True)
    shutil.copytree(theme_dir / 'assets', output / 'assets', dirs_exist_ok=True)
    for index, (slug, label, _) in enumerate(PAGES):
        source = ROOT / slug / 'README.md'
        title, content = render_chapter(source.read_text(encoding='utf-8'), slug, md, env)
        prefix = '../' if slug else ''
        nav = [dict(label=name, verb=verb, title='Getting started' if section == 'getting-started' else name, active=section == slug,
                    href=prefix + (section + '/' if section else '') + 'index.html')
               for section, name, verb in PAGES]
        html = env.get_template('page.html').render(title=title, content=content,
                  nav=nav, home=prefix+'index.html', assets=prefix+'assets/',
                  previous=nav[index-1] if index else None,
                  following=nav[index+1] if index+1 < len(nav) else None,
                  is_home=not slug)
        destination = output / slug / 'index.html'
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(html, encoding='utf-8', newline='\n')
    validate_export(output)
    print(f'Exported {len(PAGES)} pages using {theme}: {output.resolve()}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--theme', default='at-play')
    parser.add_argument('--output', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    build(args.output.resolve(), args.theme)

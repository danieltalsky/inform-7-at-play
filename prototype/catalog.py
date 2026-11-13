"""Validate the complete chapter sample catalog and assemble standalone stories."""

from pathlib import Path
import re
import tomllib

ROOT = Path(__file__).resolve().parent.parent
DOCUMENTS = ["README.md", *[f"{name}/README.md" for name in
             ("places", "things", "actions", "people", "setup", "getting-started", "naming", "mistakes")]]
BLOCK = re.compile(
    r"<!-- inform-example: ([a-z0-9-]+)(.*?)-->\s*\n```inform7[^\n]*\n(.*?)```", re.DOTALL)


def extract_source(document, example_id):
    matches = [source.strip() for name, _, source in BLOCK.findall(document) if name == example_id]
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one source block tagged {example_id!r}; found {len(matches)}")
    return matches[0]


def load_catalog(root=ROOT):
    examples = []
    sources = {}
    for document in DOCUMENTS:
        text = (root / document).read_text(encoding="utf-8")
        matches = list(BLOCK.finditer(text))
        if len(matches) != len(re.findall(r"^```inform7[^\n]*$", text, re.MULTILINE)):
            raise ValueError(f"Every Inform sample needs metadata in {document}")
        for match in matches:
            name, metadata, source = match.groups()
            if name in sources:
                raise ValueError(f"Missing or duplicate sample ID in {document}: {name!r}")
            try:
                example = tomllib.loads(metadata.strip())
            except tomllib.TOMLDecodeError as error:
                raise ValueError(f"Invalid sample metadata for {name}: {error}") from error
            if set(example) - {"title", "kind", "requires", "instead_of", "explanation", "context",
                               "commands", "expect", "notes", "chapter_transcript"}:
                raise ValueError(f"Unknown metadata field for {name}")
            example.update(id=name, document=document)
            examples.append(example)
            sources[name] = (document, source.strip())
    by_id = {example["id"]: example for example in examples}
    for example in examples:
        name = example["id"]
        kind = example.get("kind")
        if kind not in ("standalone", "additive", "alternative"):
            raise ValueError(f"Missing or invalid kind for {name}")
        for field in ("title", "explanation"):
            if not isinstance(example.get(field), str) or not example[field].strip():
                raise ValueError(f"{field} required for {name}")
        for field in ("requires", "instead_of"):
            values = example.get(field, [])
            if not isinstance(values, list) or any(not isinstance(value, str) for value in values):
                raise ValueError(f"{field} must be a list of sample IDs for {name}")
            if len(values) != len(set(values)) or name in values:
                raise ValueError(f"Duplicate or self reference in {field} for {name}")
            for dependency in values:
                if dependency not in sources:
                    raise ValueError(f"Unknown source {dependency!r} for {name}")
        if kind == "standalone" and (example.get("requires") or example.get("context")):
            raise ValueError(f"Standalone sample {name} cannot require other source")
        if kind == "additive" and not (example.get("requires") or example.get("context")):
            raise ValueError(f"Additive sample {name} needs a base or context")
        if (kind == "alternative") != bool(example.get("instead_of")):
            raise ValueError(f"Only alternatives must name instead_of targets: {name}")
        if not isinstance(example.get("commands"), list) or not example.get("expect"):
            raise ValueError(f"Commands and expected output required for {name}")
        for field in ("commands", "expect"):
            if not isinstance(example[field], list) or any(not isinstance(value, str) or not value for value in example[field]):
                raise ValueError(f"{field} must be a list of nonempty strings for {name}")

    def resolve(name, visiting):
        if name in visiting:
            raise ValueError(f"Cyclic sample dependencies: {' -> '.join([*visiting, name])}")
        example = by_id[name]
        ordered, contexts = [], []
        for dependency in example.get("requires", []):
            names, inherited = resolve(dependency, [*visiting, name])
            ordered.extend(item for item in names if item not in ordered)
            contexts.extend(item for item in inherited if item not in contexts)
        for target in example.get("instead_of", []):
            if target in ordered:
                raise ValueError(f"Alternative {name} also includes replaced sample {target}")
        ordered.append(name)
        if example.get("context") and example["context"] not in contexts:
            contexts.append(example["context"])
        return ordered, contexts

    # Resolve all recipes before mutating any metadata so inherited context is stable.
    resolved = {name: resolve(name, []) for name in by_id}
    for example in examples:
        names, contexts = resolved[example["id"]]
        for name in names:
            if set(by_id[name].get("instead_of", [])) & set(names):
                raise ValueError(f"Composition {example['id']} contains an alternative and its replaced source")
        example["sources"] = names
        if contexts:
            example["context"] = "\n\n".join(contexts)
    return examples, sources


def assemble_source(example, sources):
    parts = [sources[name][1] for name in example.get("sources", [example["id"]])]
    # Title-bearing snippets retain their own title and author. Context is only
    # used for fragments whose chapter does not provide a complete starting room.
    context = example.get("context")
    if parts[0].startswith('"'):
        if context:
            parts.insert(1, context)
    else:
        if context:
            parts[0] = context + "\n" + parts[0]
        parts.insert(0, f'"{example["title"]}"')
    return "\n\n".join(parts) + "\n"

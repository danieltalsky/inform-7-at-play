"""Create a standalone visual preview from the latest captured gameplay."""

from html import escape
import json

from run import PROTOTYPE, parse_console_output
from terminal import render_terminal


def main():
    examples = json.loads((PROTOTYPE / "examples.json").read_text(encoding="utf-8"))
    sections = []
    for example in examples:
        raw = (PROTOTYPE / "build" / example["id"] / "console-output.txt").read_bytes().decode("utf-8")
        game = parse_console_output(raw, example["commands"])
        sections.append(f'<h2>{escape(example["title"])}</h2>'
                        + render_terminal(game.without_banner()))
    html = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            '<title>Inform 7 at Play — Transcript preview</title>'
            '<style>body{margin:0;background:#f5f0e5;color:#342f28;font:18px/1.6 Georgia,serif;}'
            'main{max-width:780px;margin:0 auto;padding:36px 18px 60px;}'
            'h1{font-size:clamp(28px,5vw,42px);line-height:1.2;margin:10px 0 16px;}'
            'h2{font-size:23px;margin:40px 0 12px;}p{max-width:64ch;}'
            '</style></head><body><main><h1>Inform 7 at Play</h1>'
            '<p>Terminal transcript preview. Green prompts are commands; '
            'the text below each is the story’s actual response.</p>'
            + "".join(sections) + '</main></body></html>')
    target = PROTOTYPE / "build/terminal-preview.html"
    target.write_text(html, encoding="utf-8", newline="\n")
    print(target)


if __name__ == "__main__":
    main()

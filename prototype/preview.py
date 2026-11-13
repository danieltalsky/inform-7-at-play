"""Create a searchable source-and-terminal gallery from the last complete run."""

import json

from run import PROTOTYPE
from terminal import ENVIRONMENT, Transcript, Turn, render_terminal


def main():
    captures = json.loads((PROTOTYPE / "build/examples.json").read_text(encoding="utf-8"))
    for capture in captures:
        data = capture["transcript"]
        game = Transcript(data["initial"], tuple(Turn(**turn) for turn in data["turns"]))
        capture["terminal"] = render_terminal(game.without_banner())
    html = ENVIRONMENT.get_template("preview.html").render(
        examples=captures, documents=list(dict.fromkeys(item["document"] for item in captures)))
    target = PROTOTYPE / "build/terminal-preview.html"
    target.write_text(html, encoding="utf-8", newline="\n")
    print(target)


if __name__ == "__main__":
    main()

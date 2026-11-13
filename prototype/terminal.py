"""Structured gameplay and the HTML presentation shared by generated examples."""

from dataclasses import dataclass, replace
from html import escape
from pathlib import Path
import re

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from markupsafe import Markup


@dataclass(frozen=True)
class Turn:
    command: str
    response: str


@dataclass(frozen=True)
class Transcript:
    initial: str
    turns: tuple[Turn, ...]

    @property
    def text(self):
        text = self.initial.strip()
        for turn in self.turns:
            text += f"\n\n>{turn.command}\n{turn.response.strip()}"
        return text.rstrip() + "\n"

    def without_banner(self):
        # An introduction may precede the banner, and both the headline and
        # author are customizable. Anchor removal to the pinned release line.
        banner = (r"(?:\A|(?<=\n\n))[^\n]+\n[^\n]+\n"
                  r"Release [^\n]+ / Inform 7 v[^\n]+(?:\n\n|\Z)")
        initial, count = re.subn(banner, "", self.initial, count=1)
        if count != 1:
            raise ValueError("Unrecognized story banner; refusing to trim it")
        return replace(self, initial=initial)


def literal_text(value):
    # HTML-escape first, then encode braces so Jekyll's Liquid pass leaves story
    # text such as {{ a name }} or {% a command %} alone when building Markdown.
    return Markup(escape(str(value)).replace("{", "&#123;").replace("}", "&#125;"))


ENVIRONMENT = Environment(
    loader=FileSystemLoader(Path(__file__).resolve().parent / "templates"),
    autoescape=True,
    undefined=StrictUndefined,
    trim_blocks=True,
    lstrip_blocks=True,
    keep_trailing_newline=True,
)
ENVIRONMENT.filters["literal_text"] = literal_text


def render_terminal(transcript):
    return ENVIRONMENT.get_template("terminal.html").render(transcript=transcript).rstrip() + "\n"

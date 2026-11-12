"""Contract tests for example selection and console transcript framing."""

import contextlib
import io
from html.parser import HTMLParser
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from run import (MARKER, extract_source, format_transcript, update_chapter_transcript,
                 verify_compilers, write_or_check)
from setup_linux import debian_payload
from terminal import Transcript, Turn, render_terminal


class SourceTests(unittest.TestCase):
    def test_inserting_unrelated_blocks_does_not_change_selection(self):
        document = ('```inform7\nAn unrelated room is a room.\n```\n\n'
                    '<!-- inform-example: chosen -->\n'
                    '```inform7\nThe desired room is a room.\n```\n')
        self.assertEqual(extract_source(document, "chosen"), "The desired room is a room.")

    def test_missing_or_duplicate_ids_fail(self):
        block = '<!-- inform-example: chosen -->\n```inform7\nA room is a room.\n```\n'
        for document in ("", block + block):
            with self.subTest(document=document), self.assertRaises(ValueError):
                extract_source(document, "chosen")


class TranscriptTests(unittest.TestCase):
    def test_story_prompt_characters_and_unicode_are_preserved(self):
        raw = (f'\nA café with a > sign\n\n{MARKER}\n\n>Response > text.\n'
               f'\n{MARKER}\n\n>\n<end of input>\n')
        self.assertEqual(format_transcript(raw, ["look"]),
                         'A café with a > sign\n\n>look\nResponse > text.\n')

    def test_early_game_exit_fails_even_when_response_is_present(self):
        raw = f'Story\n{MARKER}\n>Expected response.\n'
        with self.assertRaisesRegex(RuntimeError, "boundaries"):
            format_transcript(raw, ["look"])

    def test_extra_interaction_is_not_silently_discarded(self):
        raw = (f'Story\n{MARKER}\n>Response.\n{MARKER}\n'
               '>Enter a filename:\n<end of input>\n')
        with self.assertRaisesRegex(RuntimeError, "EOF trailer"):
            format_transcript(raw, ["look"])

    def test_runtime_problem_fails(self):
        raw = (f'Story\n{MARKER}\n>*** Run-time problem P1\n'
               f'{MARKER}\n>\n<end of input>\n')
        with self.assertRaisesRegex(RuntimeError, "runtime error"):
            format_transcript(raw, ["look"])


class CompilerTests(unittest.TestCase):
    def test_compiler_version_change_requires_explicit_recipe_update(self):
        with patch("run.compiler_version", return_value="99.0"):
            with self.assertRaisesRegex(RuntimeError, "compiler upgrades require"):
                verify_compilers("inform7", "inform6")


class ChapterTests(unittest.TestCase):
    start = "<!-- inform-transcript: room -->"
    end = "<!-- /inform-transcript: room -->"
    transcript = Transcript(
        "A room\nAn Interactive Fiction\n"
        "Release 1 / Serial number 160428 / Inform 7 v10.1.2 / D\n\n"
        "Featureless Room\nA room description.",
        (Turn("look", "A room description."),))

    def test_updates_only_selected_region_and_is_idempotent(self):
        document = "Intro\n" + self.start + "\nOld play\n" + self.end + "\nExplanation\n"
        updated = update_chapter_transcript(document, "room", self.transcript)
        self.assertTrue(updated.startswith("Intro\n" + self.start))
        self.assertTrue(updated.endswith(self.end + "\nExplanation\n"))
        self.assertIn('<figure class="if-terminal"', updated)
        self.assertIn("Featureless Room\n", updated)
        self.assertNotIn("Release 1", updated)
        self.assertNotIn("Old play", updated)
        self.assertEqual(update_chapter_transcript(updated, "room", self.transcript), updated)

    def test_missing_duplicate_or_reversed_markers_fail(self):
        for document in (self.start, self.start + self.start + self.end,
                         self.end + self.start):
            with self.subTest(document=document), self.assertRaises(ValueError):
                update_chapter_transcript(document, "room", self.transcript)

    def test_unrecognized_banner_is_not_silently_removed(self):
        with self.assertRaisesRegex(ValueError, "banner"):
            update_chapter_transcript(self.start + self.end, "room", Transcript("Actual gameplay", ()))

    def test_check_reports_drift_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            chapter = root / "chapter.md"
            chapter.write_text("Old play\n", encoding="utf-8")
            with patch("run.ROOT", root), contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertFalse(write_or_check(chapter, "New play\n", True))
            self.assertIn("checked-in/chapter.md", output.getvalue())
            self.assertEqual(chapter.read_text(encoding="utf-8"), "Old play\n")


class TerminalContent(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.outputs = []
        self.commands = []
        self.tags = []
        self.active = None

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        if tag in ("samp", "kbd"):
            self.active = []

    def handle_data(self, data):
        if self.active is not None:
            self.active.append(data)

    def handle_endtag(self, tag):
        if tag in ("samp", "kbd"):
            (self.outputs if tag == "samp" else self.commands).append("".join(self.active))
            self.active = None


class TerminalTests(unittest.TestCase):
    def test_html_preserves_output_and_command_text(self):
        game = Transcript("A café\n  With indentation.", (
            Turn("look", "A description.\n\nAnother paragraph."),
            Turn("say hello", ">This is story output, not a command.")))
        parser = TerminalContent()
        parser.feed(render_terminal(game))
        self.assertEqual(parser.commands, ["look", "say hello"])
        self.assertEqual(parser.outputs, [game.initial, *(turn.response for turn in game.turns)])

    def test_html_and_liquid_syntax_remain_literal_text(self):
        text = '<script>alert("hello")</script> & {{ name }} {% include secret %}'
        game = Transcript(text, (Turn('<look & "listen">', text),))
        rendered = render_terminal(game)
        parser = TerminalContent()
        parser.feed(rendered)
        self.assertNotIn("script", parser.tags)
        self.assertNotIn("{{", rendered)
        self.assertNotIn("{%", rendered)
        self.assertEqual(parser.outputs, [text, text])
        self.assertEqual(parser.commands, ['<look & "listen">'])

    def test_banner_trimming_does_not_modify_plain_text(self):
        game = ChapterTests.transcript
        trimmed = game.without_banner()
        self.assertIn("Release 1", game.text)
        self.assertNotIn("Release 1", trimmed.text)
        self.assertEqual(trimmed.turns, game.turns)
        self.assertTrue(trimmed.initial.startswith("Featureless Room"))


class LinuxPackageTests(unittest.TestCase):
    @staticmethod
    def member(name, content):
        header = (f"{name + '/':<16}{0:<12}{0:<6}{0:<6}{'100644':<8}"
                  f"{len(content):<10}`\n").encode("ascii")
        return header + content + (b"\n" if len(content) % 2 else b"")

    def test_debian_member_alignment(self):
        package = (b"!<arch>\n" + self.member("debian-binary", b"2.0\n")
                   + self.member("control.tar.xz", b"x")
                   + self.member("data.tar.xz", b"payload"))
        self.assertEqual(debian_payload(package), b"payload")

    def test_truncated_member_is_rejected(self):
        package = b"!<arch>\n" + self.member("data.tar.xz", b"payload")
        with self.assertRaisesRegex(ValueError, "Truncated"):
            debian_payload(package[:-3])

    def test_non_package_is_rejected(self):
        with self.assertRaises(ValueError):
            debian_payload(b"not a Debian package")


if __name__ == "__main__":
    unittest.main()

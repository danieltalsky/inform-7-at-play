"""Contract tests for example selection and console transcript framing."""

import unittest
from unittest.mock import patch

from run import MARKER, extract_source, format_transcript, verify_compilers
from setup_linux import debian_payload


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

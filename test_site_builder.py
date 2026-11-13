"""Check the export's content order, safe highlighting, and link portability."""
from pathlib import Path
import tempfile
import unittest

from bs4 import BeautifulSoup

from markdown_it import MarkdownIt
from site_builder import build, highlight, hide_todos, PAGES, ROOT


class StaticSiteTests(unittest.TestCase):
    def render_notes(self, text):
        md = MarkdownIt('commonmark', {'html': True})
        return md.renderer.render(hide_todos(md.parse(text)), md.options, {})

    def test_heading_todo_hides_descendants_to_next_peer(self):
        html = self.render_notes('# Page\n\n## @TODO Draft\n\nHidden prose\n\n### Child\n\nHidden child\n\n## Ready\n\nVisible prose')
        self.assertNotIn('Draft', html)
        self.assertNotIn('Hidden', html)
        self.assertIn('Ready', html)
        self.assertIn('Visible prose', html)

    def test_todo_only_sections_and_empty_parents_disappear(self):
        html = self.render_notes('# Page\n\n## Empty parent\n\n### Empty child\n\n@TODO Write this.\n\n---\n\n## Retained\n\nReal explanation.\n\n@TODO Add more.\n\n### Child\n\nActual content.')
        self.assertNotIn('Empty', html)
        self.assertNotIn('@TODO', html)
        self.assertIn('Retained', html)
        self.assertIn('Actual content.', html)

    def test_literal_todo_in_code_is_preserved(self):
        html = self.render_notes('# Page\n\n## Example\n\n```inform7\n[Literal @TODO in a story]\n```\n\n`@TODO`\n')
        self.assertIn('Literal @TODO in a story', html)
        self.assertIn('<code>@TODO</code>', html)

    def test_highlighting_preserves_literal_source(self):
        source = 'The Box is a container. [outer [nested] comment]\n"<script>& [the box]"'
        rendered = BeautifulSoup(highlight(source), 'html.parser')
        self.assertEqual(rendered.get_text(), source)
        self.assertIsNone(rendered.find('script'))
        self.assertEqual(rendered.select_one('.comment').get_text(), '[outer [nested] comment]')

    def test_complete_portable_export_and_sequence(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as temporary:
            output = Path(temporary)
            build(output, 'at-play')  # Also validates every local link and anchor.
            self.assertEqual(len(list(output.rglob('*.html'))), len(PAGES))
            home = BeautifulSoup((output / 'index.html').read_text(encoding='utf-8'), 'html.parser')
            self.assertEqual(home.h1.get_text(), 'Make your story a world.')
            self.assertEqual(home.select_one('.wordmark').get_text(), 'Inform 7 at Play')
            chapters = home.select('.sidebar .chapter')
            self.assertEqual(chapters[0].get_text(' ', strip=True), 'Getting Started')
            self.assertEqual(chapters[0]['href'], 'getting-started/index.html')
            self.assertEqual(chapters[1].get_text(' ', strip=True), 'Going Places')
            examples = home.select('article .example')
            self.assertIn('code-example', examples[0]['class'])
            self.assertIn('play-example', examples[1]['class'])
            self.assertTrue(home.select('.console .command'))
            self.assertEqual(home.select_one('.play-example figcaption').get_text(), 'how it plays')
            for page in output.rglob('*.html'):
                soup = BeautifulSoup(page.read_text(encoding='utf-8'), 'html.parser')
                self.assertEqual(len(soup.select('[aria-current="page"]')), 1)
                self.assertFalse(soup.select('details .language-inform7'))
                self.assertFalse(soup.select('figure[style]'))
            md = MarkdownIt('commonmark', {'html': True})
            expected_sources = sum(
                sum(t.type == 'fence' and t.info.strip() == 'inform7'
                    for t in hide_todos(md.parse((ROOT / slug / 'README.md').read_text(encoding='utf-8'))))
                for slug, _, _ in PAGES)
            exported_sources = sum(len(BeautifulSoup(p.read_text(encoding='utf-8'), 'html.parser').select('.language-inform7')) for p in output.rglob('*.html'))
            self.assertEqual(exported_sources, expected_sources)
            self.assertFalse(any('@TODO' in BeautifulSoup(p.read_text(encoding='utf-8'), 'html.parser').get_text() for p in output.rglob('*.html')))


if __name__ == '__main__':
    unittest.main()

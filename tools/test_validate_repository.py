"""Regression checks for reader-facing Markdown anchor validation."""
import contextlib
import hashlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.parse import unquote, urlsplit

import validate_repository as validator
from validate_repository import local_target, markdown_anchors, markdown_targets


class MarkdownAnchorTests(unittest.TestCase):
    def test_explicit_html_ids_and_names(self):
        text = '<a id="endpoint"></a>\n<a name=legacy></a>\n<div id=\'σ\'></div>'
        self.assertEqual(markdown_anchors(text), {'endpoint', 'legacy', 'σ'})

    def test_formatted_and_unicode_headings(self):
        text = '# **Scalar** `K_ij` and [vector](matrix.json)\n## Σ₂ and café\n'
        self.assertEqual(markdown_anchors(text), {'scalar-k_ij-and-vector', 'σ₂-and-café'})

    def test_duplicate_heading_suffix_collisions(self):
        text = '# Modes\n# Modes\n# Modes-1\n# Modes\n'
        self.assertEqual(markdown_anchors(text), {'modes', 'modes-1', 'modes-1-1', 'modes-2'})

    def test_atx_closing_markers_and_setext(self):
        text = '## Main result ##\n\nBackground\n==========\n\nDetails\n-------\n'
        self.assertEqual(markdown_anchors(text), {'main-result', 'background', 'details'})

    def test_fences_comments_and_inline_examples_are_not_anchors(self):
        text = ('```md\n# Not rendered\n<a id="fake"></a>\n```\n'
                '<!-- <a id="hidden"></a>\n# Hidden heading -->\n'
                '`<a id="example"></a>`\n<div data-id="also-fake"></div>\n# Visible\n')
        self.assertEqual(markdown_anchors(text), {'visible'})

    def test_front_matter_is_not_a_heading(self):
        self.assertEqual(markdown_anchors('---\ntitle: data\n---\n# Result\n'), {'result'})

    def test_encoded_fragment_and_same_document_resolution(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'reader.md'
            path.write_text('# Σ₂\n\n<a id="literal-id"></a>\n')
            for link in ('#%CF%83%E2%82%82', 'reader.md#literal-id'):
                target = local_target(path, link)
                self.assertEqual(target, path.resolve())
                self.assertIn(unquote(urlsplit(link).fragment), markdown_anchors(target.read_text()))
            self.assertNotIn('absent', markdown_anchors(path.read_text()))
            self.assertIsNone(local_target(path, 'https://example.org/#external'))

    def test_links_in_code_and_math_are_not_link_targets(self):
        text = ('[actual](result.md#endpoint)\n'
                '```\n[fake](result.md#fake)\n```\n'
                '`[fake](result.md#inline)`\n$$[fake](x)$$\n')
        self.assertEqual(list(markdown_targets(text)), [('result.md#endpoint', False)])

    def test_validator_rejects_missing_anchor_in_existing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            document = root / 'reader.md'
            document.write_text('# Present\n\n[Broken](reader.md#absent)\n')
            manifest = root / 'manifest.json'
            manifest.write_text(json.dumps({'sha256': {
                'reader.md': hashlib.sha256(document.read_bytes()).hexdigest(),
            }}))
            output = io.StringIO()
            with patch.object(validator, 'ROOT', root), patch.object(validator, 'MANIFEST', manifest):
                with patch('sys.argv', ['validate_repository.py', '--details']):
                    with contextlib.redirect_stdout(output), self.assertRaises(SystemExit) as exit_status:
                        validator.main()
            self.assertEqual(exit_status.exception.code, 1)
            result = json.loads(output.getvalue())
            self.assertEqual(result['errors'], [{
                'file': 'reader.md', 'kind': 'missing_fragment', 'target': 'reader.md#absent',
            }])
            self.assertTrue(result['fragment_anchors_checked'])


if __name__ == '__main__':
    unittest.main()

import tempfile
import unittest
from pathlib import Path

from check_profile import validate_links


class ProfileLinks(unittest.TestCase):
    def test_external_and_existing_relative_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "guide.md").write_text("# Guide\n")
            self.assertEqual(validate_links('[Source](https://example.com/repo) [Guide](guide.md)', root), 2)

    def test_invalid_targets_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for target in ('http://example.com', 'https://user:password@example.com',
                           '../outside.md', 'missing.md', 'javascript:alert'):
                with self.subTest(target=target), self.assertRaises(ValueError):
                    validate_links(f'[Link]({target})', root)

    def test_empty_profile_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_links('# Empty\n', Path('.'))

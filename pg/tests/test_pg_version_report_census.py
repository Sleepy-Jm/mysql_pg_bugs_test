import sys
from pathlib import Path
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import pg_version_report_census as census


class VersionFieldTests(unittest.TestCase):
    def parse(self, field, description='PostgreSQL version: 14.1'):
        source = ('<meta property="article:author" content="PG Bug reporting form">'
                  '<div class="message-content"><p>Bug reference: 123<br>'
                  f'PostgreSQL version: {field}<br>Operating system: Linux<br>'
                  f'Description:</p><p>{description}</p></div>')
        with patch.object(census, 'fetch', return_value=(source, 'fixture')), \
             patch.object(Path, 'read_bytes', return_value=source.encode()):
            return census.report_scan(('https://www.postgresql.org/message-id/fixture', {'report_id': '123'}))

    def test_exact_versions(self):
        self.assertEqual(self.parse('14.1, 14.2, 17.1, 17.2')['target_versions'], list(census.VERSIONS))

    def test_no_prefix_or_body_matches(self):
        self.assertEqual(self.parse('14.10, 14.20, 17.10, 17.20')['target_versions'], [])

    def test_no_shorthand_expansion(self):
        self.assertEqual(self.parse('14.1/2')['target_versions'], ['14.1'])

    def test_missing_header_not_backfilled(self):
        self.assertEqual(self.parse('')['target_versions'], [])

    def test_original_preserved(self):
        field = 'PostgreSQL 17.2 (Debian build)'
        self.assertEqual(self.parse(field)['version_field'], field)

    def test_original_form_identity(self):
        self.assertTrue(self.parse('17.1')['is_original_form_report'])


if __name__ == '__main__':
    unittest.main()

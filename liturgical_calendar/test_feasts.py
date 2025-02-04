import unittest
from liturgical_calendar.feasts import lookup_feast

class TestLookupFeast(unittest.TestCase):
    def test_easter_feasts(self):
        self.assertEqual(lookup_feast('easter', -46)['name'], 'Ash Wednesday')
        self.assertEqual(lookup_feast('easter', 0)['name'], 'Easter')
        self.assertEqual(lookup_feast('easter', 49)['name'], 'Pentecost')

    def test_christmas_feasts(self):
        self.assertEqual(lookup_feast('christmas', '01-01')['name'], 'The Naming and Circumcision of Jesus')
        self.assertEqual(lookup_feast('christmas', '12-25')['name'], 'Christmas')
        self.assertEqual(lookup_feast('christmas', '01-06')['name'], 'Epiphany')

    def test_feast_types(self):
        self.assertEqual(lookup_feast('easter', -46)['type'], 'Principal Holy Day')
        self.assertEqual(lookup_feast('easter', 0)['type'], 'Principal Feast')
        self.assertEqual(lookup_feast('christmas', '01-06')['type'], 'Principal Feast')

    def test_feast_urls(self):
        self.assertEqual(lookup_feast('easter', -46)['url'], 'https://en.wikipedia.org/wiki/Ash_Wednesday')
        self.assertEqual(lookup_feast('christmas', '12-25')['url'], 'https://en.wikipedia.org/wiki/Christmas_Day')

if __name__ == '__main__':
    unittest.main()

import unittest
from liturgical_calendar.feasts import lookup_feast
from liturgical_calendar.readings import get_readings_for_date
from liturgical_calendar.liturgical import liturgical_calendar

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

class TestReadingsCycle(unittest.TestCase):
    def test_sunday_cycle(self):
        # Use Lent 1 in three consecutive years (A, B, C)
        sundays = [
            ('2023-02-26', 'A'),
            ('2024-02-18', 'B'),
            ('2025-03-09', 'C'),
        ]
        for date, cycle in sundays:
            info = liturgical_calendar(date)
            readings = get_readings_for_date(date, info)
            self.assertTrue(readings, f"No readings for {date} (cycle {cycle})")
            # Check that the readings are for the correct cycle by matching a known reading
            expected = {
                'A': 'Genesis 2:15-17; 3:1-7',
                'B': 'Genesis 9:8-17',
                'C': 'Deuteronomy 26:1-11',
            }[cycle]
            self.assertIn(expected, readings, f"Expected reading '{expected}' not found for {date} (cycle {cycle})")

    def test_weekday_cycle(self):
        # Monday after 2 before Lent in two years (cycle 1 and 2)
        weekdays = [
            ('2024-02-05', '1'),  # 2024 is even, weekday cycle 1
            ('2023-02-20', '2'),  # 2023 is odd, weekday cycle 2
        ]
        for date, cycle in weekdays:
            info = liturgical_calendar(date)
            readings = get_readings_for_date(date, info)
            self.assertTrue(readings, f"No readings for {date} (weekday cycle {cycle})")
            # The readings dict should be for the correct weekday cycle (by structure)
            # We can't check the key directly, but we can check that the readings are not identical
        # Ensure the readings for the two cycles are different
        info1 = liturgical_calendar(weekdays[0][0])
        info2 = liturgical_calendar(weekdays[1][0])
        r1 = get_readings_for_date(weekdays[0][0], info1)
        r2 = get_readings_for_date(weekdays[1][0], info2)
        self.assertNotEqual(r1, r2, "Readings for weekday cycles 1 and 2 should differ")

if __name__ == '__main__':
    unittest.main()

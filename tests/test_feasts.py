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

class TestWeekCalculation(unittest.TestCase):
    def test_specific_week_calculations(self):
        """Test specific week calculations that are known to be problematic"""
        test_cases = [
            ('2025-02-26', '2 before Lent', 'Should be 2 before Lent, not 1 before Lent'),
            ('2025-05-25', 'Easter 6', 'Should be Easter 6'),
            ('2025-06-22', 'Proper 7', 'Should be Proper 7'),
            ('2026-01-05', 'Christmas 2', 'Should be Christmas 2'),
            ('2026-01-20', 'Epiphany 2', 'Should be Epiphany 2'),
            ('2026-03-31', 'Holy Week', 'Should be Holy Week'),
            ('2026-04-30', 'Easter 4', 'Should be Easter 4'),
            ('2026-06-09', 'Proper 5', 'Should be Proper 5'),
            ('2026-02-12', '2 before Lent', 'Should be 2 before Lent'),
            ('2026-02-22', 'Lent 1', 'Should be Lent 1'),
            ('2026-02-23', 'Lent 1', 'Should be Lent 1 (weekday)'),
            ('2026-02-20', '1 before Lent', 'Should be 1 before Lent (weekday)'),
            ('2026-04-07', 'Easter 1', 'Should be Easter 1'),
            ('2026-05-30', 'Pentecost', 'Should be Pentecost'),
            ('2026-06-06', 'Trinity', 'Should be Trinity'),
            ('2026-11-30', 'Advent 1', 'Should be Advent 1'),
            ('2026-12-25', 'Advent 4', 'Should be Advent 4 (4th week of Advent)'),
        ]
        
        for date_str, expected_week, description in test_cases:
            with self.subTest(date=date_str, expected=expected_week):
                info = liturgical_calendar(date_str)
                actual_week = info.get('week', '')
                self.assertEqual(actual_week, expected_week, 
                               f"{description}: Expected '{expected_week}', got '{actual_week}' for {date_str}")
    
    def test_pre_lent_week_calculation(self):
        """Test the specific issue with 26 February 2025 being incorrectly calculated as '1 before Lent'"""
        # 26 February 2025 should be "2 before Lent", not "1 before Lent"
        info = liturgical_calendar('2025-02-26')
        self.assertEqual(info.get('week'), '2 before Lent', 
                        "26 February 2025 should be '2 before Lent', not '1 before Lent'")
        
        # Verify that 26 February 2025 is NOT Ash Wednesday
        self.assertNotEqual(info.get('name'), 'Ash Wednesday',
                           "26 February 2025 should not be Ash Wednesday")
        
        # Verify the season is correct (Pre-Lent becomes Ordinary Time after render_week_name)
        self.assertEqual(info.get('season'), 'Ordinary Time',
                        "26 February 2025 should be in Ordinary Time season (after render_week_name)")
    
    def test_easter_week_calculations(self):
        """Test Easter week calculations"""
        # 25 May 2025 should be Easter 6
        info = liturgical_calendar('2025-05-25')
        self.assertEqual(info.get('week'), 'Easter 6',
                        "25 May 2025 should be Easter 6")
        
        # 30 April 2026 should be Easter 4
        info = liturgical_calendar('2026-04-30')
        self.assertEqual(info.get('week'), 'Easter 4',
                        "30 April 2026 should be Easter 4")
    
    def test_christmas_epiphany_weeks(self):
        """Test Christmas and Epiphany week calculations"""
        # 5 Jan 2026 should be Christmas 2
        info = liturgical_calendar('2026-01-05')
        self.assertEqual(info.get('week'), 'Christmas 2',
                        "5 Jan 2026 should be Christmas 2")
        
        # 20 January 2026 should be Epiphany 2
        info = liturgical_calendar('2026-01-20')
        self.assertEqual(info.get('week'), 'Epiphany 2',
                        "20 January 2026 should be Epiphany 2")
    
    def test_holy_week_calculation(self):
        """Test Holy Week calculation"""
        # 31 March 2026 should be Holy Week
        info = liturgical_calendar('2026-03-31')
        self.assertEqual(info.get('week'), 'Holy Week',
                        "31 March 2026 should be Holy Week")
        self.assertEqual(info.get('season'), 'Holy Week',
                        "31 March 2026 should be in Holy Week season")
    
    def test_proper_week_calculation(self):
        """Test Proper week calculation"""
        # 22 June 2025 should be Proper 7
        info = liturgical_calendar('2025-06-22')
        self.assertEqual(info.get('week'), 'Proper 7',
                        "22 June 2025 should be Proper 7")
    
    def test_lent_weekday_calculation(self):
        """Test Lent weekday calculation"""
        # 20 Feb 2026 should be 1 before Lent (weekday)
        info = liturgical_calendar('2026-02-20')
        self.assertEqual(info.get('week'), '1 before Lent',
                        "20 Feb 2026 should be 1 before Lent (weekday)")
        self.assertEqual(info.get('season'), 'Lent',
                        "20 Feb 2026 should be in Lent season")
    
    def test_lent_week_1_calculation(self):
        """Test Lent 1 week calculation (22-28 Feb 2026)"""
        lent_1_dates = [
            '2026-02-22', '2026-02-23', '2026-02-24', '2026-02-25', 
            '2026-02-26', '2026-02-27', '2026-02-28'
        ]
        for date_str in lent_1_dates:
            with self.subTest(date=date_str):
                info = liturgical_calendar(date_str)
                self.assertEqual(info.get('week'), 'Lent 1',
                               f"{date_str} should be Lent 1")
                self.assertEqual(info.get('season'), 'Lent',
                               f"{date_str} should be in Lent season")
    
    def test_lent_week_2_calculation(self):
        """Test Lent 2 week calculation (1-7 March 2026)"""
        lent_2_dates = [
            '2026-03-01', '2026-03-02', '2026-03-03', '2026-03-04', 
            '2026-03-05', '2026-03-06', '2026-03-07'
        ]
        for date_str in lent_2_dates:
            with self.subTest(date=date_str):
                info = liturgical_calendar(date_str)
                self.assertEqual(info.get('week'), 'Lent 2',
                               f"{date_str} should be Lent 2")
                self.assertEqual(info.get('season'), 'Lent',
                               f"{date_str} should be in Lent season")
    
    def test_pentecost_and_trinity(self):
        """Test Pentecost and Trinity calculations"""
        # 30 May 2026 should be Pentecost
        info = liturgical_calendar('2026-05-30')
        self.assertEqual(info.get('week'), 'Pentecost',
                        "30 May 2026 should be Pentecost")
        self.assertEqual(info.get('season'), 'Pentecost',
                        "30 May 2026 should be in Pentecost season")
        
        # 6 June 2026 should be Trinity
        info = liturgical_calendar('2026-06-06')
        self.assertEqual(info.get('week'), 'Trinity',
                        "6 June 2026 should be Trinity")
        self.assertEqual(info.get('season'), 'Trinity',
                        "6 June 2026 should be in Trinity season")
    
    def test_trinity_2025(self):
        """Test Trinity week naming for 2025"""
        # Trinity Sunday 2025 should be "Trinity"
        info = liturgical_calendar('2025-06-15')
        self.assertEqual(info.get('week'), 'Trinity',
                        "15 June 2025 (Trinity Sunday) should be Trinity")
        self.assertEqual(info.get('season'), 'Trinity',
                        "15 June 2025 should be in Trinity season")
        
        # Next Sunday should be "Proper 7"
        info = liturgical_calendar('2025-06-22')
        self.assertEqual(info.get('week'), 'Proper 7',
                        "22 June 2025 (next Sunday) should be Proper 7")
        self.assertEqual(info.get('season'), 'Trinity',
                        "22 June 2025 should be in Trinity season")
    
    def test_season_transitions(self):
        """Test season transition points across multiple years"""
        # Test Advent to Christmas transition
        info = liturgical_calendar('2026-12-24')  # Christmas Eve
        self.assertEqual(info.get('season'), 'Advent',
                        "24 Dec 2026 should be in Advent season")
        
        info = liturgical_calendar('2026-12-25')  # Christmas Day
        self.assertEqual(info.get('season'), 'Christmas',
                        "25 Dec 2026 should be in Christmas season")
        
        # Test Christmas to Epiphany transition
        info = liturgical_calendar('2026-01-05')  # 12th Day of Christmas
        self.assertEqual(info.get('season'), 'Christmas',
                        "5 Jan 2026 should be in Christmas season")
        
        info = liturgical_calendar('2026-01-06')  # Epiphany
        self.assertEqual(info.get('season'), 'Epiphany',
                        "6 Jan 2026 should be in Epiphany season")
        
        # Test Epiphany to Ordinary Time transition (before Pre-Lent)
        info = liturgical_calendar('2026-02-01')  # Last day of Epiphany
        self.assertEqual(info.get('season'), 'Epiphany',
                        "1 Feb 2026 should be in Epiphany season")
        
        info = liturgical_calendar('2026-02-02')  # First day of Ordinary Time
        self.assertEqual(info.get('season'), 'Ordinary Time',
                        "2 Feb 2026 should be in Ordinary Time season")
        
        # Test Ordinary Time to Pre-Lent transition
        info = liturgical_calendar('2026-02-09')  # Ordinary Time
        self.assertEqual(info.get('season'), 'Ordinary Time',
                        "9 Feb 2026 should be in Ordinary Time season")
        
        info = liturgical_calendar('2026-02-10')  # Pre-Lent
        self.assertEqual(info.get('season'), 'Ordinary Time',  # After render_week_name
                        "10 Feb 2026 should be in Ordinary Time season (after render_week_name)")
        self.assertEqual(info.get('week'), '2 before Lent',
                        "10 Feb 2026 should be '2 before Lent'")
        
        # Test Pre-Lent to Lent transition
        info = liturgical_calendar('2026-02-17')  # Last day of Pre-Lent
        self.assertEqual(info.get('season'), 'Ordinary Time',
                        "17 Feb 2026 should be in Ordinary Time season (after render_week_name)")
        
        info = liturgical_calendar('2026-02-18')  # Ash Wednesday
        self.assertEqual(info.get('season'), 'Lent',
                        "18 Feb 2026 should be in Lent season")
        
        # Test Lent to Holy Week transition
        info = liturgical_calendar('2026-03-28')  # Last day of Lent
        self.assertEqual(info.get('season'), 'Lent',
                        "28 Mar 2026 should be in Lent season")
        
        info = liturgical_calendar('2026-03-29')  # Palm Sunday
        self.assertEqual(info.get('season'), 'Holy Week',
                        "29 Mar 2026 should be in Holy Week season")
        
        # Test Holy Week to Easter transition
        info = liturgical_calendar('2026-04-04')  # Last day of Holy Week
        self.assertEqual(info.get('season'), 'Holy Week',
                        "4 Apr 2026 should be in Holy Week season")
        
        info = liturgical_calendar('2026-04-05')  # Easter Sunday
        self.assertEqual(info.get('season'), 'Easter',
                        "5 Apr 2026 should be in Easter season")
        
        # Test Easter to Pentecost transition
        info = liturgical_calendar('2026-05-23')  # Last day of Easter
        self.assertEqual(info.get('season'), 'Easter',
                        "23 May 2026 should be in Easter season")
        
        info = liturgical_calendar('2026-05-24')  # Pentecost
        self.assertEqual(info.get('season'), 'Pentecost',
                        "24 May 2026 should be in Pentecost season")
        
        # Test Pentecost to Trinity transition
        info = liturgical_calendar('2026-05-30')  # Last day of Pentecost
        self.assertEqual(info.get('season'), 'Pentecost',
                        "30 May 2026 should be in Pentecost season")
        
        info = liturgical_calendar('2026-05-31')  # Trinity Sunday
        self.assertEqual(info.get('season'), 'Trinity',
                        "31 May 2026 should be in Trinity season")
    
    def test_edge_cases_multiple_years(self):
        """Test edge cases across multiple years to ensure consistency"""
        # Test leap year handling
        info = liturgical_calendar('2024-02-29')  # Leap day
        self.assertIsNotNone(info.get('season'),
                           "Leap day should have a valid season")
        
        # Test year boundary transitions
        info = liturgical_calendar('2025-12-31')  # New Year's Eve
        self.assertIsNotNone(info.get('season'),
                           "New Year's Eve should have a valid season")
        
        info = liturgical_calendar('2026-01-01')  # New Year's Day
        self.assertIsNotNone(info.get('season'),
                           "New Year's Day should have a valid season")
        
        # Test different Easter dates (early vs late Easter)
        # 2024: Easter on March 31 (early)
        info = liturgical_calendar('2024-03-31')
        self.assertEqual(info.get('season'), 'Easter',
                        "31 Mar 2024 should be in Easter season")
        
        # 2025: Easter on April 20 (late)
        info = liturgical_calendar('2025-04-20')
        self.assertEqual(info.get('season'), 'Easter',
                        "20 Apr 2025 should be in Easter season")
        
        # Test Pre-Advent (late in the year)
        info = liturgical_calendar('2026-11-20')  # Late November
        self.assertIsNotNone(info.get('season'),
                           "Late November should have a valid season")
    
    def test_week_number_edge_cases(self):
        """Test week number calculations at edge cases"""
        # Test week 1 of various seasons
        info = liturgical_calendar('2026-11-30')  # Advent 1
        self.assertEqual(info.get('week'), 'Advent 1',
                        "30 Nov 2026 should be Advent 1")
        
        info = liturgical_calendar('2026-12-25')  # Christmas 1 (Christmas Day)
        self.assertEqual(info.get('week'), 'Advent 4',
                        "25 Dec 2026 should be Advent 4")
        
        info = liturgical_calendar('2026-01-06')  # Epiphany 1
        self.assertEqual(info.get('week'), 'Christmas 2',
                        "6 Jan 2026 should be Christmas 2")
        
        # Test last weeks of seasons
        info = liturgical_calendar('2026-12-24')  # Last day of Advent
        self.assertEqual(info.get('season'), 'Advent',
                        "24 Dec 2026 should be in Advent season")
        
        info = liturgical_calendar('2026-01-05')  # Last day of Christmas
        self.assertEqual(info.get('season'), 'Christmas',
                        "5 Jan 2026 should be in Christmas season")

    def test_additional_edge_cases(self):
        """Test additional edge cases and transition points"""
        # Test very early and very late dates in the year
        info = liturgical_calendar('2026-01-01')  # New Year's Day
        self.assertIsNotNone(info.get('season'),
                           "1 Jan 2026 should have a valid season")
        
        info = liturgical_calendar('2026-12-31')  # New Year's Eve
        self.assertIsNotNone(info.get('season'),
                           "31 Dec 2026 should have a valid season")
        
        # Test leap year edge case
        info = liturgical_calendar('2024-02-29')  # Leap day
        self.assertIsNotNone(info.get('season'),
                           "29 Feb 2024 should have a valid season")
        
        # Test different years with different Easter dates
        # 2024: Early Easter (March 31)
        info = liturgical_calendar('2024-03-31')
        self.assertEqual(info.get('season'), 'Easter',
                        "31 Mar 2024 should be in Easter season")
        
        # 2025: Late Easter (April 20)
        info = liturgical_calendar('2025-04-20')
        self.assertEqual(info.get('season'), 'Easter',
                        "20 Apr 2025 should be in Easter season")
        
        # Test Pre-Advent period (very late in the year)
        info = liturgical_calendar('2026-11-20')  # Late November
        self.assertIsNotNone(info.get('season'),
                           "20 Nov 2026 should have a valid season")
        
        # Test mid-week transitions
        info = liturgical_calendar('2026-12-25')  # Christmas Day (Friday)
        self.assertEqual(info.get('season'), 'Christmas',
                        "25 Dec 2026 should be in Christmas season")
        
        info = liturgical_calendar('2026-12-26')  # Boxing Day (Saturday)
        self.assertEqual(info.get('season'), 'Christmas',
                        "26 Dec 2026 should be in Christmas season")
        
        info = liturgical_calendar('2026-12-27')  # Sunday after Christmas
        self.assertEqual(info.get('season'), 'Christmas',
                        "27 Dec 2026 should be in Christmas season")
    
    def test_weekday_vs_sunday_calculations(self):
        """Test that weekday and Sunday calculations are consistent"""
        # Test a week where we can check both Sunday and weekdays
        # 2026: February 1st is a Sunday (Epiphany 4)
        info = liturgical_calendar('2026-02-01')  # Sunday
        self.assertEqual(info.get('week'), 'Epiphany 4',
                        "1 Feb 2026 (Sunday) should be Epiphany 4")
        
        info = liturgical_calendar('2026-02-02')  # Monday
        self.assertEqual(info.get('week'), 'Epiphany 4',
                        "2 Feb 2026 (Monday) should be Epiphany 4")
        
        info = liturgical_calendar('2026-02-03')  # Tuesday
        self.assertEqual(info.get('week'), 'Epiphany 4',
                        "3 Feb 2026 (Tuesday) should be Epiphany 4")
        
        # Test Lent week consistency
        # 2026: February 22nd is a Sunday (Lent 1)
        info = liturgical_calendar('2026-02-22')  # Sunday
        self.assertEqual(info.get('week'), 'Lent 1',
                        "22 Feb 2026 (Sunday) should be Lent 1")
        
        info = liturgical_calendar('2026-02-23')  # Monday
        self.assertEqual(info.get('week'), 'Lent 1',
                        "23 Feb 2026 (Monday) should be Lent 1")
        
        info = liturgical_calendar('2026-02-24')  # Tuesday
        self.assertEqual(info.get('week'), 'Lent 1',
                        "24 Feb 2026 (Tuesday) should be Lent 1")

    def test_proper_weeks_first_and_last(self):
        """Test first and last Proper/Ordinary Sundays after Trinity"""
        # 2025: Trinity Sunday is 15 June, Proper 7 is 22 June
        info = liturgical_calendar('2025-06-22')  # Proper 7
        self.assertEqual(info.get('week'), 'Proper 7',
                        "22 Jun 2025 should be Proper 7")
        # Last Proper Sunday in 2025 (before Advent)
        info = liturgical_calendar('2025-11-23')  # Sunday before Advent
        self.assertEqual(info.get('week'), '1 before Advent',
                        "23 Nov 2025 should be '1 before Advent'")
        # 2028: Very late Trinity season (Advent starts Dec 3)
        info = liturgical_calendar('2028-11-26')  # Last Sunday before Advent
        self.assertTrue('Proper' in info.get('week') or 'Trinity' in info.get('week') or 'before Advent' in info.get('week'),
                        "26 Nov 2028 should be a Proper, Trinity, or 'before Advent' week")

    def test_advent_sunday_and_transition(self):
        """Test Advent Sunday and the Saturday before (season transition)"""
        # 2023: Advent 1 is Dec 3, Saturday before is Dec 2
        info = liturgical_calendar('2023-12-02')  # Saturday before Advent
        self.assertTrue(info.get('season') in ['Trinity', 'Ordinary Time', 'Pre-Advent'],
                        "2 Dec 2023 should be in Trinity/Ordinary/Pre-Advent season")
        info = liturgical_calendar('2023-12-03')  # Advent Sunday
        self.assertEqual(info.get('season'), 'Advent',
                        "3 Dec 2023 should be in Advent season")

    def test_christmas_eve_and_christmas_day_on_sunday(self):
        """Test Christmas Eve and Christmas Day, especially when Christmas falls on a Sunday"""
        # 2016: Christmas Day is Sunday
        info = liturgical_calendar('2016-12-18')  # Sunday before Christmas
        self.assertEqual(info.get('week'), 'Advent 4',
                        "18 Dec 2016 should be Advent 4 (week name)")
        info = liturgical_calendar('2016-12-24')  # Christmas Eve (Saturday)
        self.assertEqual(info.get('season'), 'Advent',
                        "24 Dec 2016 should be in Advent season")
        info = liturgical_calendar('2016-12-25')  # Christmas Day (Sunday)
        self.assertEqual(info.get('season'), 'Christmas',
                        "25 Dec 2016 should be in Christmas season")
        self.assertEqual(info.get('week'), 'Christmas 1',
                        "25 Dec 2016 should be Christmas 1 (week name)")

    def test_epiphany_on_sunday_vs_weekday(self):
        """Test Epiphany on a Sunday vs. a weekday (week naming logic)"""
        # 2017: Epiphany is Friday, 2012: Epiphany is Friday, 2011: Epiphany is Thursday
        info = liturgical_calendar('2017-01-06')  # Epiphany (Friday)
        self.assertEqual(info.get('season'), 'Epiphany',
                        "6 Jan 2017 should be in Epiphany season")
        # 2012: Epiphany is Friday, but check the following Sunday
        info = liturgical_calendar('2012-01-08')  # Sunday after Epiphany
        self.assertEqual(info.get('season'), 'Epiphany',
                        "8 Jan 2012 should be in Epiphany season")
        self.assertTrue('Epiphany' in info.get('week'),
                        "8 Jan 2012 should be an Epiphany week")
        # 2011: Epiphany is Thursday, Sunday after is Jan 9
        info = liturgical_calendar('2011-01-09')
        self.assertEqual(info.get('season'), 'Epiphany',
                        "9 Jan 2011 should be in Epiphany season")
        self.assertTrue('Epiphany' in info.get('week'),
                        "9 Jan 2011 should be an Epiphany week")

    def test_christmas_and_epiphany_on_sunday(self):
        """Test years where Christmas or Epiphany falls on a Sunday (week naming and season logic)"""
        # 2016: Christmas Day is Sunday
        info = liturgical_calendar('2016-12-25')
        self.assertEqual(info.get('season'), 'Christmas',
                        "25 Dec 2016 should be in Christmas season")
        self.assertEqual(info.get('week'), 'Christmas 1',
                        "25 Dec 2016 should be Christmas 1 (week name)")
        info = liturgical_calendar('2016-12-18')  # Sunday before Christmas
        self.assertEqual(info.get('week'), 'Advent 4',
                        "18 Dec 2016 should be Advent 4 (week name)")
        # 2011: Epiphany is Thursday, Sunday after is Jan 9
        info = liturgical_calendar('2011-01-09')
        self.assertEqual(info.get('season'), 'Epiphany',
                        "9 Jan 2011 should be in Epiphany season")
        self.assertTrue('Epiphany' in info.get('week'),
                        "9 Jan 2011 should be an Epiphany week")

    def test_multi_year_robustness(self):
        """Test multi-year robustness for early/late Easters and Advent 4 on Christmas Eve"""
        # Early Easter: 2008 (March 23)
        info = liturgical_calendar('2008-03-23')  # Easter
        self.assertEqual(info.get('season'), 'Easter',
                        "23 Mar 2008 should be in Easter season")
        # Late Easter: 2011 (April 24)
        info = liturgical_calendar('2011-04-24')  # Easter
        self.assertEqual(info.get('season'), 'Easter',
                        "24 Apr 2011 should be in Easter season")
        # Advent 4 on Christmas Eve: 2017
        info = liturgical_calendar('2017-12-24')  # Advent 4 and Christmas Eve
        self.assertEqual(info.get('season'), 'Advent',
                        "24 Dec 2017 should be in Advent season")
        self.assertEqual(info.get('week'), 'Advent 4',
                        "24 Dec 2017 should be Advent 4 (week name)")

if __name__ == '__main__':
    unittest.main()

"""
Unit tests for the SeasonCalculator class.

These tests verify that the SeasonCalculator correctly handles all liturgical
season calculations including season determination, week numbers, and weekday readings.
"""

import unittest
from datetime import date
from liturgical_calendar.core.season_calculator import SeasonCalculator
from liturgical_calendar.funcs import date_to_days, get_easter, get_advent_sunday


class TestSeasonCalculator(unittest.TestCase):
    """Test cases for the SeasonCalculator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calculator = SeasonCalculator()
    
    def test_determine_season_pre_lent(self):
        """Test season determination for Pre-Lent period."""
        # Test dates in Pre-Lent (easter_point between -62 and -47)
        test_date = date(2025, 2, 16)  # Septuagesima Sunday
        easter_point = -49
        christmas_point = -68
        advent_sunday = -21
        
        season = self.calculator.determine_season(test_date, easter_point, christmas_point, advent_sunday)
        self.assertEqual(season, 'Pre-Lent')
    
    def test_determine_season_advent(self):
        """Test season determination for Advent."""
        test_date = date(2025, 12, 1)  # First Sunday of Advent
        easter_point = 250  # Some positive value
        christmas_point = -24  # Before Christmas
        advent_sunday = -24
        
        season = self.calculator.determine_season(test_date, easter_point, christmas_point, advent_sunday)
        self.assertEqual(season, 'Advent')
    
    def test_determine_season_christmas(self):
        """Test season determination for Christmas."""
        test_date = date(2025, 12, 25)  # Christmas Day
        easter_point = 250
        christmas_point = 0  # Christmas Day
        advent_sunday = -24
        
        season = self.calculator.determine_season(test_date, easter_point, christmas_point, advent_sunday)
        self.assertEqual(season, 'Christmas')
    
    def test_determine_season_epiphany(self):
        """Test season determination for Epiphany."""
        test_date = date(2026, 1, 6)  # Epiphany
        easter_point = 250
        christmas_point = 12  # After Christmas
        advent_sunday = -24
        
        season = self.calculator.determine_season(test_date, easter_point, christmas_point, advent_sunday)
        self.assertEqual(season, 'Epiphany')
    
    def test_determine_season_lent(self):
        """Test season determination for Lent."""
        test_date = date(2025, 3, 5)  # Ash Wednesday
        easter_point = -46  # Ash Wednesday
        christmas_point = 70
        advent_sunday = -24
        
        season = self.calculator.determine_season(test_date, easter_point, christmas_point, advent_sunday)
        self.assertEqual(season, 'Lent')
    
    def test_determine_season_holy_week(self):
        """Test season determination for Holy Week."""
        test_date = date(2025, 4, 13)  # Palm Sunday
        easter_point = -7  # Palm Sunday
        christmas_point = 109
        advent_sunday = -24
        
        season = self.calculator.determine_season(test_date, easter_point, christmas_point, advent_sunday)
        self.assertEqual(season, 'Holy Week')
    
    def test_determine_season_easter(self):
        """Test season determination for Easter."""
        test_date = date(2025, 4, 20)  # Easter Sunday
        easter_point = 0  # Easter Sunday
        christmas_point = 116
        advent_sunday = -24
        
        season = self.calculator.determine_season(test_date, easter_point, christmas_point, advent_sunday)
        self.assertEqual(season, 'Easter')
    
    def test_determine_season_pentecost(self):
        """Test season determination for Pentecost."""
        test_date = date(2025, 6, 8)  # Pentecost Sunday
        easter_point = 49  # Pentecost Sunday
        christmas_point = 165
        advent_sunday = -24
        
        season = self.calculator.determine_season(test_date, easter_point, christmas_point, advent_sunday)
        self.assertEqual(season, 'Pentecost')
    
    def test_determine_season_trinity(self):
        """Test season determination for Trinity."""
        test_date = date(2025, 6, 15)  # Trinity Sunday
        easter_point = 56  # Trinity Sunday
        christmas_point = 172
        advent_sunday = -24
        
        season = self.calculator.determine_season(test_date, easter_point, christmas_point, advent_sunday)
        self.assertEqual(season, 'Trinity')
    
    def test_calculate_week_number_pre_lent(self):
        """Test week number calculation for Pre-Lent."""
        test_date = date(2025, 2, 16)  # Septuagesima Sunday
        easter_point = -49
        christmas_point = -68
        advent_sunday = -21
        dayofweek = 0  # Sunday
        
        weekno = self.calculator.calculate_week_number(test_date, easter_point, christmas_point, advent_sunday, dayofweek)
        self.assertEqual(weekno, 1)
    
    def test_calculate_week_number_advent(self):
        """Test week number calculation for Advent."""
        test_date = date(2025, 12, 1)  # First Sunday of Advent
        easter_point = 250
        christmas_point = -24
        advent_sunday = -24
        dayofweek = 0  # Sunday
        
        weekno = self.calculator.calculate_week_number(test_date, easter_point, christmas_point, advent_sunday, dayofweek)
        self.assertEqual(weekno, 1)
    
    def test_calculate_week_number_christmas(self):
        """Test week number calculation for Christmas."""
        test_date = date(2025, 12, 25)  # Christmas Day
        easter_point = 250
        christmas_point = 0
        advent_sunday = -24
        dayofweek = 3  # Wednesday
        
        weekno = self.calculator.calculate_week_number(test_date, easter_point, christmas_point, advent_sunday, dayofweek)
        self.assertEqual(weekno, 1)
    
    def test_calculate_week_number_lent(self):
        """Test week number calculation for Lent."""
        test_date = date(2025, 3, 9)  # First Sunday of Lent
        easter_point = -42  # First Sunday of Lent
        christmas_point = 74
        advent_sunday = -24
        dayofweek = 0  # Sunday
        
        weekno = self.calculator.calculate_week_number(test_date, easter_point, christmas_point, advent_sunday, dayofweek)
        self.assertEqual(weekno, 1)
    
    def test_calculate_week_number_easter(self):
        """Test week number calculation for Easter."""
        test_date = date(2025, 4, 20)  # Easter Sunday
        easter_point = 0
        christmas_point = 116
        advent_sunday = -24
        dayofweek = 0  # Sunday
        
        weekno = self.calculator.calculate_week_number(test_date, easter_point, christmas_point, advent_sunday, dayofweek)
        self.assertEqual(weekno, 1)
    
    def test_calculate_weekday_reading_pre_lent(self):
        """Test weekday reading calculation for Pre-Lent."""
        test_date = date(2025, 2, 16)  # Septuagesima Sunday
        easter_point = -49
        christmas_point = -68
        advent_sunday = -21
        dayofweek = 0
        days = 2460000  # Example Julian day
        easterday = 2460049  # Example Easter Julian day
        
        reading = self.calculator.calculate_weekday_reading(test_date, easter_point, christmas_point, 
                                                          advent_sunday, dayofweek, days, easterday)
        # render_week_name returns "1 before Lent" for Pre-Lent week 1
        self.assertEqual(reading, '1 before Lent')
    
    def test_calculate_weekday_reading_advent(self):
        """Test weekday reading calculation for Advent."""
        test_date = date(2025, 12, 1)  # First Sunday of Advent
        easter_point = 250
        christmas_point = -24
        advent_sunday = -24
        dayofweek = 0
        days = 2460000
        easterday = 2459750
        
        reading = self.calculator.calculate_weekday_reading(test_date, easter_point, christmas_point, 
                                                          advent_sunday, dayofweek, days, easterday)
        self.assertEqual(reading, 'Advent 1')
    
    def test_calculate_weekday_reading_christmas(self):
        """Test weekday reading calculation for Christmas."""
        test_date = date(2025, 12, 25)  # Christmas Day
        easter_point = 250
        christmas_point = 0
        advent_sunday = -24
        dayofweek = 3
        days = 2460000
        easterday = 2459750
        
        reading = self.calculator.calculate_weekday_reading(test_date, easter_point, christmas_point, 
                                                          advent_sunday, dayofweek, days, easterday)
        self.assertEqual(reading, 'Christmas 1')
    
    def test_calculate_weekday_reading_holy_week(self):
        """Test weekday reading calculation for Holy Week."""
        test_date = date(2025, 4, 13)  # Palm Sunday
        easter_point = -7
        christmas_point = 109
        advent_sunday = -24
        dayofweek = 0
        days = 2460000
        easterday = 2460007
        
        reading = self.calculator.calculate_weekday_reading(test_date, easter_point, christmas_point, 
                                                          advent_sunday, dayofweek, days, easterday)
        self.assertEqual(reading, 'Holy Week')
    
    def test_calculate_weekday_reading_pentecost(self):
        """Test weekday reading calculation for Pentecost."""
        test_date = date(2025, 6, 8)  # Pentecost Sunday
        easter_point = 49
        christmas_point = 165
        advent_sunday = -24
        dayofweek = 0
        days = 2460000
        easterday = 2459951
        
        reading = self.calculator.calculate_weekday_reading(test_date, easter_point, christmas_point, 
                                                          advent_sunday, dayofweek, days, easterday)
        self.assertEqual(reading, 'Pentecost')
    
    def test_calculate_weekday_reading_trinity(self):
        """Test weekday reading calculation for Trinity."""
        test_date = date(2025, 6, 15)  # Trinity Sunday
        easter_point = 56
        christmas_point = 172
        advent_sunday = -24
        dayofweek = 0
        days = 2460000
        easterday = 2459944
        
        reading = self.calculator.calculate_weekday_reading(test_date, easter_point, christmas_point, 
                                                          advent_sunday, dayofweek, days, easterday)
        self.assertEqual(reading, 'Trinity')
    
    def test_calculate_weekday_reading_before_advent(self):
        """Test weekday reading calculation for weeks before Advent."""
        # Use 2025-11-23, which is '1 before Advent' (Christ the King)
        test_date = date(2025, 11, 23)
        year = test_date.year
        month = test_date.month
        day = test_date.day
        dayofweek = test_date.weekday()
        # Convert to 0=Sunday, 6=Saturday
        dayofweek = 0 if test_date.isoweekday() == 7 else test_date.isoweekday()
        days = date_to_days(year, month, day)
        easterm, easterd = get_easter(year)
        easterday = date_to_days(year, easterm, easterd)
        easter_point = days - easterday
        if month > 2:
            christmas_point = days - date_to_days(year, 12, 25)
        else:
            christmas_point = days - date_to_days(year-1, 12, 25)
        advent_sunday = get_advent_sunday(year)
        reading = self.calculator.calculate_weekday_reading(
            test_date, easter_point, christmas_point, advent_sunday, dayofweek, days, easterday)
        self.assertEqual(reading, '1 before Advent')
    
    def test_render_week_name(self):
        """Test week name rendering."""
        season = 'Advent'
        weekno = 1
        easter_point = 250
        
        week_name, rendered_season = self.calculator.render_week_name(season, weekno, easter_point)
        self.assertEqual(week_name, 'Advent 1')
        self.assertEqual(rendered_season, 'Advent')
    
    def test_calculate_sunday_week_info(self):
        """Test Sunday week info calculation for weekdays."""
        # Use 2025-12-02 (Monday after Advent 1)
        test_date = date(2025, 12, 2)
        dayofweek = test_date.weekday()
        # Convert to 0=Sunday, 6=Saturday
        dayofweek = 0 if test_date.isoweekday() == 7 else test_date.isoweekday()
        days = date_to_days(test_date.year, test_date.month, test_date.day)
        easterm, easterd = get_easter(test_date.year)
        easterday = date_to_days(test_date.year, easterm, easterd)
        year = test_date.year
        sunday_season, sunday_weekno = self.calculator.calculate_sunday_week_info(
            test_date, dayofweek, days, easterday, year)
        self.assertEqual(sunday_season, 'Advent')
        self.assertEqual(sunday_weekno, 1)


if __name__ == '__main__':
    unittest.main() 
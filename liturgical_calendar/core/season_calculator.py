"""
Season calculation logic for the liturgical calendar.

This module contains the SeasonCalculator class which handles all season-related
calculations including determining liturgical seasons, week numbers, and weekday readings.
"""

from datetime import date
from typing import Tuple, Optional

from ..funcs import (
    get_easter, get_advent_sunday, date_to_days, day_of_week, 
    add_delta_days, render_week_name
)


class SeasonCalculator:
    """
    Handles liturgical season calculations including season determination,
    week number calculation, and weekday reading assignment.
    """
    
    def __init__(self):
        """Initialize the SeasonCalculator."""
        pass
    
    def determine_season(self, f_date: date, easter_point: int, 
                        christmas_point: int, advent_sunday: int) -> str:
        """
        Determine the liturgical season for a given date.
        
        Args:
            f_date: The date to calculate the season for
            easter_point: Days from Easter (negative = before, positive = after)
            christmas_point: Days from Christmas (negative = before, positive = after)
            advent_sunday: Days from Christmas to Advent Sunday
            
        Returns:
            The liturgical season name
        """
        # Pre-Lent: check before Ordinary Time
        if easter_point >= -62 and easter_point <= -47:
            return 'Pre-Lent'
        elif christmas_point >= advent_sunday and christmas_point <= -1:
            return 'Advent'
        elif christmas_point >= 0 and christmas_point <= 11:
            return 'Christmas'
        elif christmas_point >= 12 and christmas_point < 40:
            return 'Epiphany'
        elif easter_point <= -62:
            return 'Ordinary Time'
        elif easter_point > -47 and easter_point < -7:
            return 'Lent'
        elif easter_point >= -7 and easter_point < 0:
            return 'Holy Week'
        elif easter_point >= 0 and easter_point < 49:
            return 'Easter'
        elif easter_point >= 49 and easter_point < 56:
            return 'Pentecost'
        else:
            return 'Trinity'
    
    def calculate_week_number(self, f_date: date, easter_point: int, 
                            christmas_point: int, advent_sunday: int, 
                            dayofweek: int) -> int:
        """
        Calculate the liturgical week number for a given date.
        
        Args:
            f_date: The date to calculate the week number for
            easter_point: Days from Easter (negative = before, positive = after)
            christmas_point: Days from Christmas (negative = before, positive = after)
            advent_sunday: Days from Christmas to Advent Sunday
            dayofweek: Day of week (0 = Sunday, 1 = Monday, etc.)
            
        Returns:
            The liturgical week number
        """
        year = f_date.year
        
        if easter_point >= -62 and easter_point <= -47:
            # Calculate which Sunday before Lent this date belongs to
            # -49 is the Sunday of "1 before Lent", -56 is "2 before Lent", etc.
            # For weekdays, we need to find which Sunday week this belongs to
            return ((-49 - easter_point + dayofweek) // 7) + 1
        elif christmas_point >= advent_sunday and christmas_point <= -1:
            return 1 + (christmas_point - advent_sunday) // 7
        elif christmas_point >= 0 and christmas_point <= 11:
            # The Twelve Days of Christmas.
            # Christmas Day (christmas_point = 0) should always be week 1
            if christmas_point == 0:
                return 1
            else:
                return 1 + (christmas_point - dayofweek) // 7
        elif christmas_point >= 12 and christmas_point < 40:
            return 1 + (christmas_point - 12 - dayofweek) // 7
        elif easter_point <= -62:
            # Period of Ordinary Time after Epiphany (before Pre-Lent)
            from ..funcs import get_week_number
            return get_week_number(f_date) - 5
        elif easter_point > -47 and easter_point < -7:
            # Week 1 of Lent is the first Sunday after Ash Wednesday (easter_point = -46)
            # For weekdays, we need to calculate which week this belongs to
            # The first Sunday after Ash Wednesday is at easter_point = -40 (6 days after Ash Wednesday)
            # For any date, find which Sunday of Lent it belongs to
            # The first Sunday of Lent is at easter_point = -42 (first Sunday after Ash Wednesday)
            # Calculate which Sunday of Lent this date represents
            first_sunday_lent_easter_point = -42
            weeks_from_first_sunday = (easter_point - first_sunday_lent_easter_point + dayofweek) // 7
            return max(1, weeks_from_first_sunday + 1)
        elif easter_point >= -7 and easter_point < 0:
            return 0
        elif easter_point >= 0 and easter_point < 49:
            # If it's a Sunday, week calculation is correct; for weekdays, subtract 1
            if dayofweek == 0:
                return 1 + easter_point // 7
            else:
                weekno = easter_point // 7
                if weekno < 1:
                    weekno = 1
                return weekno
        elif easter_point >= 49 and easter_point < 56:
            # Period of Ordinary Time after Pentecost
            return 0
        else:
            # Period of Ordinary Time after Pentecost
            from ..funcs import get_week_number
            return get_week_number(f_date) - 18
    
    def calculate_weekday_reading(self, f_date: date, easter_point: int, 
                                christmas_point: int, advent_sunday: int, 
                                dayofweek: int, days: int, easterday: int) -> Optional[str]:
        """
        Calculate the weekday reading for a given date.
        
        Args:
            f_date: The date to calculate the weekday reading for
            easter_point: Days from Easter (negative = before, positive = after)
            christmas_point: Days from Christmas (negative = before, positive = after)
            advent_sunday: Days from Christmas to Advent Sunday
            dayofweek: Day of week (0 = Sunday, 1 = Monday, etc.)
            days: Julian day number for the date
            easterday: Julian day number for Easter
            
        Returns:
            The weekday reading name or None
        """
        year = f_date.year
        
        if easter_point >= -62 and easter_point <= -47:
            # Pre-Lent weekday_reading
            return render_week_name('Pre-Lent', ((-49 - easter_point + dayofweek) // 7) + 1, easter_point)[0]
        elif christmas_point >= advent_sunday and christmas_point <= -1:
            # Advent weekday_reading
            return render_week_name('Advent', 1 + (christmas_point - advent_sunday) // 7, easter_point)[0]
        elif christmas_point >= 0 and christmas_point <= 11:
            # Christmas weekday_reading
            if christmas_point == 0:
                return 'Christmas 1'
            else:
                return render_week_name('Christmas', 1 + (christmas_point - dayofweek) // 7, easter_point)[0]
        elif christmas_point >= 12 and christmas_point < 40:
            # Epiphany weekday_reading
            weekno = max(1, 1 + (christmas_point - 12 - dayofweek) // 7)
            return render_week_name('Epiphany', weekno, easter_point)[0]
        elif easter_point > -47 and easter_point < -7:
            # Lent weekday_reading
            # For weekdays, use the week number of the Sunday that starts this week
            if dayofweek == 0:
                # It's a Sunday, use the current week number
                first_sunday_lent_easter_point = -42
                weeks_from_first_sunday = (easter_point - first_sunday_lent_easter_point + dayofweek) // 7
                weekno = max(1, weeks_from_first_sunday + 1)
                return render_week_name('Lent', weekno, easter_point)[0]
            else:
                # It's a weekday, calculate the Sunday's week number
                sunday_days = days - dayofweek
                sunday_y, sunday_m, sunday_d = add_delta_days(sunday_days)
                sunday_days_from_epoch = date_to_days(sunday_y, sunday_m, sunday_d)
                sunday_easter_point = sunday_days_from_epoch - easterday
                first_sunday_lent_easter_point = -42
                sunday_weeks_from_first_sunday = (sunday_easter_point - first_sunday_lent_easter_point) // 7
                sunday_weekno = max(1, sunday_weeks_from_first_sunday + 1)
                return render_week_name('Lent', sunday_weekno, easter_point)[0]
        elif easter_point >= -7 and easter_point < 0:
            # Holy Week weekday_reading
            return 'Holy Week'
        elif easter_point >= 0 and easter_point < 49:
            # Easter weekday_reading
            if dayofweek == 0:
                weekno = 1 + easter_point // 7
            else:
                weekno = easter_point // 7
                if weekno < 1:
                    weekno = 1
            return render_week_name('Easter', weekno, easter_point)[0]
        elif easter_point >= 49 and easter_point < 56:
            # Pentecost weekday_reading
            return 'Pentecost'
        elif easter_point >= 56 and easter_point < 63:
            # Trinity Sunday
            return 'Trinity'
        else:
            # Trinity weekday_reading or 'N before Advent' for the last four weeks before Advent
            # Calculate weeks until Advent Sunday using absolute day numbers
            advent_sunday_abs = date_to_days(year, 12, 25) + advent_sunday
            weeks_until_advent = (advent_sunday_abs - days) // 7
            if 0 <= weeks_until_advent <= 4:
                # 0 = Advent Sunday itself, 1-4 = weeks before Advent
                if weeks_until_advent == 0:
                    return 'Advent 1'
                else:
                    return f"{weeks_until_advent} before Advent"
            else:
                trinity_week = (easter_point - 56) // 7 + 1
                return f"Trinity {trinity_week}"
    
    def render_week_name(self, season: str, weekno: int, easter_point: int) -> Tuple[str, str]:
        """
        Render a week name with or without number.
        
        Args:
            season: The liturgical season
            weekno: The week number
            easter_point: Days from Easter (negative = before, positive = after)
            
        Returns:
            Tuple of (week_name, season)
        """
        return render_week_name(season, weekno, easter_point)
    
    def calculate_sunday_week_info(self, f_date: date, dayofweek: int, days: int, 
                                  easterday: int, year: int) -> Tuple[str, int]:
        """
        Calculate the week information for the Sunday that starts the current week.
        Used for weekdays to determine which Sunday's season and week number to use.
        
        Args:
            f_date: The current date
            dayofweek: Day of week (0 = Sunday, 1 = Monday, etc.)
            days: Julian day number for the current date
            easterday: Julian day number for Easter
            year: The year
            
        Returns:
            Tuple of (sunday_season, sunday_weekno)
        """
        # Go back to the previous Sunday
        sunday_days = days - dayofweek
        sunday_y, sunday_m, sunday_d = add_delta_days(sunday_days)
        sunday_date = date(sunday_y, sunday_m, sunday_d)
        
        # Calculate the liturgical info for the Sunday
        sunday_days_from_epoch = date_to_days(sunday_y, sunday_m, sunday_d)
        sunday_easter_point = sunday_days_from_epoch - easterday
        sunday_christmas_point = (sunday_days_from_epoch - date_to_days(sunday_y, 12, 25) 
                                 if sunday_m > 2 
                                 else sunday_days_from_epoch - date_to_days(sunday_y-1, 12, 25))
        sunday_advent_sunday = get_advent_sunday(sunday_y)
        
        # Determine the Sunday's season and week number
        sunday_season = self.determine_season(sunday_date, sunday_easter_point, 
                                            sunday_christmas_point, sunday_advent_sunday)
        sunday_weekno = self.calculate_week_number(sunday_date, sunday_easter_point, 
                                                 sunday_christmas_point, sunday_advent_sunday, 0)
        
        return sunday_season, sunday_weekno 
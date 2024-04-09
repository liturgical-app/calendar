"""
Helper functions for date manipulation
"""

from datetime import date, timedelta
from dateutil.easter import easter

def get_easter(year: int) -> tuple:
    """
    Returns the date easter occurs on for a given year as (month,day)

    Parameters
    ----------
      year: int
        The year to perform the calculation for
    Return
    ------
      month: int
        The month that Easter falls in
      day: int
        The day that Easter falls on
    """
    easter_date = easter(year)
    easter_month = easter_date.month
    easter_day = easter_date.day
    return easter_month, easter_day


def get_advent_sunday(year: int) -> int:
    """
    Return date of Advent Sunday, in days relative to Christmas day
    This is always negative as Advent Sunday is before Christmas day

    Parameters
    ----------
      year: int
        The year to perform the calculation for
    Return
    ------
      offset: int
        The numnber of days that Advent Sunday falls before Christmas day
    """
    return -(day_of_week(year,12,25) + 3*7)

def date_to_days(year: int, month: int, day: int) -> int:
    """
    Convert a date from year,month,day to days since 1st January, 1 AD

    Parameters
    ----------
      year: int
        The year to convert
      month: int
        The month to convert
      day: int
        The day to convert
    Return
    ------
      offset: int
        The numnber of days since 1st January, 1 AD
    """
    # Define a start date as passed in
    f_date = date(year, month, day)
    epoch = date(1, 1, 1)
    delta = f_date - epoch
    return delta.days

def day_of_week(year: int, month: int, day: int) -> int:
    """
    Return day of week for any given date in year,month,day format
    between 0-6 where 0 is Sunday, i.e. the first day of the week
    Compare with:
      weekday() which is 0-6 and 0 is Monday
      isoweekday() which is 1-7 and 1 is Monday

    Parameters
    ----------
      year: int
        Year to perform the calculation for
      month: int
        Month to perform the calculation for
      day: int
        Day to perform the calculation for
    Return
    ------
      weekday: int
        Numerical day of the week in the range 0-6, where 0 is Sunday
    """

    # Define a start date as passed in
    f_date = date(year, month, day)

    # Get ISO week day, in range 1-7
    weekday = f_date.isoweekday()

    # Rewrite 7=Sunday as 0=Sunday
    return 0 if weekday == 7 else weekday

def add_delta_days(days: int) -> tuple:
    """
    Convert days since 1st January, 1 AD back to year,month, day

    Parameters
    ----------
      days: int
        Days since 1st January, 1 AD
    Return
    ------
      year: int
        Year of the date [days] since 1st January, 1 AD
      month: int
        Month of the date [days] since 1st January, 1 AD
      day: int
        Day of the date [days] since 1st January, 1 AD
    """
    epoch = date(1, 1, 1)
    end_date = epoch + timedelta(days=days)
    return end_date.year, end_date.month, end_date.day


def colour_code(colour: str) -> str:
    """
    Accept a colour name and return a hex colour code

    Parameters
    ----------
      colour: str
        The name of a colour
    Return
    ------
      code: str
        The corresponding hex code for the named colour
    """
    codes = {
        'white': '#ffffff',
        'red': '#ce0002',
        'rose': '#eb597a',
        'purple': '#664fa6',
        'green': '#279942',
        'not given': '#000000'
    }

    return codes.get(colour)

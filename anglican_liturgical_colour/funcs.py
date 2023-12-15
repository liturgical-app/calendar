"""
Helper functions for date manipulation
"""

from datetime import date
from dateutil.easter import easter
from juliandate import to_gregorian, from_gregorian

def get_easter(year):
    """
    Returns the date easter occurs on for a given year as (month,day)
    """
    easter_date = easter(year)
    easter_month = easter_date.month
    easter_day = easter_date.day
    return easter_month, easter_day


def get_advent_sunday(year):
    """
    Return date of Advent Sunday, in days relative to Christmas day
    """
    return -(day_of_week(year,12,25) + 4*7)

def date_to_days(year, month, day):
    """
    Convert a date from year,month,day to Julian days
    """
    return from_gregorian(year, month, day)

def day_of_week(year, month, day):
    """
    Return ISO day of week for any given date in year,month,day format
    """

    # Define a start date as passed in
    f_date = date(year, month, day)

    # Return ISO week day, in range 1-7
    return f_date.isoweekday()

def add_delta_days(days):
    """
    Convert Julian date back to year,month, day
    """
    year, mon, day, hour, min, sec, micro = to_gregorian(days)
    return year, mon, day

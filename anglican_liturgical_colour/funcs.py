"""
Helper functions for date manipulation
"""

from datetime import date
from dateutil.easter import easter

def get_easter(year):
    """
    Returns the date easter occurs on for a given year as (month,day)
    """
    easter_date = easter(year)
    easter_month = easter_date.month
    easter_day = easter_date.day
    return (easter_month, easter_day)


def get_advent_sunday(year):
    """
    Return date of Advent Sunday, in days relative to Christmas day
    """
    return -(day_of_week(year,12,25) + 4*7)

def date_to_days(year, month, day):
    """
    Convert a date from year,month,day to Julian days
    """

    # Define a start date as passed in
    f_date = date(year, month, day)

    # Define an end date as 1st of January of the year 1 A.D.
    # This is defined in Perl Date::Calm
    l_date = date(1, 1, 1)

    # Calculate the difference between the end date and start date
    delta = l_date - f_date

    # Print the number of days in the time difference
    return delta.days

def day_of_week(year, month, day):
    """
    Return ISO day of week for any given date in year,month,day format
    """

    # Define a start date as passed in
    f_date = date(year, month, day)

    # Return ISO week day, in range 1-7
    return f_date.isoweekday()

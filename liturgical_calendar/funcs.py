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
        The number of days that Advent Sunday falls before Christmas day
    """
    christmas = date(year, 12, 25)
    possible_advent = christmas - timedelta(days=28)
    # Move forward to the next Sunday if needed
    while possible_advent.weekday() != 6:  # 6 = Sunday in Python's weekday()
        possible_advent += timedelta(days=1)
    offset = (possible_advent - christmas).days
    return offset

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

def get_week_number(given_date: date) -> int:
  """
  Return the week number of the year where the week starts on a Sunday

  Parameters
  ----------
    given_date: date
    The date as a datetime.date object
  Return
  ------
    week: int
    The week number of the year
  """
  start_of_year = date(given_date.year, 1, 1)
  start_of_year_weekday = start_of_year.weekday()
  if start_of_year_weekday != 6:
    start_of_year += timedelta(days=(6 - start_of_year_weekday))
  delta_days = (given_date - start_of_year).days
  return delta_days // 7 + 1

def render_week_name(season, weekno, easter_point=None):
    """
    Render a Week name with or without number
    """
    if weekno and weekno > 0:
        # Check if this is the first week of Trinity (easter_point 56-62)
        if season == 'Trinity' and easter_point is not None and 56 <= easter_point < 63:
            week = 'Trinity'
        elif season in ['Ordinary Time', 'Trinity']:
            weekname = 'Proper'
            week = f"{weekname} {weekno}"
        else:
            weekname = season
            week = f"{weekname} {weekno}"

        # Deal with Pre-Lent and Pre-Advent week names (but don't change season)
        if season in ['Pre-Lent', 'Pre-Advent']:
            weekname = season.removeprefix('Pre-')
            week = f"{weekno} before {weekname}"
    else:
        week = season

    return week, season

def get_cache_filename(source_url):
    """
    Generate a cache filename based on the source URL.
    Uses a hash of the URL to ensure unique filenames.
    """
    import hashlib
    from urllib.parse import urlparse
    # Create a hash of the URL
    url_hash = hashlib.md5(source_url.encode()).hexdigest()
    # Try to extract a meaningful name from the URL
    parsed = urlparse(source_url)
    path_parts = parsed.path.split('/')
    # Look for the post ID in Instagram URLs
    if 'instagram.com' in source_url:
        for part in path_parts:
            if part and part != 'p':
                return f"instagram_{part}_{url_hash[:8]}.jpg"
    # Fallback to just the hash
    return f"image_{url_hash}.jpg"
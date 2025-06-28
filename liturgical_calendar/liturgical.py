"""
This Python module will return the name, season, week number and liturgical
colour for any day in the Gregorian calendar, according to the Anglican
tradition of the Church of England.
"""

import sys
from datetime import datetime, date

from .funcs import get_easter, get_advent_sunday, date_to_days, day_of_week, add_delta_days, colour_code, get_week_number, render_week_name
from .feasts import lookup_feast
from .readings import get_readings_for_date
from .artwork import get_image_source_for_date

##########################################################################

def determine_season_for_date(f_date, easter_point, christmas_point, advent_sunday):
    """
    Determine the liturgical season for a given date.
    This is extracted from the main liturgical_calendar function for reuse.
    """
    year = f_date.year
    month = f_date.month
    day = f_date.day
    dayofweek = day_of_week(year, month, day)
    
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

def calculate_week_number(f_date, easter_point, christmas_point, advent_sunday, dayofweek):
    """
    Calculate the liturgical week number for a given date.
    This is extracted from the main liturgical_calendar function for reuse.
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
        return get_week_number(f_date) - 18

def liturgical_calendar(s_date: str, transferred: bool = False):
    """
    Return the liturgical colour for a given day
    This func contains the main logic
    """

    # s_date could in a variety of formats
    # We standardise to f_date as a Date
    if isinstance(s_date, datetime):
        # If datetime, strip it to the date
        f_date = s_date.date()
    elif isinstance(s_date, date):
        # If date, accept it
        f_date = s_date
    elif isinstance(s_date, str):
        # If string, try to parse a YYYY-MM-DD
        f_date = datetime.strptime(s_date, "%Y-%m-%d").date()
    else:
        # Otherwise use today's date
        f_date = date.today()

    # Extract the components from the date
    year = f_date.year
    month = f_date.month
    day = f_date.day
    dayofweek = day_of_week(year, month, day)

    #die "Need to specify year, month and day" unless $y and $m and $d;

    # Calculate some values in Julian date
    days = date_to_days(year, month, day)
    easterm, easterd = get_easter(year)
    easterday = date_to_days(year, easterm, easterd)

    possibles = []

    # "The Church Year consists of two cycles of feasts and holy days: one is
    #  dependent upon the movable date of the Sunday of the Resurrection or
    #  Easter Day; the other, upon the fixed date of December 25, the Feast
    #  of our Lord's Nativity or Christmas Day."
    easter_point = days-easterday
    christmas_point = 0

    # We will store the amount of time until (-ve) or since (+ve) Christmas in
    # christmas_point. Let's make the cut-off date the end of February,
    # since we'll be dealing with Easter-based dates after that, and it
    # avoids the problems of considering leap years.
    if month>2:
        christmas_point = days - date_to_days(year, 12, 25)
    else:
        christmas_point = days - date_to_days(year-1, 12, 25)

    # First, figure out the season.
    season = determine_season_for_date(f_date, easter_point, christmas_point, get_advent_sunday(year))

    # Calculate week number
    weekno = calculate_week_number(f_date, easter_point, christmas_point, get_advent_sunday(year), dayofweek)
    weekday_reading = None

    advent_sunday = get_advent_sunday(year)

    # Set season_url based on season
    season_urls = {
        'Advent': 'https://en.wikipedia.org/wiki/Advent',
        'Christmas': 'https://en.wikipedia.org/wiki/Christmastide',
        'Epiphany': 'https://en.wikipedia.org/wiki/Epiphany_season',
        'Ordinary Time': 'https://en.wikipedia.org/wiki/Ordinary_Time',
        'Pre-Lent': 'https://en.wikipedia.org/wiki/Septuagesima',
        'Lent': 'https://en.wikipedia.org/wiki/Lent',
        'Holy Week': 'https://en.wikipedia.org/wiki/Holy_Week',
        'Easter': 'https://en.wikipedia.org/wiki/Eastertide',
        'Pentecost': 'https://en.wikipedia.org/wiki/Ordinary_Time',
        'Trinity': 'https://en.wikipedia.org/wiki/Ordinary_Time',
        'Pre-Advent': 'https://en.wikipedia.org/wiki/Ordinary_Time'
    }
    season_url = season_urls.get(season, 'https://en.wikipedia.org/wiki/Ordinary_Time')

    # Handle special cases that need weekday_reading
    if easter_point >= -62 and easter_point <= -47:
        # Pre-Lent weekday_reading
        weekday_reading = render_week_name('Pre-Lent',  ((-49 - easter_point + dayofweek) // 7) + 1, easter_point)[0]
    elif christmas_point >= advent_sunday and christmas_point <= -1:
        # Advent weekday_reading
        weekday_reading = render_week_name('Advent', 1 + (christmas_point - advent_sunday) // 7, easter_point)[0]
    elif christmas_point >= 0 and christmas_point <= 11:
        # Christmas weekday_reading
        if christmas_point == 0:
            weekday_reading = 'Christmas 1'
        else:
            weekday_reading = render_week_name('Christmas', 1 + (christmas_point - dayofweek) // 7, easter_point)[0]
    elif christmas_point >= 12 and christmas_point < 40:
        # Epiphany weekday_reading
        weekno = max(1, 1 + (christmas_point - 12 - dayofweek) // 7)
        weekday_reading = render_week_name('Epiphany', weekno, easter_point)[0]
    elif easter_point > -47 and easter_point < -7:
        # Lent weekday_reading
        # For weekdays, use the week number of the Sunday that starts this week
        if dayofweek == 0:
            # It's a Sunday, use the current week number
            first_sunday_lent_easter_point = -42
            weeks_from_first_sunday = (easter_point - first_sunday_lent_easter_point + dayofweek) // 7
            weekno = max(1, weeks_from_first_sunday + 1)
            weekday_reading = render_week_name('Lent', weekno, easter_point)[0]
        else:
            # It's a weekday, calculate the Sunday's week number
            sunday_days = days - dayofweek
            sunday_y, sunday_m, sunday_d = add_delta_days(sunday_days)
            sunday_days_from_epoch = date_to_days(sunday_y, sunday_m, sunday_d)
            sunday_easter_point = sunday_days_from_epoch - easterday
            first_sunday_lent_easter_point = -42
            sunday_weeks_from_first_sunday = (sunday_easter_point - first_sunday_lent_easter_point) // 7
            sunday_weekno = max(1, sunday_weeks_from_first_sunday + 1)
            weekday_reading = render_week_name('Lent', sunday_weekno, easter_point)[0]
    elif easter_point >= -7 and easter_point < 0:
        # Holy Week weekday_reading
        weekday_reading = 'Holy Week'
    elif easter_point >= 0 and easter_point < 49:
        # Easter weekday_reading
        if dayofweek == 0:
            weekno = 1 + easter_point // 7
        else:
            weekno = easter_point // 7
            if weekno < 1:
                weekno = 1
        weekday_reading = render_week_name('Easter', weekno, easter_point)[0]
    elif easter_point >= 49 and easter_point < 56:
        # Pentecost weekday_reading
        weekday_reading = 'Pentecost'
    elif easter_point >= 56 and easter_point < 63:
        # Trinity Sunday
        weekday_reading = 'Trinity'
    else:
        # Trinity weekday_reading or 'N before Advent' for the last four weeks before Advent
        # Calculate weeks until Advent Sunday using absolute day numbers
        advent_sunday_abs = date_to_days(year, 12, 25) + advent_sunday
        weeks_until_advent = (advent_sunday_abs - days) // 7
        if 0 <= weeks_until_advent <= 4:
            # 0 = Advent Sunday itself, 1-4 = weeks before Advent
            if weeks_until_advent == 0:
                weekday_reading = 'Advent 1'
            else:
                weekday_reading = f"{weeks_until_advent} before Advent"
        else:
            trinity_week = (easter_point - 56) // 7 + 1
            weekday_reading = f"Trinity {trinity_week}"

    # Render a Week name with or without number
    # For weekdays, determine the week name based on the Sunday that starts the week
    if dayofweek == 0:
        # It's a Sunday, use the current season
        # Special case: if weekday_reading is "N before Advent", use that for the week name too
        if weekday_reading and weekday_reading.endswith(' before Advent'):
            week = weekday_reading
        else:
            week, season = render_week_name(season, weekno, easter_point)
    else:
        # It's a weekday, calculate what the season would be for the Sunday that starts this week
        # Go back to the previous Sunday
        sunday_days = days - dayofweek
        sunday_y, sunday_m, sunday_d = add_delta_days(sunday_days)
        sunday_date = date(sunday_y, sunday_m, sunday_d)
        
        # Calculate the liturgical info for the Sunday
        sunday_days_from_epoch = date_to_days(sunday_y, sunday_m, sunday_d)
        sunday_easter_point = sunday_days_from_epoch - easterday
        sunday_christmas_point = sunday_days_from_epoch - date_to_days(sunday_y, 12, 25) if sunday_m > 2 else sunday_days_from_epoch - date_to_days(sunday_y-1, 12, 25)
        sunday_advent_sunday = get_advent_sunday(sunday_y)
        
        # Determine the Sunday's season and week number using the helper functions
        sunday_season = determine_season_for_date(sunday_date, sunday_easter_point, sunday_christmas_point, sunday_advent_sunday)
        sunday_weekno = calculate_week_number(sunday_date, sunday_easter_point, sunday_christmas_point, sunday_advent_sunday, 0)  # 0 = Sunday
        
        # Use the Sunday's season and week number to render the week name
        week, _ = render_week_name(sunday_season, sunday_weekno, sunday_easter_point)

    # Only set weekno to None if it's not positive and not Pre-Lent, Christmas, or Lent
    if weekno is not None and int(weekno) > 0:
        weekno = int(weekno)
    elif season not in ['Pre-Lent', 'Christmas', 'Lent']:
        weekno = None

    # Change Pre-Lent and Pre-Advent seasons to Ordinary Time for the final result
    if season in ['Pre-Lent', 'Pre-Advent']:
        season = 'Ordinary Time'

    # Now, look for feasts.
    feast_from_easter    = lookup_feast('easter', easter_point)
    feast_from_christmas = lookup_feast('christmas', "%02d-%02d" % (month, day))

    if feast_from_easter:
        possibles.append(feast_from_easter)

    if feast_from_christmas:
        possibles.append(feast_from_christmas)

    # Maybe transferred from yesterday.
    # Call recursively to look for yesterday feast and push to possibles
    if transferred is False:
        yestery, yesterm, yesterd = add_delta_days(days-1)

        transferred_feast = liturgical_calendar(s_date=f"{yestery}-{yesterm}-{yesterd}", transferred=True)

        if transferred_feast:
            transferred_feast['name'] = transferred_feast['name'] + ' (transferred)'
            # Sundays can't be transferred
            if transferred_feast['prec'] != 5:
                possibles.append(transferred_feast)


    # Maybe a Sunday
    # Shouldn't need to trap weekno=0 here, as the weekno increments on
    # a Sunday so it can never be less than 1 on a Sunday
    if dayofweek == 0:
        possibles.append({ 'prec': 5, 'type': 'Sunday', 'name': f"{season} {weekno}" })

    # So, which event takes priority?
    possibles = sorted(possibles, key=lambda x: x['prec'], reverse=True)

    if transferred:
        # If two feasts coincided today, we were asked to find
        # the one which got transferred.
        # But Sundays don't get transferred!
        try:
            if possibles[0] and possibles[0]['prec'] == 5:
                return None
            return possibles[1]
        except IndexError:
            return None

    # Get highest priority feast
    try:
        result = possibles.pop(0)
    except IndexError:
        result = { 'name': '', 'prec': 1 }

    # Append season info regardless
    result['season'] = season
    result['season_url'] = season_url
    result['weekno'] = weekno
    result['week'] = week
    result['date'] = f_date
    result['weekday_reading'] = weekday_reading 

    # Support for special Sundays which are rose
    if result['name'] in [ 'Advent 3', 'Lent 4' ]:
        result['colour'] = 'rose'

    # If no colour is already set...
    if result.get('colour') is None:
        # If the priority is higher than a Lesser Festival, but not a Sunday...
        if result['prec'] > 4 and result['prec'] != 5:
            # It's a feast day.
            # Feasts are generally white, unless marked differently.
            # But martyrs are red
            if result.get('martyr'):
                result['colour'] = 'red'
            else:
                result['colour'] = 'white'
        else:
            # Not a feast day.
            # Set a default colour for the season
            if season == 'Advent':
                result['colour'] = 'purple'
            elif season == 'Christmas':
                result['colour'] = 'white'
            elif season == 'Epiphany':
                result['colour'] = 'white'
            elif season == 'Lent':
                result['colour'] = 'purple'
            elif season == 'Holy Week':
                result['colour'] = 'red'
            elif season == 'Easter':
                result['colour'] = 'white'
            else:
                # The great fallback:
                result['colour'] = 'green'

    # Two special cases for Christmas-based festivals which
    # depend on the day of the week.
    if result['prec'] == 5: # An ordinary Sunday
        if christmas_point == advent_sunday:
            result['name'] = 'Advent Sunday'
            result['colour'] = 'white'
        elif christmas_point == advent_sunday-7:
            result['name'] = 'Christ the King'
            result['colour'] = 'white'

    # Set colour code
    result['colourcode'] = colour_code(result['colour'])

    if 'readings' not in result:
        result['readings'] = get_readings_for_date(f_date.strftime("%Y-%m-%d"), result)
    else:
        if result['prec'] < 5:
            result['readings'] += get_readings_for_date(f_date.strftime("%Y-%m-%d"), result)

    # Get artwork for this date
    artwork = get_image_source_for_date(f_date.strftime("%Y-%m-%d"), result)
    if artwork:
        result['artwork'] = artwork

    return result

def main():
    """
    Display liturgical info to a human user
    """

    # Read in args
    if len(sys.argv) > 1:
        mydate = sys.argv[1]
    else:
        mydate = None

    info = liturgical_calendar(mydate)
    for key, value in info.items():
        print(key, ':', value)

if __name__ == '__main__':
    main()

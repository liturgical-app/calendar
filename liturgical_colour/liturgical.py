"""
This Python module will return the name, season, week number and liturgical
colour for any day in the Gregorian calendar, according to the Anglican
tradition of the Church of England.
"""

import sys
from datetime import datetime, date
from .funcs import get_easter, get_advent_sunday, date_to_days, day_of_week, add_delta_days
from .feasts import lookup_feast

##########################################################################

def liturgical_colour(s_date: str, transferred: bool = False):
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
    season = ''
    weekno = None

    advent_sunday = get_advent_sunday(year)

    if easter_point > -47 and easter_point < 0:
        season = 'Lent'
        weekno = (easter_point+50) // 7
        # The ECUSA calendar seems to indicate that Easter Eve ends
        # Lent *and* begins the Easter season. I'm not sure how. Maybe it's
        # in both? Maybe the daytime is in Lent and the night is in Easter?
    elif easter_point >= 0 and easter_point <= 49:
        # yes, this is correct: Pentecost itself is in Easter season;
        # Pentecost season actually begins on the day after Pentecost.
        # Its proper name is "The Season After Pentecost".
        season = 'Easter'
        weekno = easter_point // 7
    elif christmas_point >= advent_sunday and christmas_point <= -1:
        season = 'Advent'
        weekno = 1 + (christmas_point-advent_sunday) // 7
    elif christmas_point >= 0 and christmas_point <= 11:
        # The Twelve Days of Christmas.
        season = 'Christmas'
        weekno = 1 + christmas_point // 7
    elif christmas_point >= 12 and easter_point <= -47:
        season = 'Epiphany'
        weekno = 1 + (christmas_point-12) // 7
    else:
        season = 'Pentecost'
        weekno = 1 + (easter_point - 49) // 7
    weekno = int(weekno)

    # Now, look for feasts.
    feast_from_easter    = lookup_feast(easter_point)
    feast_from_christmas = lookup_feast(10000+100*month+day)

    if feast_from_easter:
        possibles.append(feast_from_easter)

    if feast_from_christmas:
        possibles.append(feast_from_christmas)

    # Maybe transferred from yesterday.
    # Call recursively to look for yesterday feast and push to possibles
    if transferred is False:
        yestery, yesterm, yesterd = add_delta_days(days-1)
        transferred_feast = liturgical_colour(s_date=f"{yestery}-{yesterm}-{yesterd}", transferred=True)

        if transferred_feast:
            transferred_feast['name'] = transferred_feast['name'] + ' (transferred)'
            possibles.append(transferred_feast)

    # Maybe a Sunday.
    if day_of_week(year, month, day) == 7:
        possibles.append({ 'prec': 5, 'name': f"{season} {weekno}" })

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
    result['weekno'] = weekno
    result['date'] = f_date

    # Support for special Sundays which are rose
    if result['name'] in [ 'Advent 2', 'Lent 3' ]:
        result['colour'] = 'rose'
        result['colourcode'] = '##ff57a0'

    if result.get('colour') is None:
        if result['prec'] > 2 and result['prec'] != 5:
            # feasts are generally white, unless marked differently.
            # But martyrs are red
            if result.get('martyr'):
                result['colour'] = 'red'
                result['colourcode'] = '#a11c08'
            else:
                result['colour'] = 'white'
                result['colourcode'] = '#ffffff'
        else:
            # Not a feast day.
            if season == 'Lent':
                result['colour'] = 'purple'
                result['colourcode'] = '#ad099a'
            elif season == 'Advent':
                result['colour'] = 'purple'
                result['colourcode'] = '#ad099a'
            else:
                # The great fallback:
                result['colour'] = 'green'
                result['colourcode'] = '#03bf00'

    # Two special cases for Christmas-based festivals which
    # depend on the day of the week.
    if result['prec'] == 5: # An ordinary Sunday
        if christmas_point == advent_sunday:
            result['name'] = 'Advent Sunday'
            result['colour'] = 'white'
            result['colourcode'] = '#ffffff'
        elif christmas_point == advent_sunday-7:
            result['name'] = 'Christ the King'
            result['colour'] = 'white'
            result['colourcode'] = '#ffffff'

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

    info = liturgical_colour(mydate)
    for key, value in info.items():
        print(key, ':', value)

if __name__ == '__main__':
    main()

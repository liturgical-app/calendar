import json
from datetime import datetime
from .funcs import get_easter
from .readings_data import sunday_readings, weekday_readings

def get_yearly_cycle(year):
    """
    Determine the lectionary cycle for the given year.
    :param year: The year to determine the cycle for.
    :return: The cycle (A, B, or C) for Sundays and (1 or 2) for weekdays.
    """
    sunday_cycle = ['A', 'B', 'C'][(year - 1) % 3]
    weekday_cycle = 1 if year % 2 == 0 else 2
    return sunday_cycle, weekday_cycle

def get_readings_for_date(date_str, liturgical_info):
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    year = date.year
    month = date.month
    day = date.day

    # Determine the lectionary cycle for the year
    sunday_cycle, weekday_cycle = get_yearly_cycle(year)

    # Check if the date is a Sunday
    if date.weekday() == 6:  # Sunday is represented by 6
        week = liturgical_info['week']
        return sunday_readings.get(week, {}).get(sunday_cycle, {})
    
    else:
        week = liturgical_info['weekday_reading'] if liturgical_info['weekday_reading'] != None else liturgical_info['week']
        day_of_week = date.strftime('%A')  # Get the day of the week (e.g., 'Monday')
        return weekday_readings.get(week, {}).get(day_of_week, {}).get(str(weekday_cycle), {})

    return {}
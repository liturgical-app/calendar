# Liturgical Calendar

This Python module will return the name, season, week number and liturgical
colour for any day in the Gregorian calendar, according to the Anglican
tradition of the Church of England.

This module's algorithm is a direct port to Python of
[`DateTime::Calendar::Liturgical::Christian`](https://github.com/gitpan/DateTime-Calendar-Liturgical-Christian),
which was originally written in Perl and loaded with the calendar of the Episcopal
Church of the USA. It has now been fed with data from the Church of England's
[Calendar of saints](https://en.wikipedia.org/wiki/Calendar_of_saints_(Church_of_England))
and substantially modified to suit the Anglican calendar.

The output of this module is compared against the
[Church of England Lectionary](https://www.chpublishing.co.uk/features/lectionary),
which is taken to be the canonical source.

## Background

Some churches use a special church calendar. Days and seasons within the year
may be either "fasts" (solemn times) or "feasts" (joyful times). The year is
structured around the greatest feast in the calendar, the festival of the
Resurrection of Jesus, known as Easter, and the second greatest feast, the
festival of the Nativity of Jesus, known as Christmas. Before Christmas and
Easter there are solemn fast seasons known as Advent and Lent respectively.
After Christmas comes the feast of Epiphany, and after Easter comes the feast
of Pentecost. These days have the adjacent seasons named after them.

The church's new year falls on Advent Sunday, which occurs around the start of
December. Then follows the four-week fast season of Advent, then comes the
Christmas season, which lasts twelve days; then comes Epiphany, then the
forty days of Lent. Then comes Easter, then the long season of Pentecost
(which some churches call Trinity, after the feast which falls soon after
Pentecost). Then the next year begins and we return to Advent again.

Along with all these, the church remembers the women and men who have made
a positive difference in church history by designating feast days for them,
usually on the anniversary of their death. For example, we remember St. Andrew
on the 30th day of November in the Western churches. Every Sunday is the feast
day of Jesus, and if it has no other name is numbered according to the
season in which it falls. So, for example, the third Sunday in Pentecost
season would be called Pentecost 3.

Seasons are traditionally assigned colours, which are used for clothing and
other materials. The major feasts are coloured white or gold. Fasts are
purple. Feasts for martyrs (people who died for their faith) are red.
Other days are green.

## Installation

```console
pip install liturgical-calendar
```

## Usage, as a command

Once installed, this can be run at the command line. Currently it prints
an object with various attributes. This portion of the module needs
improvement, although it is probably more useful as a library.

Specify the date in YYYY-MM-DD format, or leave blank to return info
for today.

```console
# Get info for today
$ liturgical_calendar
name : 
prec : 1
season : Lent
season_url : https://en.wikipedia.org/wiki/Lent
weekno : 1
week : Lent 1
date : 2025-03-13
colour : purple
colourcode : #664fa6
ember : 0

# Get info for an arbitrary date
$ liturgical_calendar 2023-01-25
name : The Conversion of Paul
url : https://en.wikipedia.org/wiki/Conversion_of_Paul
prec : 7
type : Festival
type_url : https://en.wikipedia.org/wiki/Festival_(Church_of_England)
season : Epiphany
season_url : https://en.wikipedia.org/wiki/Epiphany_season
weekno : 3
week : Epiphany 3
date : 2023-01-25
colour : white
colourcode : #ffffff
ember : 0
```

## Usage, as a library

```py
# Get info for today
dayinfo = liturgical_calendar()

# Get info for an arbitrary date
# Date can be expressed as a string in YYYY-MM-DD format, a Datetime object, or a Date object
dayinfo = liturgical_calendar('YYYY-MM-DD')

# Access the attributes individually
print(dayinfo['colour'])
```

## Issues

If you find bugs (either in the code or in the calendar), please
[create an issue on GitHub](https://github.com/liturgical-app/calendar/issues).

Pull requests are always welcome, either to address bugs or add new features.

## Example

There is a sample app which uses this library called
[Liturgical Colour App](https://github.com/djjudas21/liturgical-colour-app).

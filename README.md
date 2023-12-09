# anglican-liturgical-colour

## NAME

DateTime::Calendar::Liturgical::Christian - calendar of the church year

## SYNOPSIS

 $dtclc = DateTime::Calendar::Liturgical::Christian->new(
    day=>4,
    month=>6,
    year=>2006);

 print $dtclc->name();    # 'Pentecost'
 print $dtclc->colour();  # 'red'

## DESCRIPTION

This module will return the name, season, week number and liturgical colour
for any day in the Gregorian calendar. It will eventually support the
liturgical calendars of several churches (hopefully at least Anglican,
Lutheran, Orthodox and Roman Catholic). At present it only knows the calendar
for the Episcopal Church of the USA.

If you find bugs, or if you have information on the calendar of another
liturgical church, please do let me know (thomas at thurman dot org dot uk).

## OVERVIEW

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

## CONSTRUCTOR

=over 4

### new ([ OPTIONS ])

This constructs a DateTime::Calendar::Liturgical::Christian object. It takes
a series of named options. Possible options are:

**year** (required). The year AD in the Gregorian calendar.

**month** (required). The month number in the Gregorian calendar. 1 is January.

**day** (required). The day of the month.

**tradition** (recommended). The tradition to use. Currently only `ECUSA` is known.

**advent_blue**. It is currently popular in ECUSA to colour Advent blue,
instead of purple, which will happen if this option is set to 1.

**bvm_blue**. Some people mark feasts of the Blessed Virgin Mary, the mother of
Jesus, with blue instead of white. This will happen if this option is set to 1.
To tell the difference between this blue and `advent_blue`'s blue, see the
`bvm` method, below.

**rose**. Some people colour the middle Sundays of Lent and Advent pink, or
"rose", instead of purple. This will happen if this option is set to 1.

### from_object ( OBJECT )

Constructs a DateTime::Calendar::Liturgical::Christian object from an object
of any other DateTime class.

=back

## METHODS

=over 4

### name

Returns the name of the feast, if any.

### season

Returns the season.

### colour

Returns the colour of the day. Can be `red`, `green`, `white`, or `purple`,
or `blue` or `rose` if the relevant options are set.

### color

Alternative spelling of `colour`.

### bvm

Returns true if the current day is a feast of the Blessed Virgin Mary. This
can be used to distinguish Advent blue from Marian blue.

### day

Returns the day number which was used to construct the object.

### month

Returns the month number which was used to construct the object.

### year

Returns the year number which was used to construct the object.

=back

## SEE ALSO

`DateTime`.

## COPYRIGHT

Copyright (c) 2006 Thomas Thurman.
This program is free software; you can redistribute it and/or modify it
under the same terms as Perl itself.

If you use this software, please consider sending me an email at
thomas at thurman dot org dot uk, so that I can see where it's being used.

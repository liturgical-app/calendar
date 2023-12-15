# DateTime::Calendar::Liturgical::Christian         -*- cperl -*-
#
# This program is free software; you may distribute it under the same
# conditions as Perl itself.
#
# Copyright (c) 2006 Thomas Thurman <thomas@thurman.org.uk>
#
##########################################################################

from dateutil.easter import *
from datetime import date, today
import sys

##########################################################################

feasts = {

    # Anglican Holy Days are variously categorised as Principal Feasts, Festivals, Lesser Festivals, or Commemorations
    # The observance of Lesser Festivals or Commemorations is optional.
    # Principal Feasts = prec 9
    # Festivals        = prec 7
    # Sundays          = prec 5
    # Lesser Festivals = prec 4
    # Commemorations   = prec 3

    # Dates relative to Easter are encoded as the number of days after Easter.

    # Principal Feasts (precedence is 9)
    0 : { 'name': 'Easter', 'prec':9 },
    39: { 'name': 'Ascension', 'prec':9 },
    49: { 'name': 'Pentecost', 'colour': 'red', 'prec':9 },
    56: { 'name': 'Trinity', 'prec':9 },

    # And others:
    -46: { 'name': 'Ash Wednesday', 'colour':'purple', 'prec':7 },
    # is the colour of Shrove Tuesday right?
    -47: { 'name': 'Shrove Tuesday', 'colour':'white', 'prec':7 }, 
    # Actually, Easter Eve doesn't have a colour
    -1: { 'name': 'Easter Eve', 'colour':'purple', 'prec':7 },
    -2: { 'name': 'Good Friday', 'colour':'purple', 'prec':7 },

    50: { 'name': 'Book of Common Prayer', 'prec':3 },

    # Dates relative to Christmas are encoded as 10000 + 100*m + d for simplicity.
    10101: { 'name': 'The Naming and Circumcision of Jesus', 'prec':7},
    10102: { 'name': 'Basil the Great and Gregory of Nazianzus', 'prec':4},
    10106: { 'name': 'Epiphany', 'prec':9},
    10110: { 'name': 'William Laud', 'prec':3},
    10111: { 'name': 'Mary Slessor', 'prec':3},
    10112: { 'name': 'Aelred of Hexham', 'prec':4},
    10113: { 'name': 'Hilary', 'prec':4},
    10117: { 'name': 'Antony', 'prec':4},
    10118: { 'name': 'Amy Carmichael', 'prec':3},
    10119: { 'name': 'Wulfstan', 'prec':4},
    10120: { 'name': 'Richard Rolle of Hampole', 'prec':3},
    10121: { 'name': 'Agnes', 'prec':4},
    10122: { 'name': 'Vincent', 'martyr':1, 'prec':3},
    10124: { 'name': 'Francis de Sales', 'prec':4},
    10125: { 'name': 'The Conversion of Paul', 'prec':7},
    10126: { 'name': 'Timothy and Titus', 'prec':4},
    10128: { 'name': 'Thomas Aquinas', 'prec':4},
    10130: { 'name': 'Charles, King and Martyr', 'martyr':1, 'prec':4},
    10131: { 'name': 'John Bosco', 'prec':3},

    10201: { 'name': 'Brigid of Kildare', 'prec':3},
    10202: { 'name': 'Candlemas', 'prec':9},
    10203: { 'name': 'Anskar', 'prec':4},
    10204: { 'name': 'Gilbert of Sempringham', 'prec':3},
    10206: { 'name': 'Martyrs of Japan', 'martyr':1, 'prec':3},
    10210: { 'name': 'Scholastica', 'prec':3},
    10214: { 'name': 'Valentine', 'martyr':1, 'prec':4},
    10215: { 'name': 'Thomas Bray', 'prec':3},
    10217: { 'name': 'Janani Luwum', 'martyr':1, 'prec':4},
    10223: { 'name': 'Polycarp', 'martyr':1, 'prec':4},
    10227: { 'name': 'George Herbert', 'prec':4},

    10301: { 'name': 'David', 'prec':4},
    10302: { 'name': 'Chad', 'prec':4},
    10307: { 'name': 'Perpetua, Felicity and their Companions', 'martyr':1, 'prec':4},
    10308: { 'name': 'Edward King', 'prec':4},
    10317: { 'name': 'Patrick', 'prec':4},
    10318: { 'name': 'Cyril', 'prec':3},
    10319: { 'name': 'Joseph of Nazareth', 'prec':7},
    10320: { 'name': 'Cuthbert', 'prec':4},
    10321: { 'name': 'Thomas Cranmer', 'martyr':1, 'prec':4},
    10324: { 'name': 'Walter Hilton of Thurgarton', 'prec':3},
    10325: { 'name': 'Annunciation of our Lord', 'prec':9},
    10326: { 'name': 'Harriet Monsell', 'prec':3},
    10331: { 'name': 'John Donne', 'prec':3},

    10401: { 'name': 'Frederick Denison Maurice', 'prec':3},
    10409: { 'name': 'Dietrich Bonhoeffer', 'martyr':1, 'prec':3},
    10410: { 'name': 'William Law', 'prec':4},
    10411: { 'name': 'George Augustus Selwyn', 'prec':3},
    10416: { 'name': 'Isabella Gilmore', 'prec':3},
    10419: { 'name': 'Alphege', 'martyr':1, 'prec':4},
    10421: { 'name': 'Anselm', 'prec':4},
    10423: { 'name': 'George', 'martyr':1, 'prec':7},
    10424: { 'name': 'Mellitus', 'prec':3},
    10425: { 'name': 'Mark the Evangelist', 'prec':7},
    10427: { 'name': 'Christina Rossetti', 'prec':3},
    10428: { 'name': 'Peter Chanel', 'martyr':1, 'prec':3},
    10429: { 'name': 'Catherine of Siena', 'prec':4},
    10430: { 'name': 'Pandita Mary Ramabai', 'prec':3},

    10501: { 'name': 'Philip and James, Apostles', 'prec':7},
    10502: { 'name': 'Athanasius', 'prec':4},
    10504: { 'name': 'English Saints and Martyrs of the Reformation Era', 'prec':4},
    10508: { 'name': 'Julian of Norwich', 'prec':4},
    10512: { 'name': 'Gregory Dix', 'prec':3},
    10514: { 'name': 'Matthias the Apostle', 'prec':7},
    10516: { 'name': 'Caroline Chisholm', 'prec':3},
    10519: { 'name': 'Dunstan', 'prec':4},
    10520: { 'name': 'Alcuin', 'prec':4},
    10521: { 'name': 'Helena', 'prec':3},
    10524: { 'name': 'John and Charles Wesley', 'prec':4},
    10525: { 'name': 'Bede', 'prec':4},
    10526: { 'name': 'Augustine of Canterbury', 'prec':4},
    10528: { 'name': 'Lanfranc', 'prec':3},
    10530: { 'name': 'Josephine Butler', 'prec':4},
    10531: { 'name': 'The Visit of the Blessed Virgin Mary to Elizabeth', 'prec':7},

    10601: { 'name': 'Justin', 'martyr':1, 'prec':4},
    10602: { 'name': 'Martyrs of Lyons', 'martyr':1, 'prec':3},
    10603: { 'name': 'Martyrs of Uganda', 'martyr':1, 'prec':3},
    10604: { 'name': 'Petroc', 'prec':3},
    10605: { 'name': 'Boniface', 'prec':4},
    10606: { 'name': 'Ini Kopuria', 'prec':3},
    10608: { 'name': 'Thomas Ken', 'prec':4},
    10609: { 'name': 'Columba', 'prec':4},
    10610: { 'name': 'Ephrem of Edessa', 'prec':3},
    10611: { 'name': 'Barnabas the Apostle', 'prec':7},
    10614: { 'name': 'Richard Baxter', 'prec':3},
    10615: { 'name': 'Evelyn Underhill', 'prec':3},
    10616: { 'name': 'Richard of Chichester', 'prec':4},
    10617: { 'name': 'Samuel and Henrietta Barnett', 'prec':3},
    10618: { 'name': 'Bernard Mizeki', 'prec':3},
    10619: { 'name': 'Sundar Singh of India', 'prec':3},
    10622: { 'name': 'Alban', 'martyr':1, 'prec':4},
    10623: { 'name': 'Etheldreda', 'prec':4},
    10624: { 'name': 'The Birth of John the Baptist', 'prec':7},
    10627: { 'name': 'Cyril', 'prec':3},
    10628: { 'name': 'Irenaeus', 'prec':4},
    10629: { 'name': 'Peter and Paul, Apostles', 'martyr':1, 'prec':7},

    10701: { 'name': 'Henry, John, and Henry Venn the younger', 'prec':3},
    10703: { 'name': 'Thomas the Apostle', 'prec':7},
    10704: { 'name': 'Independence Day', 'prec':3},
    10706: { 'name': 'Thomas More and John Fisher', 'martyr':1, 'prec':3},
    10711: { 'name': 'Benedict of Nursia', 'prec':4},
    10714: { 'name': 'John Keble', 'prec':4},
    10715: { 'name': 'Swithun', 'prec':4},
    10716: { 'name': 'Osmund', 'prec':3},
    10717: { 'name': 'William White', 'prec':3},
    10718: { 'name': 'Elizabeth Ferard', 'prec':3},
    10719: { 'name': 'Gregory, and his sister Macrina', 'prec':4},
    10720: { 'name': 'Margaret of Antioch', 'martyr':1, 'prec':3},
    10722: { 'name': 'Mary Magdalene', 'prec':7},
    10723: { 'name': 'Bridget of Sweden', 'prec':3},
    10724: { 'name': 'Thomas a Kempis', 'prec':3},
    10725: { 'name': 'James the Apostle', 'prec':7},
    10726: { 'name': 'Parents of the Blessed Virgin Mary', 'prec':4},
    10727: { 'name': 'Brooke Foss Westcott', 'prec':3},
    10729: { 'name': 'Mary, Martha and Lazarus', 'prec':4},
    10730: { 'name': 'William Wilberforce', 'prec':3},
    10731: { 'name': 'Ignatius of Loyola', 'prec':3},

    10804: { 'name': 'Jean-Baptiste Vianney', 'prec':3},
    10805: { 'name': 'Oswald', 'martyr':1, 'prec':4},
    10806: { 'name': 'The Transfiguration of Our Lord', 'prec':7},
    10807: { 'name': 'John Mason Neale', 'prec':3},
    10808: { 'name': 'Dominic', 'prec':4},
    10809: { 'name': 'Mary Sumner', 'prec':4},
    10810: { 'name': 'Lawrence', 'martyr':1, 'prec':4},
    10811: { 'name': 'Clare', 'prec':4},
    10813: { 'name': 'Jeremy Taylor', 'prec':4},
    10814: { 'name': 'Maximilian Kolbe', 'martyr':1, 'prec':3},
    10815: { 'name': 'The Blessed Virgin Mary', 'prec':7},
    10818: { 'name': 'William Porcher DuBose', 'prec':3},
    10820: { 'name': 'Bernard', 'prec':4},
    10824: { 'name': 'Bartholomew the Apostle', 'prec':7},
    10825: { 'name': 'Louis', 'prec':3},
    10827: { 'name': 'Monica', 'prec':4},
    10828: { 'name': 'Augustine of Hippo', 'prec':4},
    10829: { 'name': 'The Beheading of John the Baptist', 'prec':4},
    10830: { 'name': 'John Bunyan', 'prec':4},
    10831: { 'name': 'Aidan', 'prec':4},

    10901: { 'name': 'Giles of Provence', 'prec':3},
    10902: { 'name': 'Martyrs of New Guinea', 'martyr':1, 'prec':3},
    10903: { 'name': 'Gregory the Great', 'prec':4},
    10904: { 'name': 'Birinus', 'prec':3},
    10906: { 'name': 'Allen Gardiner', 'prec':3},
    10908: { 'name': 'The Birth of the Blessed Virgin Mary', 'prec':4},
    10909: { 'name': 'Charles Fuge Lowder', 'prec':3},
    10912: { 'name': 'John Henry Hobart', 'prec':3},
    10913: { 'name': 'John Chrysostom', 'prec':4},
    10914: { 'name': 'Holy Cross Day', 'prec':7},
    10915: { 'name': 'Cyprian, Bishop of Carthage', 'martyr':1, 'prec':4},
    10916: { 'name': 'Ninian', 'prec':4},
    10917: { 'name': 'Hildegard', 'prec':4},
    10918: { 'name': 'Edward Bouverie Pusey', 'prec':3},
    10919: { 'name': 'Theodore of Tarsus', 'prec':3},
    10920: { 'name': 'John Coleridge Patteson and companions', 'martyr':1, 'prec':4},
    10921: { 'name': 'Matthew', 'martyr':1, 'prec':7},
    10925: { 'name': 'Lancelot Andrewes', 'prec':4},
    10926: { 'name': 'Wilson Carlile', 'prec':3},
    10927: { 'name': 'Vincent de Paul', 'prec':4},
    10929: { 'name': 'Michael and All Angels', 'prec':7},
    10930: { 'name': 'Jerome', 'prec':3},

    11001: { 'name': 'Remigius', 'prec':3},
    11003: { 'name': 'George Bell', 'prec':3},
    11004: { 'name': 'Francis of Assisi', 'prec':3},
    11006: { 'name': 'William Tyndale', 'prec':4},
    11009: { 'name': 'Robert Grosseteste', 'prec':3},
    11010: { 'name': 'Paulinus', 'prec':4},
    11011: { 'name': 'Ethelburga', 'prec':3},
    11012: { 'name': 'Wilfrid of Ripon', 'prec':4},
    11013: { 'name': 'Edward the Confessor', 'prec':4},
    11015: { 'name': 'Teresa of Avila', 'prec':4},
    11016: { 'name': 'Hugh Latimer, Nicholas Ridley, Thomas Cranmer', 'martyr':1, 'prec':3},
    11017: { 'name': 'Ignatius', 'martyr':1, 'prec':4},
    11018: { 'name': 'Luke the Evangelist', 'prec':7},
    11019: { 'name': 'Henry Martyn', 'prec':4},
    11023: { 'name': 'James of Jerusalem', 'martyr':1, 'prec':4},
    11025: { 'name': 'Crispin and Crispinian', 'prec':3},
    11026: { 'name': 'Alfred the Great', 'prec':4},
    11028: { 'name': 'Simon and Jude, Apostles', 'prec':7},
    11029: { 'name': 'James Hannington and his companions', 'martyr':1, 'prec':4},
    11031: { 'name': 'Martin Luther', 'prec':3},

    11101: { 'name': 'All Saints', 'prec':9},
    11102: { 'name': 'All Souls Day', 'prec':4},
    11103: { 'name': 'Richard Hooker', 'prec':4},
    11106: { 'name': 'Leonard', 'prec':3},
    11107: { 'name': 'Willibrord', 'prec':4},
    11108: { 'name': 'The Saints and Martyrs of England', 'prec':4},
    11109: { 'name': 'Margery Kempe', 'prec':3},
    11110: { 'name': 'Leo the Great', 'prec':4},
    11111: { 'name': 'Martin of Tours', 'prec':4},
    11112: { 'name': 'Charles Simeon', 'prec':3},
    11113: { 'name': 'Charles Simeon', 'prec':4},
    11114: { 'name': 'Samuel Seabury', 'prec':3},
    11116: { 'name': 'Margaret', 'prec':4},
    11117: { 'name': 'Hugh', 'prec':4},
    11118: { 'name': 'Elizabeth of Hungary', 'prec':4},
    11119: { 'name': 'Hilda, Abbess of Whitby', 'prec':4},
    11120: { 'name': 'Edmund', 'martyr':1, 'prec':4},
    11122: { 'name': 'Cecilia', 'prec':3},
    11123: { 'name': 'Clement of Rome', 'prec':4},
    11125: { 'name': 'Catherine of Alexandria', 'martyr':1, 'prec':3},
    11130: { 'name': 'Andrew the Apostle', 'prec':7},

    11201: { 'name': 'Charles de Foucauld', 'prec':3},
    11202: { 'name': 'Channing Moore Williams', 'prec':3},
    11203: { 'name': 'Francis Xavier', 'prec':3},
    11204: { 'name': 'John of Damascus', 'prec':3},
    11205: { 'name': 'Clement of Alexandria', 'prec':3},
    11206: { 'name': 'Nicholas', 'prec':4},
    11207: { 'name': 'Ambrose', 'prec':4},
    11208: { 'name': 'The Conception of the Blessed Virgin Mary', 'prec':7},
    11213: { 'name': 'Lucy', 'prec':4},
    11214: { 'name': 'John of the Cross', 'prec':4},
    11217: { 'name': 'Eglantine Jebb', 'prec':3},
    11221: { 'name': 'Thomas', 'prec':4},
    11224: { 'name': 'Christmas Eve', 'prec':4},
    11225: { 'name': 'Christmas', 'prec':9},
    11226: { 'name': 'Stephen', 'martyr':1, 'prec':7},
    11227: { 'name': 'John the Apostle', 'prec':7},
    11228: { 'name': 'Holy Innocents', 'martyr':1, 'prec':7},
    11229: { 'name': 'Thomas Becket', 'martyr':1, 'prec':4},
    11231: { 'name': 'John Wyclif', 'prec':3},
}

# This returns the date easter occurs on for a given year as (month,day).
def Date_Easter(year):      
    easter_date = easter(year)
    easter_month = easter_date.month
    easter_day = easter_date.day
    return(easter_month, easter_day)


def advent_sunday(year):
    return -(Day_of_Week(y,12,25) + 4*7)

def Date_to_Days(year, month, day):

    # Define a start date as passed in
    f_date = date(year, month, day)

    # Define an end date as 1st of January of the year 1 A.D.
    # This is defined in Perl Date::Calm
    l_date = date(1, 1, 1)

    # Calculate the difference between the end date and start date
    delta = l_date - f_date

    # Print the number of days in the time difference
    return(delta.days)

def Day_of_Week(year, month, day):

    # Define a start date as passed in
    f_date = date(year, month, day)

    # Return ISO week day, in range 1-7
    return(f_date.isoweekday)

##########################################################################

def new():
#  my ($class, %opts) = @_;

    # get today's date
    today = today()
    y = today.year
    m = today.month
    d = today.day

    #die "Need to specify year, month and day" unless $y and $m and $d;

    days = Date_to_Days(y, m, d)
    easter = Date_to_Days(y, Date_Easter(y))

    possibles = []

  # "The Church Year consists of two cycles of feasts and holy days: one is
  #  dependent upon the movable date of the Sunday of the Resurrection or
  #  Easter Day; the other, upon the fixed date of December 25, the Feast
  #  of our Lord's Nativity or Christmas Day."

    easter_point = days-easter
    christmas_point = 0

    # We will store the amount of time until (-ve) or since (+ve) Christmas in
    # $christmas_point. Let's make the cut-off date the end of February,
    # since we'll be dealing with Easter-based dates after that, and it
    # avoids the problems of considering leap years.

    if m>2:
        christmas_point = days - Date_to_Days(y, 12, 25)
    else:
        christmas_point = days - Date_to_Days(y-1, 12, 25)

    # First, figure out the season.
    season = ''
    weekno = None

    advent_sunday = advent_sunday(y)

    if easter_point > -47 and easter_point < 0:
        season = 'Lent'
        weekno = (easter_point+50) // 7;
        # FIXME: The ECUSA calendar seems to indicate that Easter Eve ends
        # Lent *and* begins the Easter season. I'm not sure how. Maybe it's
        # in both? Maybe the daytime is in Lent and the night is in Easter?
    elif easter_point >= 0 and easter_point <= 49:
        # yes, this is correct: Pentecost itself is in Easter season;
        # Pentecost season actually begins on the day after Pentecost.
        # Its proper name is "The Season After Pentecost".
        season = 'Easter';
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

    # Now, look for feasts.
    feast_from_Easter    = feasts[easter_point]
    feast_from_Christmas = feasts[10000+100*m+d]

    if feast_from_Easter:
        possibles.append(feast_from_Easter)

    if feast_from_Christmas:
        possibles.append(feast_from_Christmas)

    # Maybe transferred from yesterday.
    unless (opts['transferred']) { # don't go round infinitely
        my ($yestery, $yesterm, $yesterd) = Add_Delta_Days(1, 1, 1, $days-2);
        my $transferred = $class->new(
            %opts,
            year = $yestery,
            month = $yesterm,
            day = $yesterd,
            transferred=1,
        );

        if ($transferred) {
            $transferred->{name} .= ' (transferred)';
            push @possibles, $transferred;
        }
    }

    # Maybe a Sunday.
    if Day_of_Week(y, m, d) == 7:
        possibles.append({ 'prec': 5, name: f"{season} {weekno}" })

    # So, which event takes priority?

    possibles = sorted(possibles.items(), key = lambda tup: (tup[1]['prec']))

    if opts['transferred']:
        # If two feasts coincided today, we were asked to find
        # the one which got transferred.
        # But Sundays don't get transferred!
        if possibles[1] and possibles[1]['prec'] == 5:
            return None
        else:
            return possibles[1]
    
    # Get first item
    result = list(possibles.keys())[0]

    if result is None:
        result = { 'name': '', 'prec': 1 }
    result = { opts, result, season=season, weekno=weekno }

    rose_days = { 'Advent 2': 1, 'Lent 3': 1 }
    if result['name'] in rose_days.keys():
        result['colour'] = 'rose'

    if result['colour'] is None:
        if result['prec'] > 2 and result['prec'] != 5:
            # feasts are generally white, unless marked differently.
            # But martyrs are red
            if result['martyr']:
                result['colour'] = 'red'
            else:
                result['colour'] = 'white'
        else:
            # Not a feast day.
            if season is 'Lent':
                result['colour'] = 'purple'
            elif season is 'Advent':
                result['colour'] = 'purple'
            else:
                # The great fallback:
                result['colour'] = 'green'

    # Two special cases for Christmas-based festivals which
    # depend on the day of the week.
    if result['prec'] == 5: # An ordinary Sunday
        if christmas_point == advent_sunday:
            result['name'] = 'Advent Sunday';
            result['colour'] = 'white';
        elif: christmas_point == advent_sunday-7:
            result['name'] = 'Christ the King';
            result['colour'] = 'white';

    return (result, class)
 
    sub year   { my ($self)=@_; return $self->{year};   }
    sub month  { my ($self)=@_; return $self->{month};  }
    sub day    { my ($self)=@_; return $self->{day};    }
    sub colour { my ($self)=@_; return $self->{colour}; }
    sub color  { goto &colour; }
    sub season { my ($self)=@_; return $self->{season}; }
    sub name   { my ($self)=@_; return $self->{name};   }


def utc_rd_values(self) {
    return (
        Date_to_Days(self['year'], self['month'], self['day'])-1,
        0,
        0,
    )
}

sub from_object {
    my ($class, $object)=@_;
    my ($days, $secs, $nanosecs) = $object->utc_rd_values();

    my ($y, $m, $d, $hour, $min, $seconds) =
        Add_Delta_DHMS(1, 1, 1, 0, 0, 0, $days-1, 0, 0, $secs);

    return $class->new(
        day = $d,
        month = $m,
        year = $y,
        hour = $hour,
        minute = $min,
        seconds = $seconds,
        nanosecond = $nanosecs,
    );
}

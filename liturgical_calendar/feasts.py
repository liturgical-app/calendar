"""
This is a massive function which effectively contains all of the data from this Wikipedia page:
https://en.wikipedia.org/wiki/Calendar_of_saints_(Church_of_England)
"""
def lookup_feast(relative_to, pointer):
    """
    The feasts dict contains structured data and there is a trivial function
    at the end to return feasts by day
    """
    feasts = {

        # Anglican Holy Days are variously categorised as Principal Feasts,
        # Principal Holy Days, Festivals, Lesser Festivals, or Commemorations
        # The observance of Lesser Festivals or Commemorations is optional.
        # Principal Feasts    = prec 9
        # Principal Holy Days = prec 9
        # Festivals           = prec 7
        # Sundays             = prec 5
        # Lesser Festivals    = prec 4
        # Commemorations      = prec 3

        # These Festivals need implementing
        # 7 Dedication Festival, the first Sunday in October or the Last Sunday after Trinity, if date unknown
        'easter': {
            # Dates relative to Easter are encoded as the number of days after Easter.
            -47: { 'name': 'Shrove Tuesday', 'colour':'white', 'url': 'https://en.wikipedia.org/wiki/Shrove_Tuesday', 'prec':7 },
            -46: { 'name': 'Ash Wednesday', 'colour':'purple', 'url': 'https://en.wikipedia.org/wiki/Ash_Wednesday', 'prec':9, 'type': 'Principal Holy Day', 'readings': ['Joel 2:1-2,12-17 or Isaiah 58:1-12', 'Psalm 51:1-18', '2 Corinthians 5:20b-6:10', 'Matthew 6:1-6, 16-21 or John 8:1-11'] },
            -7: { 'name': 'Palm Sunday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Palm_Sunday', 'prec':5, 'readings': ['Isaiah 50:4-9a', 'Philippians 2:5-11', 'Matthew 26:14-27:66 or Matthew 27:11-54 ', 'Psalm 31:9-16'] },
            -6: { 'name': 'Holy Monday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Holy_Monday', 'prec':9, 'type': 'Principal Holy Day', 'readings': ['Isaiah 42:1-9', 'Hebrews 9:11-15', 'John 12:1-11', 'Psalm 36:5-11'] },
            -5: { 'name': 'Holy Tuesday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Holy_Tuesday', 'prec':9, 'type': 'Principal Holy Day', 'readings': ['Isaiah 49:1-7', '1 Corinthians 1:18-31', 'John 12:20-36', 'Psalm 71:1-14'] },
            -4: { 'name': 'Holy Wednesday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Holy_Wednesday', 'prec':9, 'type': 'Principal Holy Day', 'readings': ['Isaiah 50:4-9a', 'Hebrews 12:1-3', 'John 13:21-32', 'Psalm 70'] },
            -3: { 'name': 'Maundy Thursday', 'colour':'white', 'url': 'https://en.wikipedia.org/wiki/Maundy_Thursday', 'prec':9, 'type': 'Principal Holy Day', 'readings': ['Exodus 12:1-14', '1 Corinthians 11:23-26', 'John 13:1-17,31b-35', 'Psalm 116:1,10-17'] },
            -2: { 'name': 'Good Friday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Good_Friday', 'prec':9, 'type': 'Principal Holy Day', 'readings': ['Isaiah 52:13-53:12', 'Hebrews 10:16-25', 'John 18:1-19:42', 'Psalm 22'] },
            -1: { 'name': 'Holy Saturday', 'colour':'not given', 'url': 'https://en.wikipedia.org/wiki/Holy_Saturday', 'prec':9, 'type': 'Principal Holy Day', 'readings': ['Job 14:1-14', '1 Peter 4:1-8', 'Matthew 27:57-66', 'Psalm 31:1-4,15-16'] },
            0 : { 'name': 'Easter', 'url': 'https://en.wikipedia.org/wiki/Easter', 'prec':9, 'type': 'Principal Feast'},
            # Easter Sunday’s readings are in Sundays
            39: { 'name': 'Ascension', 'url': 'https://en.wikipedia.org/wiki/Ascension_Day', 'prec':9, 'type': 'Principal Feast', 'readings': ['Acts 1:1-11', 'Ephesians 1:15-23', 'Luke 24:44-53', 'Psalm 47 or Psalm 93'] },
            49: { 'name': 'Pentecost', 'colour': 'red', 'url': 'https://en.wikipedia.org/wiki/Pentecost', 'prec':9, 'type': 'Principal Feast' },
            # Pentecost (Whit Sunday)’s readings are in Sundays
            56: { 'name': 'Trinity', 'url': 'https://en.wikipedia.org/wiki/Trinity_Sunday', 'prec':9, 'type': 'Principal Feast' },
            # Trinity Sunday’s readings are in Sundays
            60: { 'name': 'Corpus Christi', 'url':'https://en.wikipedia.org/wiki/Corpus_Christi_(feast)', 'prec':7, 'readings': ['Genesis 14:18-20', '1 Corinthians 11:23-26', 'John 6:51-58', 'Psalm 116:10-17'] },
        },
        'christmas': {
            '01-01': { 'name': 'The Naming and Circumcision of Jesus', 'url': 'https://en.wikipedia.org/wiki/Circumcision_of_Christ', 'prec':7, 'readings': ['Numbers 6:22-27', 'Galatians 4:4-7', 'Luke 2:15-21', 'Psalm 8'] },
            '01-02': { 'name': 'Basil the Great and Gregory of Nazianzus', 'url': 'https://en.wikipedia.org/wiki/Basil_of_Caesarea', 'prec':4, 'readings': ['2 Timothy 4:1-8', 'Matthew 5.13-19'] },
            '01-06': { 'name': 'Epiphany', 'url': 'https://en.wikipedia.org/wiki/Epiphany_(Christian)', 'prec':9, 'type': 'Principal Feast', 'readings': ['Isaiah 60:1-6', 'Ephesians 3:1-12', 'Matthew 2:1-12', 'Psalm 72:1-9,10-15'] },
            # Figure out where "The First Sunday of Epiphany" goes because that’s actually when the next line is celebrated…
            # '01-07': { 'name': 'The Baptism of Christ', 'url': 'https://en.wikipedia.org/wiki/Baptism_of_the_Lord', 'prec':7},
            '01-10': { 'name': 'William Laud', 'url': 'https://en.wikipedia.org/wiki/William_Laud', 'prec':3},
            '01-11': { 'name': 'Mary Slessor', 'url': 'https://en.wikipedia.org/wiki/Mary_Slessor', 'prec':3},
            '01-12': { 'name': 'Aelred of Hexham', 'url': 'https://en.wikipedia.org/wiki/Ailred_of_Rievaulx', 'prec':4, 'readings': ['Ecclesiasticus 15:1-6'] },
            '01-13': { 'name': 'Hilary', 'url': 'https://en.wikipedia.org/wiki/Hilary_of_Poitiers', 'prec':4, 'readings': ['1 John 2:18-25', 'John 8:25-32'] },
            '01-17': { 'name': 'Antony of Egypt', 'url': 'https://en.wikipedia.org/wiki/Anthony_the_Great', 'prec':4, 'readings': ['Philippians 3:7-14', 'Matthew 19:16-26'] },
            '01-18': { 'name': 'Amy Carmichael', 'url': 'https://en.wikipedia.org/wiki/Amy_Carmichael', 'prec':3},
            '01-19': { 'name': 'Wulfstan', 'url': 'https://en.wikipedia.org/wiki/Wulfstan,_Bishop_of_Worcester', 'prec':4, 'readings': ['Matthew 24:42-46'] },
            '01-20': { 'name': 'Richard Rolle', 'url': 'https://en.wikipedia.org/wiki/Richard_Rolle', 'prec':3},
            '01-21': { 'name': 'Agnes', 'url': 'https://en.wikipedia.org/wiki/Saint_Agnes', 'prec':4, 'readings': ['Revelation 7:13-end'] },
            '01-22': { 'name': 'Vincent of Saragossa', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Vincent_of_Saragossa', 'prec':3},
            '01-24': { 'name': 'Francis de Sales', 'url': 'https://en.wikipedia.org/wiki/Francis_de_Sales', 'prec':4, 'readings': ['Proverbs 3:13-18', 'John 3:17-21'] },
            '01-25': { 'name': 'The Conversion of Paul', 'url': 'https://en.wikipedia.org/wiki/Conversion_of_Paul', 'prec':7, 'readings': ['Acts 9:1-22', 'Galatians 1:11-16', 'Matthew 19:27-30', 'Psalm 67'] },
            '01-26': { 'name': 'Timothy and Titus', 'url': 'https://en.wikipedia.org/wiki/Saint_Timothy', 'prec':4, 'readings': ['Isaiah 61:1-3a', 'Psalm 100', '2 Timothy 2:1-8 or Titus 1:1-5', 'Luke 10:1-9'] },
            '01-28': { 'name': 'Thomas Aquinas', 'url': 'https://en.wikipedia.org/wiki/Thomas_Aquinas', 'prec':4, 'readings': ['Wisdom 7:7-10,15,16', '1 Corinthians 2:9-end', 'John 16:12-15'] },
            '01-30': { 'name': 'Charles, king and martyr', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Charles,_King_and_Martyr', 'prec':4, 'readings': ['Ecclesiasticus 2:12-end', '1 Timothy 6:12-16'] },
            '01-31': { 'name': 'John Bosco', 'url': 'https://en.wikipedia.org/wiki/John_Bosco', 'prec':3},

            '02-01': { 'name': 'Brigid of Kildare', 'url': 'https://en.wikipedia.org/wiki/Brigid_of_Kildare', 'prec':3},
            '02-02': { 'name': 'Presentation of Christ at the Temple', 'url': 'https://en.wikipedia.org/wiki/Presentation_of_Jesus_at_the_Temple', 'prec':9, 'type': 'Principal Feast', 'readings': ['Malachi 3:1-5', 'Hebrews 2:14-18', 'Luke 2:22-40', 'Psalm 24'] },
            '02-03': { 'name': 'Anskar', 'url': 'https://en.wikipedia.org/wiki/Ansgar', 'prec':4, 'readings': ['Isaiah 52:7-10','Romans 10:11-15'] },
            '02-04': { 'name': 'Gilbert of Sempringham', 'url': 'https://en.wikipedia.org/wiki/Gilbert_of_Sempringham', 'prec':3},
            '02-06': { 'name': 'Martyrs of Japan', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/26_Martyrs_of_Japan', 'prec':3},
            '02-10': { 'name': 'Scholastica', 'url': 'https://en.wikipedia.org/wiki/Scholastica', 'prec':3},
            '02-14': { 'name': 'Valentine', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Valentine', 'prec':3},
            '02-14': { 'name': 'Cyril and Methodius', 'url': 'https://en.wikipedia.org/wiki/Cyril_and_Methodius', 'prec':4, 'readings': ['Isaiah 52:7-10', 'Romans 10:11-15'] },
            '02-15': { 'name': 'Thomas Bray', 'url': 'https://en.wikipedia.org/wiki/Thomas_Bray', 'prec':3},
            '02-17': { 'name': 'Janani Luwum', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Janani_Luwum', 'prec':4, 'readings': ['Ecclesiasticus 4:20-28', 'John 12:24-32'] },
            '02-23': { 'name': 'Polycarp', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Polycarp', 'prec':4, 'readings': ['Revelation 2:8-11'] },
            '02-27': { 'name': 'George Herbert', 'url': 'https://en.wikipedia.org/wiki/George_Herbert', 'prec':4, 'readings': ['Malachi 2:5-7', 'Matthew 11:25-end', 'Revelation 19:5-9'] },

            '03-01': { 'name': 'David', 'url': 'https://en.wikipedia.org/wiki/Saint_David', 'prec':4, 'readings': ['2 Samuel 23:1-4', 'Psalm 89:19-24'] },
            '03-02': { 'name': 'Chad', 'url': 'https://en.wikipedia.org/wiki/Chad_of_Mercia', 'prec':4, 'readings': ['1 Timothy 6:11b-16'] },
            '03-07': { 'name': 'Perpetua, Felicity and companions', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Perpetua_and_Felicitas', 'prec':4, 'readings': ['Revelation 12:10-12a', 'Wisdom 3:1-7'] },
            '03-08': { 'name': 'Edward King', 'url': 'https://en.wikipedia.org/wiki/Edward_King_(English_bishop)', 'prec':4, 'readings': ['Hebrews 13:1-8'] },
            '03-17': { 'name': 'Patrick', 'url': 'https://en.wikipedia.org/wiki/Saint_Patrick%27s_Day', 'prec':4, 'readings': ['Psalm 91:1-4,13-16', 'Luke 10:1-12,17-20'] },
            '03-18': { 'name': 'Cyril', 'url': 'https://en.wikipedia.org/wiki/Cyril_of_Jerusalem', 'prec':3},
            '03-19': { 'name': 'Joseph of Nazareth', 'url': 'https://en.wikipedia.org/wiki/Saint_Joseph', 'prec':7, 'readings': ['2 Samuel 7:4,8-16', 'Romans 4:13-18', 'Matthew 1:18-25', 'Psalm 89:1-4,19-26'] },
            '03-20': { 'name': 'Cuthbert', 'url': 'https://en.wikipedia.org/wiki/Cuthbert_of_Lindisfarne', 'prec':4, 'readings': ['Ezekiel 34:11-16', 'Matthew 18:12-14'] },
            '03-21': { 'name': 'Thomas Cranmer', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Thomas_Cranmer', 'prec':4, 'readings': ['2 Timothy 2:8-15', 'Matthew 10:16-22'] },
            '03-24': { 'name': 'Walter Hilton of Thurgarton', 'url': 'https://en.wikipedia.org/wiki/Walter_Hilton', 'prec':3},
            '03-25': { 'name': 'The Annunciation of our Lord', 'url': 'https://en.wikipedia.org/wiki/Annunciation', 'prec':9, 'type': 'Principal Feast', 'readings': ['Isaiah 7:10-14', 'Hebrews 10:4-10', 'Luke 1:26-38', 'Psalm 40:5-11'] },
            '03-26': { 'name': 'Harriet Monsell', 'url': 'https://en.wikipedia.org/wiki/Harriet_Monsell', 'prec':3},
            '03-31': { 'name': 'John Donne', 'url': 'https://en.wikipedia.org/wiki/John_Donne', 'prec':3},

            '04-01': { 'name': 'Frederick Denison Maurice', 'url': 'https://en.wikipedia.org/wiki/Frederick_Denison_Maurice', 'prec':3},
            '04-09': { 'name': 'Dietrich Bonhoeffer', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Dietrich_Bonhoeffer', 'prec':3},
            '04-10': { 'name': 'William Law', 'url': 'https://en.wikipedia.org/wiki/William_Law', 'prec':4, 'readings': ['1 Corinthians 2:9-end', 'Matthew 17:1-9'] },
            '04-11': { 'name': 'George Selwyn', 'url': 'https://en.wikipedia.org/wiki/George_Selwyn_(Bishop_of_Lichfield)', 'prec':3},
            '04-16': { 'name': 'Isabella Gilmore', 'url': 'https://en.wikipedia.org/wiki/Isabella_Gilmore', 'prec':3},
            '04-19': { 'name': 'Alphege', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Alphege', 'prec':4, 'readings': ['Hebrews 5:1-4'] },
            '04-21': { 'name': 'Anselm', 'url': 'https://en.wikipedia.org/wiki/Anselm_of_Canterbury', 'prec':4, 'readings': ['Wisdom 9:13-end','Romans 5:8-11'] },
            '04-23': { 'name': 'George', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_George', 'prec':7, 'readings': ['Revelation 12:7-12', 'John 15:18-21', '2 Timothy 2:3-13 ', 'Psalm 126'] },
            '04-24': { 'name': 'Mellitus', 'url': 'https://en.wikipedia.org/wiki/Mellitus', 'prec':3},
            '04-25': { 'name': 'Mark the Evangelist', 'url': 'https://en.wikipedia.org/wiki/Mark_the_Evangelist', 'prec':7, 'readings': ['Acts 15:35-41', 'Psalm 119:9-16 ', 'Ephesians 4:7-16', 'Mark 13:5-13'] },
            '04-27': { 'name': 'Christina Rossetti', 'url': 'https://en.wikipedia.org/wiki/Christina_Rossetti', 'prec':3},
            '04-28': { 'name': 'Peter Chanel', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Peter_Chanel', 'prec':3},
            '04-29': { 'name': 'Catherine of Siena', 'url': 'https://en.wikipedia.org/wiki/Catherine_of_Siena', 'prec':4, 'readings': ['Proverbs 8:1,6-11', 'John 17:12-end'] },
            '04-30': { 'name': 'Pandita Mary Ramabai', 'url': 'https://en.wikipedia.org/wiki/Pandita_Ramabai', 'prec':3},

            '05-01': { 'name': 'Philip and James, Apostles', 'url': 'https://en.wikipedia.org/wiki/Philip_the_Apostle', 'prec':7, 'readings': ['Isaiah 30:15-21', 'Psalm 119:1-8', 'Ephesians 1:3-10', 'John 14:1-14'] },
            '05-02': { 'name': 'Athanasius', 'url': 'https://en.wikipedia.org/wiki/Athanasius_of_Alexandria', 'prec':4, 'readings': ['Ecclesiasticus 4:20-28', 'Matthew 10:24-27'] },
            '05-04': { 'name': 'English Saints and Martyrs of the Reformation Era', 'prec':4},
            '05-08': { 'name': 'Julian of Norwich', 'url': 'https://en.wikipedia.org/wiki/Julian_of_Norwich', 'prec':4, 'readings': ['1 Corinthians 13:8-end', 'Matthew 5:13-16'] },
            '05-12': { 'name': 'Gregory Dix', 'url': 'https://en.wikipedia.org/wiki/Gregory_Dix', 'prec':3},
            '05-14': { 'name': 'Matthias the Apostle', 'url': 'https://en.wikipedia.org/wiki/Saint_Matthias', 'prec':7, 'readings': ['Acts 1:15-26', 'Psalm 15', 'Acts 1:15-26', 'John 15:9-17'] },
            '05-16': { 'name': 'Caroline Chisholm', 'url': 'https://en.wikipedia.org/wiki/Caroline_Chisholm', 'prec':3},
            '05-19': { 'name': 'Dunstan', 'url': 'https://en.wikipedia.org/wiki/Dunstan', 'prec':4, 'readings': ['Matthew 24:42-46', 'Exodus 31:1-5'] },
            '05-20': { 'name': 'Alcuin', 'url': 'https://en.wikipedia.org/wiki/Alcuin', 'prec':4, 'readings': ['Colossians 3:12-16', 'John 4.19-24'] },
            '05-21': { 'name': 'Helena', 'url': 'https://en.wikipedia.org/wiki/Helena_of_Constantinople', 'prec':3},
            '05-24': { 'name': 'John and Charles Wesley', 'url': 'https://en.wikipedia.org/wiki/John_Wesley', 'prec':4, 'readings': ['Ephesians 5:15-20'] },
            '05-25': { 'name': 'The Venerable Bede', 'url': 'https://en.wikipedia.org/wiki/Bede', 'prec':4, 'readings': ['Ecclesiasticus 39:1-10'] },
            '05-26': { 'name': 'Augustine of Canterbury', 'url': 'https://en.wikipedia.org/wiki/Augustine_of_Canterbury', 'prec':4, 'readings': ['1 Thessalonians 2:2-8', 'Matthew 13:31-33'] },
            '05-28': { 'name': 'Lanfranc', 'url': 'https://en.wikipedia.org/wiki/Lanfranc', 'prec':3},
            '05-30': { 'name': 'Josephine Butler', 'url': 'https://en.wikipedia.org/wiki/Josephine_Butler', 'prec':4, 'readings': ['Isaiah 58:6-11', '1 John 3:18-23', 'Matthew 9:10-13'] },
            '05-31': { 'name': 'The Visit of the Blessed Virgin Mary to Elizabeth', 'prec':7, 'readings': ['Zephaniah 3:14-18 ', 'Romans 12:9-16b', 'Luke 1:39-57', 'Psalm 113'] },

            '06-01': { 'name': 'Justin', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Justin_Martyr', 'prec':4, 'readings': ['John 15:18-21', '1 Maccabees 2:15-22', '1 Corinthians 1:18-25'] },
            '06-03': { 'name': 'Martyrs of Uganda', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Martyrs_of_Uganda', 'prec':3},
            '06-04': { 'name': 'Petroc', 'url': 'https://en.wikipedia.org/wiki/Saint_Petroc', 'prec':3},
            '06-05': { 'name': 'Boniface', 'url': 'https://en.wikipedia.org/wiki/Saint_Boniface', 'prec':4, 'readings': ['Acts 20:24-28'] },
            '06-06': { 'name': 'Ini Kopuria', 'url': 'https://en.wikipedia.org/wiki/Ini_Kopuria', 'prec':3},
            '06-08': { 'name': 'Thomas Ken', 'url': 'https://en.wikipedia.org/wiki/Thomas_Ken', 'prec':4, 'readings': ['2 Corinthians 4:1-10', 'Matthew 24:42-46'] },
            '06-09': { 'name': 'Columba', 'url': 'https://en.wikipedia.org/wiki/Columba', 'prec':4, 'readings': ['Titus 2:11-end'] },
            '06-10': { 'name': 'Ephrem of Syria', 'url': 'https://en.wikipedia.org/wiki/Ephrem_the_Syrian', 'prec':3},
            '06-11': { 'name': 'Barnabas the Apostle', 'url': 'https://en.wikipedia.org/wiki/Barnabas', 'prec':7, 'readings': ['Acts 11:19-30', 'Psalm 112', 'Job 29:11-16', 'John 15:12-17'] },
            '06-14': { 'name': 'Richard Baxter', 'url': 'https://en.wikipedia.org/wiki/Richard_Baxter', 'prec':3},
            '06-15': { 'name': 'Evelyn Underhill', 'url': 'https://en.wikipedia.org/wiki/Evelyn_Underhill', 'prec':3},
            '06-16': { 'name': 'Richard of Chichester', 'url': 'https://en.wikipedia.org/wiki/Richard_of_Chichester', 'prec':4, 'readings': ['John 21:15-19'] },
            '06-17': { 'name': 'Samuel and Henrietta Barnett', 'url': 'https://en.wikipedia.org/wiki/Samuel_Augustus_Barnett', 'prec':3},
            '06-18': { 'name': 'Bernard Mizeki', 'url': 'https://en.wikipedia.org/wiki/Bernard_Mizeki', 'prec':3},
            '06-19': { 'name': 'Sundar Singh', 'url': 'https://en.wikipedia.org/wiki/Sadhu_Sundar_Singh', 'prec':3},
            '06-22': { 'name': 'Alban', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Alban', 'prec':4, 'readings': ['2 Timothy 2:3-13', 'John 12:24-26'] },
            '06-23': { 'name': 'Etheldreda', 'url': 'https://en.wikipedia.org/wiki/%C3%86thelthryth', 'prec':4, 'readings': ['Matthew 25:1-13'] },
            '06-24': { 'name': 'The Birth of John the Baptist', 'url': 'https://en.wikipedia.org/wiki/Nativity_of_St._John_the_Baptist', 'prec':7, 'readings': ['Isaiah 40:1-11', 'Acts 13:14b-26 or Galatians 3:23-29 ', 'Luke 1:57-80', 'Psalm 85:7-13'] },
            '06-27': { 'name': 'Cyril', 'url': 'https://en.wikipedia.org/wiki/Cyril_of_Alexandria', 'prec':3},
            '06-28': { 'name': 'Irenaeus', 'url': 'https://en.wikipedia.org/wiki/Irenaeus', 'prec':4, 'readings': ['2 Peter 1:16-end'] },
            '06-29': { 'name': 'Peter and Paul, Apostles', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Peter', 'prec':7, 'readings': ['Acts 12:1-11', 'Psalm 125', 'Zechariah 4:1-14 ', 'Matthew 16:13-19'] },

            '07-01': { 'name': 'Henry, John, and Henry Venn', 'url': 'https://en.wikipedia.org/wiki/Henry_Venn_(Clapham_Sect)', 'prec':3},
            '07-03': { 'name': 'Thomas the Apostle', 'url': 'https://en.wikipedia.org/wiki/Thomas_the_Apostle', 'prec':7, 'readings': ['Ephesians 2:19-22', 'Psalm 31:1-6', 'John 20:24-29', 'Habakkuk 2:1-4'] },
            '07-06': { 'name': 'Thomas More and John Fisher', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Thomas_More', 'prec':3},
            '07-11': { 'name': 'Benedict', 'url': 'https://en.wikipedia.org/wiki/Benedict_of_Nursia', 'prec':4, 'readings': ['1 Corinthians 3:10-11', 'Luke 18:18-22'] },
            '07-14': { 'name': 'John Keble', 'url': 'https://en.wikipedia.org/wiki/John_Keble', 'prec':4, 'readings': ['Lamentations 3:19-26', 'Matthew 5:1-8'] },
            '07-15': { 'name': 'Swithun', 'url': 'https://en.wikipedia.org/wiki/Swithun', 'prec':4, 'readings': ['James 5:7-11,13-18'] },
            '07-16': { 'name': 'Osmund', 'url': 'https://en.wikipedia.org/wiki/Saint_Osmund', 'prec':3},
            '07-18': { 'name': 'Elizabeth Ferard', 'url': 'https://en.wikipedia.org/wiki/Elizabeth_Ferard', 'prec':3},
            '07-19': { 'name': 'Gregory, and his sister Macrina', 'url': 'https://en.wikipedia.org/wiki/Gregory_of_Nyssa', 'prec':4, 'readings': ['1 Corinthians 2:9-13', 'Wisdom 9:13-17'] },
            '07-20': { 'name': 'Margaret of Antioch', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Margaret_the_Virgin', 'prec':3},
            '07-22': { 'name': 'Mary Magdalene', 'url': 'https://en.wikipedia.org/wiki/Mary_Magdalene', 'prec':7, 'readings': ['Song of Solomon 3:1-4', '2 Corinthians 5:14-17', 'John 20:1-2,11-18', 'Psalm 42'] },
            '07-23': { 'name': 'Bridget', 'url': 'https://en.wikipedia.org/wiki/Bridget_of_Sweden', 'prec':3},
            '07-25': { 'name': 'James the Apostle', 'url': 'https://en.wikipedia.org/wiki/James,_son_of_Zebedee', 'prec':7, 'readings': ['Acts 11:27-12:2', 'Psalm 126', 'Jeremiah 45:1-5', 'Matthew 20:20-28'] },
            '07-26': { 'name': 'Parents of the Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Saint_Anne', 'prec':4, 'readings': ['Zephaniah 3:14-18a', 'Psalm 127', 'Romans 8:28-30', 'Matthew 13:16-17'] },
            '07-27': { 'name': 'Brooke Foss Westcott', 'url': 'https://en.wikipedia.org/wiki/Brooke_Foss_Westcott', 'prec':3},
            '07-29': { 'name': 'Mary, Martha and Lazarus', 'url': 'https://en.wikipedia.org/wiki/Mary,_sister_of_Lazarus', 'prec':4, 'readings': ['Isaiah 25:6-9', 'Psalm 49:5-10,16', 'Hebrews 2:10-15', 'John 12:1-8'] },
            '07-30': { 'name': 'William Wilberforce', 'url': 'https://en.wikipedia.org/wiki/William_Wilberforce', 'prec':3, 'readings': ['Job 31:16-23', 'Galatians 3:26-end', 'Luke 4:16-21'] },
            '07-31': { 'name': 'Ignatius of Loyola', 'url': 'https://en.wikipedia.org/wiki/Ignatius_of_Loyola', 'prec':3},

            '08-04': { 'name': 'Jean-Baptiste Vianney', 'url': 'https://en.wikipedia.org/wiki/Jean_Vianney', 'prec':3},
            '08-05': { 'name': 'Oswald', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Oswald_of_Northumbria', 'prec':4, 'readings': ['1 Peter 4:12-end', 'John 16:29-end'] },
            '08-06': { 'name': 'The Transfiguration of Our Lord', 'url': 'https://en.wikipedia.org/wiki/Transfiguration_of_Jesus', 'prec':7, 'readings': ['Daniel 7:9,10,13,14 ', '2 Peter 1:16-19', 'Luke 9:28-36', 'Psalm 97'] },
            '08-07': { 'name': 'John Mason Neale', 'url': 'https://en.wikipedia.org/wiki/John_Mason_Neale', 'prec':3},
            '08-08': { 'name': 'Dominic', 'url': 'https://en.wikipedia.org/wiki/Saint_Dominic', 'prec':4, 'readings': ['Ecclesiasticus 39:1-10'] },
            '08-09': { 'name': 'Mary Sumner', 'url': 'https://en.wikipedia.org/wiki/Mary_Sumner', 'prec':4, 'readings': ['Hebrews 13:1-5'] },
            '08-10': { 'name': 'Laurence', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Lawrence_of_Rome', 'prec':4, 'readings': ['2 Corinthians 9:6-10'] },
            '08-11': { 'name': 'Clare', 'url': 'https://en.wikipedia.org/wiki/Clare_of_Assisi', 'prec':4, 'readings': ['Song of Solomon 8:6-7'] },
            '08-13': { 'name': 'Jeremy Taylor', 'url': 'https://en.wikipedia.org/wiki/Jeremy_Taylor', 'prec':4, 'readings': ['Titus 2:7,8,11-14'] },
            '08-14': { 'name': 'Maximilian Kolbe', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Maximilian_Kolbe', 'prec':3},
            '08-15': { 'name': 'The Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Blessed_Virgin_Mary', 'prec':7, 'readings': ['Isaiah 61:10-11', 'Galatians 4:4-7', 'Luke 1:46-55', 'Psalm 45:10-17 '] },
            '08-20': { 'name': 'Bernard', 'url': 'https://en.wikipedia.org/wiki/Bernard_of_Clairvaux', 'prec':4, 'readings': ['Revelation 19:5-9'] },
            '08-24': { 'name': 'Bartholomew the Apostle', 'url': 'https://en.wikipedia.org/wiki/Bartholomew_the_Apostle', 'prec':7, 'readings': ['Acts 5:12-16', 'Psalm 145:1-7', 'Isaiah 43:8-13', 'Luke 22:24-30'] },
            '08-27': { 'name': 'Monica', 'url': 'https://en.wikipedia.org/wiki/Monica_of_Hippo', 'prec':4, 'readings': ['Ecclesiasticus 26:1-3,13-16'] },
            '08-28': { 'name': 'Augustine', 'url': 'https://en.wikipedia.org/wiki/Augustine_of_Hippo', 'prec':4, 'readings': ['Ecclesiasticus 39:1-10', 'Romans 13:11-13'] },
            '08-29': { 'name': 'The Beheading of John the Baptist', 'url': 'https://en.wikipedia.org/wiki/John_the_Baptist', 'prec':4, 'readings': ['Jeremiah 1:4-10', 'Psalm 11', 'Hebrews 11:32–12:2', 'Matthew 14:1-12'] },
            '08-30': { 'name': 'John Bunyan', 'url': 'https://en.wikipedia.org/wiki/John_Bunyan', 'prec':4, 'readings': ['Hebrews 12:1-2', 'Luke 21:21,34-36'] },
            '08-31': { 'name': 'Aidan', 'url': 'https://en.wikipedia.org/wiki/Aidan_of_Lindisfarne', 'prec':4, 'readings': ['1 Corinthians 9:16-19'] },

            '09-01': { 'name': 'Giles of Provence', 'url': 'https://en.wikipedia.org/wiki/Saint_Giles', 'prec':3},
            '09-02': { 'name': 'The Martyrs of Papua New Guinea', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Martyrs_of_Papua_New_Guinea', 'prec':3},
            '09-03': { 'name': 'Gregory the Great', 'url': 'https://en.wikipedia.org/wiki/Pope_Gregory_I', 'prec':4, 'readings': ['1 Thessalonians 2:3-8'] },
            '09-04': { 'name': 'Birinus', 'url': 'https://en.wikipedia.org/wiki/Birinus', 'prec':3},
            '09-06': { 'name': 'Allen Gardiner', 'url': 'https://en.wikipedia.org/wiki/Allen_Gardiner', 'prec':3},
            '09-08': { 'name': 'The Birth of the Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Nativity_of_Mary', 'prec':4, 'readings': ['Ruth 4:13-16', 'James 1:17-18', 'Luke 8:19-21'] },
            '09-09': { 'name': 'Charles Fuge Lowder', 'url': 'https://en.wikipedia.org/wiki/Charles_Fuge_Lowder', 'prec':3},
            '09-13': { 'name': 'John Chrysostom', 'url': 'https://en.wikipedia.org/wiki/John_Chrysostom', 'prec':4, 'readings': ['Matthew 5:13-19', 'Jeremiah 1:4-10'] },
            '09-14': { 'name': 'Holy Cross Day', 'url': 'https://en.wikipedia.org/wiki/Feast_of_the_Cross', 'prec':7, 'readings': ['Numbers 21:4-9', 'Philippians 2:6-11', 'John 3:13-17', 'Psalm 22:23-28'] },
            '09-15': { 'name': 'Cyprian, Bishop of Carthage', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Cyprian', 'prec':4, 'readings': ['1 Peter 4:12-end', 'Matthew 18:18-22'] },
            '09-16': { 'name': 'Ninian', 'url': 'https://en.wikipedia.org/wiki/Saint_Ninian', 'prec':4, 'readings': ['Acts 13:46-49', 'Mark 16.:5-end'] },
            '09-17': { 'name': 'Hildegard', 'url': 'https://en.wikipedia.org/wiki/Hildegard_of_Bingen', 'prec':4, 'readings': ['1 Corinthians 2:9-13', 'Luke 10:21-24'] },
            '09-19': { 'name': 'Theodore', 'url': 'https://en.wikipedia.org/wiki/Theodore_of_Tarsus', 'prec':3},
            '09-20': { 'name': 'John Coleridge Patteson and companions', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/John_Coleridge_Patteson', 'prec':4, 'readings': ['2 Chronicles 24:17-21', 'Acts 7:55-end'] },
            '09-21': { 'name': 'Matthew the Evangelist', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Matthew_the_Evangelist', 'prec':7, 'readings': ['Proverbs 3:13-18', '2 Corinthians 4:1-6 ', 'Matthew 9:9-13', 'Psalm 119:65-72'] },
            '09-25': { 'name': 'Lancelot Andrewes', 'url': 'https://en.wikipedia.org/wiki/Lancelot_Andrewes', 'prec':4, 'readings': ['Isaiah 6:1-8'] },
            '09-26': { 'name': 'Wilson Carlile', 'url': 'https://en.wikipedia.org/wiki/Wilson_Carlile', 'prec':3},
            '09-27': { 'name': 'Vincent de Paul', 'url': 'https://en.wikipedia.org/wiki/Vincent_de_Paul', 'prec':4, 'readings': ['1 Corinthians 1:25-end', 'Matthew 25:34-40'] },
            '09-29': { 'name': 'Michael and All Angels', 'url': 'https://en.wikipedia.org/wiki/Michaelmas', 'prec':7, 'readings': ['Genesis 28:10-17', 'Revelation 12:7-12', 'John 1:47-51', 'Psalm 103:19-22'] },
            '09-30': { 'name': 'Jerome', 'url': 'https://en.wikipedia.org/wiki/St._Jerome', 'prec':3},

            '10-01': { 'name': 'Remigius', 'url': 'https://en.wikipedia.org/wiki/Saint_Remigius', 'prec':3},
            '10-03': { 'name': 'George Bell', 'url': 'https://en.wikipedia.org/wiki/George_Bell_(bishop)', 'prec':3},
            '10-04': { 'name': 'Francis of Assisi', 'url': 'https://en.wikipedia.org/wiki/Francis_of_Assisi', 'prec':3, 'readings': ['Galatians 6:14-end', 'Luke 12:22-34'] },
            '10-06': { 'name': 'William Tyndale', 'url': 'https://en.wikipedia.org/wiki/William_Tyndale', 'prec':4, 'readings': ['Proverbs 8:4-11', '2 Timothy 3:12-end'] },
            '10-09': { 'name': 'Robert Grosseteste', 'url': 'https://en.wikipedia.org/wiki/Robert_Grosseteste', 'prec':3},
            '10-10': { 'name': 'Paulinus', 'url': 'https://en.wikipedia.org/wiki/Paulinus_of_York', 'prec':4, 'readings': ['Matthew 28:16-end'] },
            '10-11': { 'name': 'Ethelburga', 'url': 'https://en.wikipedia.org/wiki/Ethelburga_of_Barking', 'prec':3},
            '10-12': { 'name': 'Wilfrid', 'url': 'https://en.wikipedia.org/wiki/Wilfrid', 'prec':4, 'readings': ['Luke 5:1-11', '1 Corinthians 1:18-25'] },
            '10-13': { 'name': 'Edward the Confessor', 'url': 'https://en.wikipedia.org/wiki/Edward_the_Confessor', 'prec':4, 'readings': ['2 Samuel 23:1-5', '1 John 4:13-16'] },
            '10-15': { 'name': 'Teresa of Avila', 'url': 'https://en.wikipedia.org/wiki/Teresa_of_%C3%81vila', 'prec':4, 'readings': ['Romans 8.22-27'] },
            '10-16': { 'name': 'Nicholas Ridley and Hugh Latimer', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Nicholas_Ridley_(martyr)', 'prec':3},
            '10-17': { 'name': 'Ignatius', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Ignatius_of_Antioch', 'prec':4, 'readings': ['Philippians 3:7-12', 'John 6:52-58'] },
            '10-18': { 'name': 'Luke the Evangelist', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Luke_the_Evangelist', 'prec':7, 'readings': ['2 Timothy 4:5-17', 'Psalm 147:1-7', 'Luke 10:1-9', '	Isaiah 35:3-6 or Acts 16:6-12'] },
            '10-19': { 'name': 'Henry Martyn', 'url': 'https://en.wikipedia.org/wiki/Henry_Martyn', 'prec':4, 'readings': ['Mark 16:15-end', 'Isaiah 55:6-11'] },
            '10-25': { 'name': 'Crispin and Crispinian', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Crispin', 'prec':3},
            '10-26': { 'name': 'Alfred the Great', 'url': 'https://en.wikipedia.org/wiki/Alfred_the_Great', 'prec':4, 'readings': ['2 Samuel 23:1-5', 'John 18:33-37'] },
            '10-28': { 'name': 'Simon and Jude, Apostles', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Simon_the_Zealot', 'prec':7, 'readings': ['Isaiah 28:14-16', 'Psalm 119:89-96', 'Ephesians 2:19-22', 'John 15:17-27'] },
            '10-29': { 'name': 'James Hannington', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/James_Hannington', 'prec':4, 'readings': ['Matthew 10:28-39'] },
            '10-31': { 'name': 'Martin Luther', 'url': 'https://en.wikipedia.org/wiki/Martin_Luther', 'prec':3},

            # All Saints’ Sunday? Has an A B C reading
            '11-01': { 'name': 'All Saints', 'url': 'https://en.wikipedia.org/wiki/All_Saints%27_Day', 'prec':9, 'type': 'Principal Feast'},
            '11-02': { 'name': 'All Souls', 'url': 'https://en.wikipedia.org/wiki/All_Souls%27_Day', 'colour':'purple', 'prec':4, 'readings': ['Lamentations 3:17–26, 31–33', 'Psalm 23 or Psalm 27:1–6,16,17', 'Romans 5:5–11 or 1 Peter 1:3–9', 'John 5:19–25 or John 6:37–40' ]},
            '11-03': { 'name': 'Richard Hooker', 'url': 'https://en.wikipedia.org/wiki/Richard_Hooker', 'prec':4, 'readings': ['John 16:12-15', 'Ecclesiasticus 44:10-15'] },
            '11-06': { 'name': 'Leonard', 'url': 'https://en.wikipedia.org/wiki/Leonard_of_Noblac', 'prec':3},
            '11-07': { 'name': 'Willibrord', 'url': 'https://en.wikipedia.org/wiki/Willibrord', 'prec':4, 'readings': ['Isaiah 52:7-10', 'Matthew 28:16-end'] },
            '11-08': { 'name': 'The Saints and Martyrs of England', 'prec':4, 'readings': ['Isaiah 61.4–9', 'Psalm 15', 'Revelation 19:5–10', 'John 17:18–23'] },
            '11-09': { 'name': 'Margery Kempe', 'url': 'https://en.wikipedia.org/wiki/Margery_Kempe', 'prec':3},
            '11-10': { 'name': 'Leo the Great', 'url': 'https://en.wikipedia.org/wiki/Pope_Leo_I', 'prec':4, 'readings': ['1 Peter 5:1-11'] },
            '11-11': { 'name': 'Martin', 'url': 'https://en.wikipedia.org/wiki/Martin_of_Tours', 'prec':4, 'readings': ['1 Thessalonians 5:1-11', 'Matthew 25:34-40'] },
            '11-13': { 'name': 'Charles Simeon', 'url': 'https://en.wikipedia.org/wiki/Charles_Simeon', 'prec':4, 'readings': ['Malachi 2:5-7', 'Colossians 1:3-8', 'Luke 8:4-8'] },
            '11-14': { 'name': 'Samuel Seabury', 'url': 'https://en.wikipedia.org/wiki/Samuel_Seabury_(1729%E2%80%931796)', 'prec':3},
            '11-16': { 'name': 'Margaret', 'url': 'https://en.wikipedia.org/wiki/Saint_Margaret_of_Scotland', 'prec':4, 'readings': ['Proverbs 31:10-12,20,26-end', '1 Corinthians 12:13–13:3', 'Matthew 25:34-end'] },
            '11-17': { 'name': 'Hugh', 'url': 'https://en.wikipedia.org/wiki/Hugh_of_Lincoln', 'prec':4, 'readings': ['1 Timothy 6:11-16'] },
            '11-18': { 'name': 'Elizabeth', 'url': 'https://en.wikipedia.org/wiki/Elisabeth_of_Hungary', 'prec':4, 'readings': ['Matthew 25:31-end', 'Proverbs 31:10-end'] },
            '11-19': { 'name': 'Hilda', 'url': 'https://en.wikipedia.org/wiki/Hilda_of_Whitby', 'prec':4, 'readings': ['Isaiah 61:10–62:5'] },
            '11-20': { 'name': 'Edmund', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Edmund_the_Martyr', 'prec':4, 'readings': ['Proverbs 20:28', 'Proverbs 21:1-4,7'] },
            '11-22': { 'name': 'Cecilia', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Cecilia_(saint)', 'prec':3},
            '11-23': { 'name': 'Clement', 'url': 'https://en.wikipedia.org/wiki/Pope_Clement_I', 'prec':4, 'readings': ['Philippians 3:17–4:3', 'Matthew 16:13-19'] },
            '11-25': { 'name': 'Catherine', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Catherine_of_Alexandria', 'prec':3},
            '11-30': { 'name': 'Andrew the Apostle', 'url': 'https://en.wikipedia.org/wiki/Saint_Andrew', 'prec':7, 'readings': ['Isaiah 52:7-10', 'Psalm 19:1-6', 'Romans 10:12-18', 'Matthew 4:18-22'] },

            '12-01': { 'name': 'Charles de Foucauld', 'url': 'https://en.wikipedia.org/wiki/Charles_de_Foucauld', 'prec':3},
            '12-03': { 'name': 'Francis Xavier', 'url': 'https://en.wikipedia.org/wiki/Francis_Xavier', 'prec':3},
            '12-04': { 'name': 'John of Damascus', 'url': 'https://en.wikipedia.org/wiki/John_of_Damascus', 'prec':3},
            '12-06': { 'name': 'Nicholas', 'url': 'https://en.wikipedia.org/wiki/Saint_Nicholas', 'prec':4, 'readings': ['Isaiah 61:1-3', '1 Timothy 6:6-11', 'Mark 10:13-16'] },
            '12-07': { 'name': 'Ambrose', 'url': 'https://en.wikipedia.org/wiki/Ambrose', 'prec':4, 'readings': ['Isaiah 41:9-13', 'Luke 22:24-30'] },
            '12-08': { 'name': 'The Conception of the Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Feast_of_the_Immaculate_Conception', 'prec':7, 'readings': ['Genesis 3:8-15', 'Galatians 4:4-7', 'Luke 1:26-38', 'Psalm 113'] },
            '12-13': { 'name': 'Lucy', 'url': 'https://en.wikipedia.org/wiki/Saint_Lucy', 'prec':4, 'readings': ['Wisdom 3:1-7', '2 Corinthians 4:6-15'] },
            '12-14': { 'name': 'John of the Cross', 'url': 'https://en.wikipedia.org/wiki/John_of_the_Cross', 'prec':4, 'readings': ['1 Corinthians 2:1-10', 'John 14:18-23'] },
            '12-17': { 'name': 'Eglantine Jebb', 'url': 'https://en.wikipedia.org/wiki/Eglantyne_Jebb', 'prec':3},
            '12-24': { 'name': 'Christmas Eve', 'url': 'https://en.wikipedia.org/wiki/Christmas_Eve', 'prec':4, 'readings': ['2 Samuel 7:1-5,8-11,16', 'Psalm 89:2,19-27', 'Acts 13:16-26', 'Luke 1:67-79']},
            '12-25': { 'name': 'Christmas', 'url': 'https://en.wikipedia.org/wiki/Christmas_Day', 'prec':9, 'type': 'Principal Feast', 'readings': ['Isaiah 52:7-10', 'Psalm 98', 'Hebrews 1:1-4[5-12]', 'John 1:1-14']},
            '12-26': { 'name': 'Stephen', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Stephen', 'prec':7, 'readings': ['Acts 7:51-60', 'Psalm 119:161-168', 'Matthew 10:17-22', '2 Chronicles 24:20-22']},
            '12-27': { 'name': 'John the Apostle', 'url': 'https://en.wikipedia.org/wiki/John_the_Apostle', 'prec':7, 'readings': ['1 John 1', 'Psalm 117', 'John 21:19-25', 'Exodus 33:7-11']},
            '12-28': { 'name': 'The Holy Innocents', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Massacre_of_the_Innocents', 'prec':7, 'readings': ['Jeremiah 31:15-17', 'Psalm 124', '1 Corinthians 1:26-29', 'Matthew 2:13-18']},
            '12-29': { 'name': 'Thomas Becket', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Thomas_Becket', 'prec':4, 'readings': ['Matthew 10:28-33', 'Ecclesiasticus 51:1-8']},
            '12-31': { 'name': 'John Wyclif', 'url': 'https://en.wikipedia.org/wiki/John_Wycliffe', 'prec':3}
        }
    }

    # Get the feast from the list above
    feast = feasts[relative_to].get(pointer)

    # Append extra common info. Careful with prec=9 here as some are
    # Principal Feasts and some are Principal Holy Days
    if feast:
        if feast['prec'] == 3:
            feast['type'] = 'Commemoration'
            feast['type_url'] = 'https://en.wikipedia.org/wiki/Commemoration_(Anglicanism)'
        elif feast['prec'] == 4:
            feast['type'] = 'Lesser Festival'
            feast['type_url'] = 'https://en.wikipedia.org/wiki/Lesser_Festival'
        elif feast['prec'] == 5:
            pass
        elif feast['prec'] == 7:
            feast['type'] = 'Festival'
            feast['type_url'] = 'https://en.wikipedia.org/wiki/Festival_(Church_of_England)'
        elif feast['prec'] == 9:
            if feast['type'] == 'Principal Holy Day':
                feast['type_url'] = 'https://en.wikipedia.org/wiki/Principal_Holy_Day'
            elif feast['type'] == 'Principal Feast':
                feast['type_url'] = 'https://en.wikipedia.org/wiki/Principal_Feast'

    return feast

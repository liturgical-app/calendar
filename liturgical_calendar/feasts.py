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
            -46: { 'name': 'Ash Wednesday', 'colour':'purple', 'url': 'https://en.wikipedia.org/wiki/Ash_Wednesday', 'prec':9, 'type': 'Principal Holy Day' },
            -7: { 'name': 'Palm Sunday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Palm_Sunday', 'prec':5 },
            -6: { 'name': 'Holy Monday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Holy_Monday', 'prec':9, 'type': 'Principal Holy Day'},
            -5: { 'name': 'Holy Tuesday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Holy_Tuesday', 'prec':9, 'type': 'Principal Holy Day'},
            -4: { 'name': 'Holy Wednesday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Holy_Wednesday', 'prec':9, 'type': 'Principal Holy Day'},
            -3: { 'name': 'Maundy Thursday', 'colour':'white', 'url': 'https://en.wikipedia.org/wiki/Maundy_Thursday', 'prec':9, 'type': 'Principal Holy Day'},
            -2: { 'name': 'Good Friday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Good_Friday', 'prec':9, 'type': 'Principal Holy Day' },
            -1: { 'name': 'Holy Saturday', 'colour':'not given', 'url': 'https://en.wikipedia.org/wiki/Holy_Saturday', 'prec':9, 'type': 'Principal Holy Day' },
            0 : { 'name': 'Easter', 'url': 'https://en.wikipedia.org/wiki/Easter', 'prec':9, 'type': 'Principal Feast' },
            39: { 'name': 'Ascension', 'url': 'https://en.wikipedia.org/wiki/Ascension_Day', 'prec':9, 'type': 'Principal Feast' },
            49: { 'name': 'Pentecost', 'colour': 'red', 'url': 'https://en.wikipedia.org/wiki/Pentecost', 'prec':9, 'type': 'Principal Feast' },
            56: { 'name': 'Trinity', 'url': 'https://en.wikipedia.org/wiki/Trinity_Sunday', 'prec':9, 'type': 'Principal Feast' },
            60: { 'name': 'Corpus Christi', 'url':'https://en.wikipedia.org/wiki/Corpus_Christi_(feast)', 'prec':7 },
        },
        'christmas': {
            '01-01': { 'name': 'The Naming and Circumcision of Jesus', 'url': 'https://en.wikipedia.org/wiki/Circumcision_of_Christ', 'prec':7 },
            '01-02': { 'name': 'Basil the Great and Gregory of Nazianzus', 'url': 'https://en.wikipedia.org/wiki/Basil_of_Caesarea', 'prec':4},
            '01-06': { 'name': 'Epiphany', 'url': 'https://en.wikipedia.org/wiki/Epiphany_(Christian)', 'prec':9, 'type': 'Principal Feast'},
            '01-07': { 'name': 'The Baptism of Christ', 'url': 'https://en.wikipedia.org/wiki/Baptism_of_the_Lord', 'prec':7},
            '01-10': { 'name': 'William Laud', 'url': 'https://en.wikipedia.org/wiki/William_Laud', 'prec':3},
            '01-11': { 'name': 'Mary Slessor', 'url': 'https://en.wikipedia.org/wiki/Mary_Slessor', 'prec':3},
            '01-12': { 'name': 'Aelred of Hexham', 'url': 'https://en.wikipedia.org/wiki/Ailred_of_Rievaulx', 'prec':4},
            '01-13': { 'name': 'Hilary', 'url': 'https://en.wikipedia.org/wiki/Hilary_of_Poitiers', 'prec':4},
            '01-17': { 'name': 'Antony of Egypt', 'url': 'https://en.wikipedia.org/wiki/Anthony_the_Great', 'prec':4},
            '01-18': { 'name': 'Amy Carmichael', 'url': 'https://en.wikipedia.org/wiki/Amy_Carmichael', 'prec':3},
            '01-19': { 'name': 'Wulfstan', 'url': 'https://en.wikipedia.org/wiki/Wulfstan,_Bishop_of_Worcester', 'prec':4},
            '01-20': { 'name': 'Richard Rolle', 'url': 'https://en.wikipedia.org/wiki/Richard_Rolle', 'prec':3},
            '01-21': { 'name': 'Agnes', 'url': 'https://en.wikipedia.org/wiki/Saint_Agnes', 'prec':4},
            '01-22': { 'name': 'Vincent of Saragossa', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Vincent_of_Saragossa', 'prec':3},
            '01-24': { 'name': 'Francis de Sales', 'url': 'https://en.wikipedia.org/wiki/Francis_de_Sales', 'prec':4},
            '01-25': { 'name': 'The Conversion of Paul', 'url': 'https://en.wikipedia.org/wiki/Conversion_of_Paul', 'prec':7},
            '01-26': { 'name': 'Timothy and Titus', 'url': 'https://en.wikipedia.org/wiki/Saint_Timothy', 'prec':4},
            '01-28': { 'name': 'Thomas Aquinas', 'url': 'https://en.wikipedia.org/wiki/Thomas_Aquinas', 'prec':4},
            '01-30': { 'name': 'Charles, king and martyr', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Charles,_King_and_Martyr', 'prec':4},
            '01-31': { 'name': 'John Bosco', 'url': 'https://en.wikipedia.org/wiki/John_Bosco', 'prec':3},

            '02-01': { 'name': 'Brigid of Kildare', 'url': 'https://en.wikipedia.org/wiki/Brigid_of_Kildare', 'prec':3},
            '02-02': { 'name': 'Presentation of Christ at the Temple', 'url': 'https://en.wikipedia.org/wiki/Presentation_of_Jesus_at_the_Temple', 'prec':9, 'type': 'Principal Feast'},
            '02-03': { 'name': 'Anskar', 'url': 'https://en.wikipedia.org/wiki/Ansgar', 'prec':4},
            '02-04': { 'name': 'Gilbert of Sempringham', 'url': 'https://en.wikipedia.org/wiki/Gilbert_of_Sempringham', 'prec':3},
            '02-06': { 'name': 'Martyrs of Japan', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/26_Martyrs_of_Japan', 'prec':3},
            '02-10': { 'name': 'Scholastica', 'url': 'https://en.wikipedia.org/wiki/Scholastica', 'prec':3},
            '02-14': { 'name': 'Valentine', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Valentine', 'prec':3},
            '02-15': { 'name': 'Thomas Bray', 'url': 'https://en.wikipedia.org/wiki/Thomas_Bray', 'prec':3},
            '02-17': { 'name': 'Janani Luwum', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Janani_Luwum', 'prec':4},
            '02-23': { 'name': 'Polycarp', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Polycarp', 'prec':4},
            '02-27': { 'name': 'George Herbert', 'url': 'https://en.wikipedia.org/wiki/George_Herbert', 'prec':4},

            '03-01': { 'name': 'David', 'url': 'https://en.wikipedia.org/wiki/Saint_David', 'prec':4},
            '03-02': { 'name': 'Chad', 'url': 'https://en.wikipedia.org/wiki/Chad_of_Mercia', 'prec':4},
            '03-07': { 'name': 'Perpetua, Felicity and companions', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Perpetua_and_Felicitas', 'prec':4},
            '03-08': { 'name': 'Edward King', 'url': 'https://en.wikipedia.org/wiki/Edward_King_(English_bishop)', 'prec':4},
            '03-17': { 'name': 'Patrick', 'url': 'https://en.wikipedia.org/wiki/Saint_Patrick%27s_Day', 'prec':4},
            '03-18': { 'name': 'Cyril', 'url': 'https://en.wikipedia.org/wiki/Cyril_of_Jerusalem', 'prec':3},
            '03-19': { 'name': 'Joseph of Nazareth', 'url': 'https://en.wikipedia.org/wiki/Saint_Joseph', 'prec':7},
            '03-20': { 'name': 'Cuthbert', 'url': 'https://en.wikipedia.org/wiki/Cuthbert_of_Lindisfarne', 'prec':4},
            '03-21': { 'name': 'Thomas Cranmer', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Thomas_Cranmer', 'prec':4},
            '03-24': { 'name': 'Walter Hilton of Thurgarton', 'url': 'https://en.wikipedia.org/wiki/Walter_Hilton', 'prec':3},
            '03-25': { 'name': 'The Annunciation of our Lord', 'url': 'https://en.wikipedia.org/wiki/Annunciation', 'prec':9, 'type': 'Principal Feast'},
            '03-26': { 'name': 'Harriet Monsell', 'url': 'https://en.wikipedia.org/wiki/Harriet_Monsell', 'prec':3},
            '03-31': { 'name': 'John Donne', 'url': 'https://en.wikipedia.org/wiki/John_Donne', 'prec':3},

            '04-01': { 'name': 'Frederick Denison Maurice', 'url': 'https://en.wikipedia.org/wiki/Frederick_Denison_Maurice', 'prec':3},
            '04-09': { 'name': 'Dietrich Bonhoeffer', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Dietrich_Bonhoeffer', 'prec':3},
            '04-10': { 'name': 'William Law', 'url': 'https://en.wikipedia.org/wiki/William_Law', 'prec':4},
            '04-11': { 'name': 'George Selwyn', 'url': 'https://en.wikipedia.org/wiki/George_Selwyn_(Bishop_of_Lichfield)', 'prec':3},
            '04-16': { 'name': 'Isabella Gilmore', 'url': 'https://en.wikipedia.org/wiki/Isabella_Gilmore', 'prec':3},
            '04-19': { 'name': 'Alphege', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Alphege', 'prec':4},
            '04-21': { 'name': 'Anselm', 'url': 'https://en.wikipedia.org/wiki/Anselm_of_Canterbury', 'prec':4},
            '04-23': { 'name': 'George', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_George', 'prec':7},
            '04-24': { 'name': 'Mellitus', 'url': 'https://en.wikipedia.org/wiki/Mellitus', 'prec':3},
            '04-25': { 'name': 'Mark the Evangelist', 'url': 'https://en.wikipedia.org/wiki/Mark_the_Evangelist', 'prec':7},
            '04-27': { 'name': 'Christina Rossetti', 'url': 'https://en.wikipedia.org/wiki/Christina_Rossetti', 'prec':3},
            '04-28': { 'name': 'Peter Chanel', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Peter_Chanel', 'prec':3},
            '04-29': { 'name': 'Catherine of Siena', 'url': 'https://en.wikipedia.org/wiki/Catherine_of_Siena', 'prec':4},
            '04-30': { 'name': 'Pandita Mary Ramabai', 'url': 'https://en.wikipedia.org/wiki/Pandita_Ramabai', 'prec':3},

            '05-01': { 'name': 'Philip and James, Apostles', 'url': 'https://en.wikipedia.org/wiki/Philip_the_Apostle', 'prec':7},
            '05-02': { 'name': 'Athanasius', 'url': 'https://en.wikipedia.org/wiki/Athanasius_of_Alexandria', 'prec':4},
            '05-04': { 'name': 'English Saints and Martyrs of the Reformation Era', 'prec':4},
            '05-08': { 'name': 'Julian of Norwich', 'url': 'https://en.wikipedia.org/wiki/Julian_of_Norwich', 'prec':4},
            '05-12': { 'name': 'Gregory Dix', 'url': 'https://en.wikipedia.org/wiki/Gregory_Dix', 'prec':3},
            '05-14': { 'name': 'Matthias the Apostle', 'url': 'https://en.wikipedia.org/wiki/Saint_Matthias', 'prec':7},
            '05-16': { 'name': 'Caroline Chisholm', 'url': 'https://en.wikipedia.org/wiki/Caroline_Chisholm', 'prec':3},
            '05-19': { 'name': 'Dunstan', 'url': 'https://en.wikipedia.org/wiki/Dunstan', 'prec':4},
            '05-20': { 'name': 'Alcuin', 'url': 'https://en.wikipedia.org/wiki/Alcuin', 'prec':4},
            '05-21': { 'name': 'Helena', 'url': 'https://en.wikipedia.org/wiki/Helena_of_Constantinople', 'prec':3},
            '05-24': { 'name': 'John and Charles Wesley', 'url': 'https://en.wikipedia.org/wiki/John_Wesley', 'prec':4},
            '05-25': { 'name': 'The Venerable Bede', 'url': 'https://en.wikipedia.org/wiki/Bede', 'prec':4},
            '05-26': { 'name': 'Augustine of Canterbury', 'url': 'https://en.wikipedia.org/wiki/Augustine_of_Canterbury', 'prec':4},
            '05-28': { 'name': 'Lanfranc', 'url': 'https://en.wikipedia.org/wiki/Lanfranc', 'prec':3},
            '05-30': { 'name': 'Josephine Butler', 'url': 'https://en.wikipedia.org/wiki/Josephine_Butler', 'prec':4},
            '05-31': { 'name': 'The Visit of the Blessed Virgin Mary to Elizabeth', 'prec':7},

            '06-01': { 'name': 'Justin', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Justin_Martyr', 'prec':4},
            '06-03': { 'name': 'Martyrs of Uganda', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Martyrs_of_Uganda', 'prec':3},
            '06-04': { 'name': 'Petroc', 'url': 'https://en.wikipedia.org/wiki/Saint_Petroc', 'prec':3},
            '06-05': { 'name': 'Boniface', 'url': 'https://en.wikipedia.org/wiki/Saint_Boniface', 'prec':4},
            '06-06': { 'name': 'Ini Kopuria', 'url': 'https://en.wikipedia.org/wiki/Ini_Kopuria', 'prec':3},
            '06-08': { 'name': 'Thomas Ken', 'url': 'https://en.wikipedia.org/wiki/Thomas_Ken', 'prec':4},
            '06-09': { 'name': 'Columba', 'url': 'https://en.wikipedia.org/wiki/Columba', 'prec':4},
            '06-10': { 'name': 'Ephrem of Syria', 'url': 'https://en.wikipedia.org/wiki/Ephrem_the_Syrian', 'prec':3},
            '06-11': { 'name': 'Barnabas the Apostle', 'url': 'https://en.wikipedia.org/wiki/Barnabas', 'prec':7},
            '06-14': { 'name': 'Richard Baxter', 'url': 'https://en.wikipedia.org/wiki/Richard_Baxter', 'prec':3},
            '06-15': { 'name': 'Evelyn Underhill', 'url': 'https://en.wikipedia.org/wiki/Evelyn_Underhill', 'prec':3},
            '06-16': { 'name': 'Richard of Chichester', 'url': 'https://en.wikipedia.org/wiki/Richard_of_Chichester', 'prec':4},
            '06-17': { 'name': 'Samuel and Henrietta Barnett', 'url': 'https://en.wikipedia.org/wiki/Samuel_Augustus_Barnett', 'prec':3},
            '06-18': { 'name': 'Bernard Mizeki', 'url': 'https://en.wikipedia.org/wiki/Bernard_Mizeki', 'prec':3},
            '06-19': { 'name': 'Sundar Singh', 'url': 'https://en.wikipedia.org/wiki/Sadhu_Sundar_Singh', 'prec':3},
            '06-22': { 'name': 'Alban', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Alban', 'prec':4},
            '06-23': { 'name': 'Etheldreda', 'url': 'https://en.wikipedia.org/wiki/%C3%86thelthryth', 'prec':4},
            '06-24': { 'name': 'The Birth of John the Baptist', 'url': 'https://en.wikipedia.org/wiki/Nativity_of_St._John_the_Baptist', 'prec':7},
            '06-27': { 'name': 'Cyril', 'url': 'https://en.wikipedia.org/wiki/Cyril_of_Alexandria', 'prec':3},
            '06-28': { 'name': 'Irenaeus', 'url': 'https://en.wikipedia.org/wiki/Irenaeus', 'prec':4},
            '06-29': { 'name': 'Peter and Paul, Apostles', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Peter', 'prec':7},

            '07-01': { 'name': 'Henry, John, and Henry Venn', 'url': 'https://en.wikipedia.org/wiki/Henry_Venn_(Clapham_Sect)', 'prec':3},
            '07-03': { 'name': 'Thomas the Apostle', 'url': 'https://en.wikipedia.org/wiki/Thomas_the_Apostle', 'prec':7},
            '07-06': { 'name': 'Thomas More and John Fisher', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Thomas_More', 'prec':3},
            '07-11': { 'name': 'Benedict', 'url': 'https://en.wikipedia.org/wiki/Benedict_of_Nursia', 'prec':4},
            '07-14': { 'name': 'John Keble', 'url': 'https://en.wikipedia.org/wiki/John_Keble', 'prec':4},
            '07-15': { 'name': 'Swithun', 'url': 'https://en.wikipedia.org/wiki/Swithun', 'prec':4},
            '07-16': { 'name': 'Osmund', 'url': 'https://en.wikipedia.org/wiki/Saint_Osmund', 'prec':3},
            '07-18': { 'name': 'Elizabeth Ferard', 'url': 'https://en.wikipedia.org/wiki/Elizabeth_Ferard', 'prec':3},
            '07-19': { 'name': 'Gregory, and his sister Macrina', 'url': 'https://en.wikipedia.org/wiki/Gregory_of_Nyssa', 'prec':4},
            '07-20': { 'name': 'Margaret of Antioch', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Margaret_the_Virgin', 'prec':3},
            '07-22': { 'name': 'Mary Magdalene', 'url': 'https://en.wikipedia.org/wiki/Mary_Magdalene', 'prec':7},
            '07-23': { 'name': 'Bridget', 'url': 'https://en.wikipedia.org/wiki/Bridget_of_Sweden', 'prec':3},
            '07-25': { 'name': 'James the Apostle', 'url': 'https://en.wikipedia.org/wiki/James,_son_of_Zebedee', 'prec':7},
            '07-26': { 'name': 'Parents of the Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Saint_Anne', 'prec':4},
            '07-27': { 'name': 'Brooke Foss Westcott', 'url': 'https://en.wikipedia.org/wiki/Brooke_Foss_Westcott', 'prec':3},
            '07-29': { 'name': 'Mary, Martha and Lazarus', 'url': 'https://en.wikipedia.org/wiki/Mary,_sister_of_Lazarus', 'prec':4},
            '07-30': { 'name': 'William Wilberforce', 'url': 'https://en.wikipedia.org/wiki/William_Wilberforce', 'prec':3},
            '07-31': { 'name': 'Ignatius of Loyola', 'url': 'https://en.wikipedia.org/wiki/Ignatius_of_Loyola', 'prec':3},

            '08-04': { 'name': 'Jean-Baptiste Vianney', 'url': 'https://en.wikipedia.org/wiki/Jean_Vianney', 'prec':3},
            '08-05': { 'name': 'Oswald', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Oswald_of_Northumbria', 'prec':4},
            '08-06': { 'name': 'The Transfiguration of Our Lord', 'url': 'https://en.wikipedia.org/wiki/Transfiguration_of_Jesus', 'prec':7},
            '08-07': { 'name': 'John Mason Neale', 'url': 'https://en.wikipedia.org/wiki/John_Mason_Neale', 'prec':3},
            '08-08': { 'name': 'Dominic', 'url': 'https://en.wikipedia.org/wiki/Saint_Dominic', 'prec':4},
            '08-09': { 'name': 'Mary Sumner', 'url': 'https://en.wikipedia.org/wiki/Mary_Sumner', 'prec':4},
            '08-10': { 'name': 'Laurence', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Lawrence_of_Rome', 'prec':4},
            '08-11': { 'name': 'Clare', 'url': 'https://en.wikipedia.org/wiki/Clare_of_Assisi', 'prec':4},
            '08-13': { 'name': 'Jeremy Taylor', 'url': 'https://en.wikipedia.org/wiki/Jeremy_Taylor', 'prec':4},
            '08-14': { 'name': 'Maximilian Kolbe', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Maximilian_Kolbe', 'prec':3},
            '08-15': { 'name': 'The Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Blessed_Virgin_Mary', 'prec':7},
            '08-20': { 'name': 'Bernard', 'url': 'https://en.wikipedia.org/wiki/Bernard_of_Clairvaux', 'prec':4},
            '08-24': { 'name': 'Bartholomew the Apostle', 'url': 'https://en.wikipedia.org/wiki/Bartholomew_the_Apostle', 'prec':7},
            '08-27': { 'name': 'Monica', 'url': 'https://en.wikipedia.org/wiki/Monica_of_Hippo', 'prec':4},
            '08-28': { 'name': 'Augustine', 'url': 'https://en.wikipedia.org/wiki/Augustine_of_Hippo', 'prec':4},
            '08-29': { 'name': 'The Beheading of John the Baptist', 'url': 'https://en.wikipedia.org/wiki/John_the_Baptist', 'prec':4},
            '08-30': { 'name': 'John Bunyan', 'url': 'https://en.wikipedia.org/wiki/John_Bunyan', 'prec':4},
            '08-31': { 'name': 'Aidan', 'url': 'https://en.wikipedia.org/wiki/Aidan_of_Lindisfarne', 'prec':4},

            '09-01': { 'name': 'Giles of Provence', 'url': 'https://en.wikipedia.org/wiki/Saint_Giles', 'prec':3},
            '09-02': { 'name': 'The Martyrs of Papua New Guinea', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Martyrs_of_Papua_New_Guinea', 'prec':3},
            '09-03': { 'name': 'Gregory the Great', 'url': 'https://en.wikipedia.org/wiki/Pope_Gregory_I', 'prec':4},
            '09-04': { 'name': 'Birinus', 'url': 'https://en.wikipedia.org/wiki/Birinus', 'prec':3},
            '09-06': { 'name': 'Allen Gardiner', 'url': 'https://en.wikipedia.org/wiki/Allen_Gardiner', 'prec':3},
            '09-08': { 'name': 'The Birth of the Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Nativity_of_Mary', 'prec':4},
            '09-09': { 'name': 'Charles Fuge Lowder', 'url': 'https://en.wikipedia.org/wiki/Charles_Fuge_Lowder', 'prec':3},
            '09-13': { 'name': 'John Chrysostom', 'url': 'https://en.wikipedia.org/wiki/John_Chrysostom', 'prec':4},
            '09-14': { 'name': 'Holy Cross Day', 'url': 'https://en.wikipedia.org/wiki/Feast_of_the_Cross', 'prec':7},
            '09-15': { 'name': 'Cyprian, Bishop of Carthage', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Cyprian', 'prec':4},
            '09-16': { 'name': 'Ninian', 'url': 'https://en.wikipedia.org/wiki/Saint_Ninian', 'prec':4},
            '09-17': { 'name': 'Hildegard', 'url': 'https://en.wikipedia.org/wiki/Hildegard_of_Bingen', 'prec':4},
            '09-19': { 'name': 'Theodore', 'url': 'https://en.wikipedia.org/wiki/Theodore_of_Tarsus', 'prec':3},
            '09-20': { 'name': 'John Coleridge Patteson and companions', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/John_Coleridge_Patteson', 'prec':4},
            '09-21': { 'name': 'Matthew the Evangelist', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Matthew_the_Evangelist', 'prec':7},
            '09-25': { 'name': 'Lancelot Andrewes', 'url': 'https://en.wikipedia.org/wiki/Lancelot_Andrewes', 'prec':4},
            '09-26': { 'name': 'Wilson Carlile', 'url': 'https://en.wikipedia.org/wiki/Wilson_Carlile', 'prec':3},
            '09-27': { 'name': 'Vincent de Paul', 'url': 'https://en.wikipedia.org/wiki/Vincent_de_Paul', 'prec':4},
            '09-29': { 'name': 'Michael and All Angels', 'url': 'https://en.wikipedia.org/wiki/Michaelmas', 'prec':7},
            '09-30': { 'name': 'Jerome', 'url': 'https://en.wikipedia.org/wiki/St._Jerome', 'prec':3},

            '10-01': { 'name': 'Remigius', 'url': 'https://en.wikipedia.org/wiki/Saint_Remigius', 'prec':3},
            '10-03': { 'name': 'George Bell', 'url': 'https://en.wikipedia.org/wiki/George_Bell_(bishop)', 'prec':3},
            '10-04': { 'name': 'Francis of Assisi', 'url': 'https://en.wikipedia.org/wiki/Francis_of_Assisi', 'prec':3},
            '10-06': { 'name': 'William Tyndale', 'url': 'https://en.wikipedia.org/wiki/William_Tyndale', 'prec':4},
            '10-09': { 'name': 'Robert Grosseteste', 'url': 'https://en.wikipedia.org/wiki/Robert_Grosseteste', 'prec':3},
            '10-10': { 'name': 'Paulinus', 'url': 'https://en.wikipedia.org/wiki/Paulinus_of_York', 'prec':4},
            '10-11': { 'name': 'Ethelburga', 'url': 'https://en.wikipedia.org/wiki/Ethelburga_of_Barking', 'prec':3},
            '10-12': { 'name': 'Wilfrid', 'url': 'https://en.wikipedia.org/wiki/Wilfrid', 'prec':4},
            '10-13': { 'name': 'Edward the Confessor', 'url': 'https://en.wikipedia.org/wiki/Edward_the_Confessor', 'prec':4},
            '10-15': { 'name': 'Teresa of Avila', 'url': 'https://en.wikipedia.org/wiki/Teresa_of_%C3%81vila', 'prec':4},
            '10-16': { 'name': 'Nicholas Ridley and Hugh Latimer', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Nicholas_Ridley_(martyr)', 'prec':3},
            '10-17': { 'name': 'Ignatius', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Ignatius_of_Antioch', 'prec':4},
            '10-18': { 'name': 'Luke the Evangelist', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Luke_the_Evangelist', 'prec':7},
            '10-19': { 'name': 'Henry Martyn', 'url': 'https://en.wikipedia.org/wiki/Henry_Martyn', 'prec':4},
            '10-25': { 'name': 'Crispin and Crispinian', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Crispin', 'prec':3},
            '10-26': { 'name': 'Alfred the Great', 'url': 'https://en.wikipedia.org/wiki/Alfred_the_Great', 'prec':4},
            '10-28': { 'name': 'Simon and Jude, Apostles', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Simon_the_Zealot', 'prec':7},
            '10-29': { 'name': 'James Hannington', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/James_Hannington', 'prec':4},
            '10-31': { 'name': 'Martin Luther', 'url': 'https://en.wikipedia.org/wiki/Martin_Luther', 'prec':3},

            '11-01': { 'name': 'All Saints', 'url': 'https://en.wikipedia.org/wiki/All_Saints%27_Day', 'prec':9, 'type': 'Principal Feast'},
            '11-02': { 'name': 'All Souls', 'url': 'https://en.wikipedia.org/wiki/All_Souls%27_Day', 'colour':'purple', 'prec':4},
            '11-03': { 'name': 'Richard Hooker', 'url': 'https://en.wikipedia.org/wiki/Richard_Hooker', 'prec':4},
            '11-06': { 'name': 'Leonard', 'url': 'https://en.wikipedia.org/wiki/Leonard_of_Noblac', 'prec':3},
            '11-07': { 'name': 'Willibrord', 'url': 'https://en.wikipedia.org/wiki/Willibrord', 'prec':4},
            '11-08': { 'name': 'The Saints and Martyrs of England', 'prec':4},
            '11-09': { 'name': 'Margery Kempe', 'url': 'https://en.wikipedia.org/wiki/Margery_Kempe', 'prec':3},
            '11-10': { 'name': 'Leo the Great', 'url': 'https://en.wikipedia.org/wiki/Pope_Leo_I', 'prec':4},
            '11-11': { 'name': 'Martin', 'url': 'https://en.wikipedia.org/wiki/Martin_of_Tours', 'prec':4},
            '11-13': { 'name': 'Charles Simeon', 'url': 'https://en.wikipedia.org/wiki/Charles_Simeon', 'prec':4},
            '11-14': { 'name': 'Samuel Seabury', 'url': 'https://en.wikipedia.org/wiki/Samuel_Seabury_(1729%E2%80%931796)', 'prec':3},
            '11-16': { 'name': 'Margaret', 'url': 'https://en.wikipedia.org/wiki/Saint_Margaret_of_Scotland', 'prec':4},
            '11-17': { 'name': 'Hugh', 'url': 'https://en.wikipedia.org/wiki/Hugh_of_Lincoln', 'prec':4},
            '11-18': { 'name': 'Elizabeth', 'url': 'https://en.wikipedia.org/wiki/Elisabeth_of_Hungary', 'prec':4},
            '11-19': { 'name': 'Hilda', 'url': 'https://en.wikipedia.org/wiki/Hilda_of_Whitby', 'prec':4},
            '11-20': { 'name': 'Edmund', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Edmund_the_Martyr', 'prec':4},
            '11-22': { 'name': 'Cecilia', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Cecilia_(saint)', 'prec':3},
            '11-23': { 'name': 'Clement', 'url': 'https://en.wikipedia.org/wiki/Pope_Clement_I', 'prec':4},
            '11-25': { 'name': 'Catherine', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Catherine_of_Alexandria', 'prec':3},
            '11-30': { 'name': 'Andrew the Apostle', 'url': 'https://en.wikipedia.org/wiki/Saint_Andrew', 'prec':7},

            '12-01': { 'name': 'Charles de Foucauld', 'url': 'https://en.wikipedia.org/wiki/Charles_de_Foucauld', 'prec':3},
            '12-03': { 'name': 'Francis Xavier', 'url': 'https://en.wikipedia.org/wiki/Francis_Xavier', 'prec':3},
            '12-04': { 'name': 'John of Damascus', 'url': 'https://en.wikipedia.org/wiki/John_of_Damascus', 'prec':3},
            '12-06': { 'name': 'Nicholas', 'url': 'https://en.wikipedia.org/wiki/Saint_Nicholas', 'prec':4},
            '12-07': { 'name': 'Ambrose', 'url': 'https://en.wikipedia.org/wiki/Ambrose', 'prec':4},
            '12-08': { 'name': 'The Conception of the Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Feast_of_the_Immaculate_Conception', 'prec':7},
            '12-13': { 'name': 'Lucy', 'url': 'https://en.wikipedia.org/wiki/Saint_Lucy', 'prec':4},
            '12-14': { 'name': 'John of the Cross', 'url': 'https://en.wikipedia.org/wiki/John_of_the_Cross', 'prec':4},
            '12-17': { 'name': 'Eglantine Jebb', 'url': 'https://en.wikipedia.org/wiki/Eglantyne_Jebb', 'prec':3},
            '12-24': { 'name': 'Christmas Eve', 'url': 'https://en.wikipedia.org/wiki/Christmas_Eve', 'prec':4},
            '12-25': { 'name': 'Christmas', 'url': 'https://en.wikipedia.org/wiki/Christmas_Day', 'prec':9, 'type': 'Principal Feast'},
            '12-26': { 'name': 'Stephen', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Stephen', 'prec':7},
            '12-27': { 'name': 'John the Apostle', 'url': 'https://en.wikipedia.org/wiki/John_the_Apostle', 'prec':7},
            '12-28': { 'name': 'The Holy Innocents', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Massacre_of_the_Innocents', 'prec':7},
            '12-29': { 'name': 'Thomas Becket', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Thomas_Becket', 'prec':4},
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

"""
This is a massive function which effectively contains all of the data from this Wikipedia page:
https://en.wikipedia.org/wiki/Calendar_of_saints_(Church_of_England)
"""
def lookup_feast_artwork(relative_to, pointer):
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
            -46: { 'name': 'Ash Wednesday', 'source': 'https://www.instagram.com/p/DG0EMDKu47o/' },
            -7: { 'name': 'Palm Sunday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Palm_Sunday', 'prec':5, 'readings': ['Isaiah 50:4-9a', 'Philippians 2:5-11', 'Matthew 26:14-27:66 or Matthew 27:11-54 ', 'Psalm 31:9-16'] },
            -6: { 'name': 'Holy Monday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Holy_Monday', 'prec':9, 'type': 'Principal Holy Day', 'readings': ['Isaiah 42:1-9', 'Hebrews 9:11-15', 'John 12:1-11', 'Psalm 36:5-11'] },
            -5: { 'name': 'Holy Tuesday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Holy_Tuesday', 'prec':9, 'type': 'Principal Holy Day', 'readings': ['Isaiah 49:1-7', '1 Corinthians 1:18-31', 'John 12:20-36', 'Psalm 71:1-14'] },
            -4: { 'name': 'Holy Wednesday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Holy_Wednesday', 'prec':9, 'type': 'Principal Holy Day', 'readings': ['Isaiah 50:4-9a', 'Hebrews 12:1-3', 'John 13:21-32', 'Psalm 70'] },
            -3: { 'name': 'Maundy Thursday', 'colour':'white', 'url': 'https://en.wikipedia.org/wiki/Maundy_Thursday', 'prec':9, 'type': 'Principal Holy Day', 'readings': ['Exodus 12:1-14', '1 Corinthians 11:23-26', 'John 13:1-17,31b-35', 'Psalm 116:1,10-17'] },
            -2: { 'name': 'Good Friday', 'colour':'red', 'url': 'https://en.wikipedia.org/wiki/Good_Friday', 'prec':9, 'type': 'Principal Holy Day', 'readings': ['Isaiah 52:13-53:12', 'Hebrews 10:16-25', 'John 18:1-19:42', 'Psalm 22'] },
            -1: { 'name': 'Holy Saturday', 'colour':'not given', 'url': 'https://en.wikipedia.org/wiki/Holy_Saturday', 'prec':9, 'type': 'Principal Holy Day', 'readings': ['Job 14:1-14', '1 Peter 4:1-8', 'Matthew 27:57-66', 'Psalm 31:1-4,15-16'] },
            0 : { 'name': 'Easter', 'url': 'https://en.wikipedia.org/wiki/Easter', 'prec':9, 'type': 'Principal Feast'},
            # Easter Sunday’s readings are in Sundays
            #Photini is celebrated on the 4th Sunday after Easter
            28: { 'name': 'Photini', 'url': 'https://en.wikipedia.org/wiki/Samaritan_woman_at_the_well', 'source': 'https://www.instagram.com/p/DGikGvsOe4P/' },
            39: { 'name': 'Ascension', 'source': 'https://www.instagram.com/p/C6unZ-dMhtU/' },
            49: { 'name': 'Pentecost', 'source': 'https://www.instagram.com/p/C7HteatOkp3/' },
            # Pentecost (Whit Sunday)’s readings are in Sundays
            56: { 'name': 'Trinity', 'source': 'https://www.instagram.com/p/DK6tUD3ugfk/' },
            # Trinity Sunday’s readings are in Sundays
            60: { 'name': 'Corpus Christi', 'url':'https://en.wikipedia.org/wiki/Corpus_Christi_(feast)', 'prec':7, 'readings': ['Genesis 14:18-20', '1 Corinthians 11:23-26', 'John 6:51-58', 'Psalm 116:10-17'] },
        },
        'christmas': {
            '01-01': { 'name': 'The Naming and Circumcision of Jesus', 'source': 'https://www.instagram.com/p/DESTyMyu9aN/' },
            '01-02': { 'name': 'Vedanayagam Samuel Azariah', 'url': 'https://en.wikipedia.org/wiki/Vedanayagam_Samuel_Azariah', 'source': 'https://www.instagram.com/p/DEUhxUauwoG/' },
            '01-02': { 'name': 'Seraphim of Sarov', 'url': 'https://en.wikipedia.org/wiki/Seraphim_of_Sarov', 'source': 'https://www.instagram.com/p/DEaBZJYuTkc/' },
            '01-06': { 'name': 'Epiphany', 'source': 'https://www.instagram.com/p/DEe1CJYBcXG/' },
            # Figure out where "The First Sunday of Epiphany" goes because that’s actually when the next line is celebrated…
            # '01-07': { 'name': 'The Baptism of Christ', 'url': 'https://en.wikipedia.org/wiki/Baptism_of_the_Lord', 'prec':7},
            '01-10': { 'name': 'William Laud', 'source': 'https://www.instagram.com/p/DEpIIYSO4vt/'},
            '01-11': { 'name': 'Mary Slessor', 'source': 'https://www.instagram.com/p/DErs-0oO6TP/'},
            '01-13': { 'name': 'Hilary', 'source': 'https://www.instagram.com/p/DEw2kVRuIRu/' },
            '01-13': { 'name': 'Mungo', 'url': 'https://en.wikipedia.org/wiki/Saint_Mungo', 'source': 'https://www.instagram.com/p/DEzbZgNuBQO/'},
            # MLK Day is the third monday in January?!
            '01-15': { 'name': 'Martin Luther King Jr', 'url': 'https://en.wikipedia.org/wiki/Martin_Luther_King_Jr.', 'source': 'https://www.instagram.com/p/DFC4HP7OEhh/'},
            '01-17': { 'name': 'Antony of Egypt', 'source': 'https://www.instagram.com/p/DE7qGc0ON34/' },
            '01-18': { 'name': 'Confession of Peter', 'url': 'https://en.wikipedia.org/wiki/Confession_of_Peter', 'source': 'https://www.instagram.com/p/DE9ufpIhU7l/' },
            '01-19': { 'name': 'Wulfstan', 'source': 'https://www.instagram.com/p/DE_H11Oh-LQ/' },
            '01-20': { 'name': 'Sebastian and Fabian', 'url': 'https://en.wikipedia.org/wiki/Saint_Sebastian', 'source': 'https://www.instagram.com/p/DFBsm2vuBlJ/'},
            '01-21': { 'name': 'Agnes', 'source': 'https://www.instagram.com/p/DFFc4ikult2/'},
            '01-22': { 'name': 'Vincent of Saragossa', 'source': 'https://www.instagram.com/p/DFIBr6fOY-p/'},
            '01-23': { 'name': 'Phillips Brooks', 'url': 'https://en.wikipedia.org/wiki/Phillips_Brooks', 'source': 'https://www.instagram.com/p/DFKmd32uXGT/'},
            '01-24': { 'name': 'Francis de Sales', 'source': 'https://www.instagram.com/p/DFNLTghuCdU/' },
            '01-25': { 'name': 'The Conversion of Paul', 'source': 'https://www.instagram.com/p/DFRCfmghoMz/' },
            '01-26': { 'name': 'Timothy and Titus', 'source': 'https://www.instagram.com/p/DFRJZt4uvmp/' },
            '01-27': { 'name': 'Lydia, Dorcas and Phoebe', 'url': 'https://en.wikipedia.org/wiki/Lydia_of_Thyatira', 'source': 'https://www.instagram.com/p/DFU5oVeudHA/' },
            '01-28': { 'name': 'Thomas Aquinas', 'source': 'https://www.instagram.com/p/DFXefIXuk7z/' },
            '01-30': { 'name': 'Leslie Newbigin', 'url': 'https://en.wikipedia.org/wiki/Lesslie_Newbigin', 'source': 'https://www.instagram.com/p/DFaDOtKOtEs/'},
            '01-30': { 'name': 'Charles, king and martyr', 'source': 'https://www.instagram.com/p/DFcoGi2uKQi/'},
            '01-31': { 'name': 'Samuel Shoemaker', 'url': 'https://en.wikipedia.org/wiki/Samuel_Moor_Shoemaker', 'source': 'https://www.instagram.com/p/DFfM1m3OOj6/'},

            '02-01': { 'name': 'Brigid of Kildare', 'source': 'https://www.instagram.com/p/DFhxpeHhMel/'},
            '02-02': { 'name': 'Presentation of Christ at the Temple', 'source': 'https://www.instagram.com/p/DFkWcZahKzT/' },
            '02-03': { 'name': 'Anskar', 'source': 'https://www.instagram.com/p/DFm0bEzBsLe/' },
            '02-04': { 'name': 'Cornelius the Centurion', 'url': 'https://en.wikipedia.org/wiki/Cornelius_the_Centurion', 'source': 'https://www.instagram.com/p/DFp8pryOYmY/' },
            '02-06': { 'name': 'Martyrs of Japan', 'source': 'https://www.instagram.com/p/DFsHIB5uZz_/'},
            '02-08': { 'name': 'Josephine Bakhita', 'url': 'https://en.wikipedia.org/wiki/Josephine_Bakhita', 'source': 'https://www.instagram.com/p/DF0HXRROh0D/'},
            '02-10': { 'name': 'Scholastica', 'source': 'https://www.instagram.com/p/DF480AFuBOa/'},
            '02-12': { 'name': 'Lady Jane Grey','martyr': 1, 'url': 'https://en.wikipedia.org/wiki/Lady_Jane_Grey', 'source': 'https://www.instagram.com/p/C6hvd0DO7RU/'}
            '02-13': { 'name': 'Absalom Jones', 'url': 'https://en.wikipedia.org/wiki/Absalom_Jones', 'source': 'https://www.instagram.com/p/DGA3ikqOtD4/' },
            '02-14': { 'name': 'Valentine, Cyril and Methodius', 'source': 'https://www.instagram.com/p/DGDcsizOQ2x/'},
            '02-15': { 'name': 'Thomas Bray', 'source': 'https://www.instagram.com/p/DGGAZ3JO7AN/'},
            '02-17': { 'name': 'Janani Luwum', 'source': 'https://www.instagram.com/p/DGK-VX-OeHE/' },
            '02-19': { 'name': 'Lucy Yi Zhenmei, Agatha Lin Zhao and Agnes Tsao Kou Ying', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Lucy_Yi_Zhenmei', 'source': 'https://www.instagram.com/p/DGQH_eGO1j4/'},
            '02-20': { 'name': 'Frederick Douglass', 'url': 'https://en.wikipedia.org/wiki/Frederick_Douglass', 'source': 'https://www.instagram.com/p/DGSsxOCOxD4/' },
            '02-21': { 'name': 'Billy Graham', 'url': 'https://en.wikipedia.org/wiki/Billy_Graham', 'source': 'https://www.instagram.com/p/DGVRi6MujzN/'},
            '02-21': { 'name': 'Eric Lidell', 'url': 'https://en.wikipedia.org/wiki/Eric_Liddell', 'source': 'https://www.instagram.com/p/DGX2UWKBAa8/'},
            '02-23': { 'name': 'Polycarp', 'source': 'https://www.instagram.com/p/DGZIvZuBcVP/' },
            '02-27': { 'name': 'George Herbert', 'source': 'https://www.instagram.com/p/DGlFjvuu62y/' },
            '02-28': { 'name': 'John Cassian', 'url': 'https://en.wikipedia.org/wiki/John_Cassian', 'source': 'https://www.instagram.com/p/DGnk-v_u5N5/'},

            '03-01': { 'name': 'David', 'source': 'https://www.instagram.com/p/DGqPMfURwSg/' },
            '03-02': { 'name': 'Chad', 'source': 'https://www.instagram.com/p/DGrIIEQuCMF/' },
            '03-05': { 'name': 'Non', 'url': 'https://en.wikipedia.org/wiki/Saint_Non', 'source': 'https://www.instagram.com/p/DG1WqGBOfXY/'},
            '03-07': { 'name': 'Paul Cuffee', 'url': 'https://en.wikipedia.org/wiki/Paul_Cuffee_(missionary)', 'source': 'https://www.instagram.com/p/DGyH3aGpo4j/' },
            '03-07': { 'name': 'Perpetua, Felicity and companions', 'source': 'https://www.instagram.com/p/DG5NyJtuLL6/' },
            '03-08': { 'name': 'Edward King', 'url': 'https://en.wikipedia.org/wiki/Edward_King_(English_bishop)', 'prec':4, 'readings': ['Hebrews 13:1-8'] },
            '03-08': { 'name': 'Felix of Burgundy', 'url': 'https://en.wikipedia.org/wiki/Felix_of_Burgundy', 'source': 'https://www.instagram.com/p/DG75f2MhtFK/' },
            '03-09': { 'name': 'Robert Machray', 'url': 'https://en.wikipedia.org/wiki/Robert_Machray_(bishop)', 'source': 'https://www.instagram.com/p/DHCWejMOtMy/' },
            '03-09': { 'name': 'Maqhamusela Khanyile', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Maqhamusela_Khanyile', 'source': 'https://www.instagram.com/p/DG9E9FVBHYi/'},
            '03-10': { 'name': 'Harriet Tubman', 'url': 'https://en.wikipedia.org/wiki/Harriet_Tubman', 'source': 'https://www.instagram.com/p/DHBUSR1uGdr/'},
            '03-13': { 'name': 'James Theodore Holly', 'url': 'https://en.wikipedia.org/wiki/James_Theodore_Holly', 'source': 'https://www.instagram.com/p/DHIqncSu_1T/' },
            '03-17': { 'name': 'Patrick', 'source': 'https://www.instagram.com/p/DHRojzTB2ex/' },
            '03-18': { 'name': 'Cyril', 'source': 'https://www.instagram.com/p/C4p6qGLOzTw/'},
            '03-19': { 'name': 'Joseph of Nazareth', 'source': 'https://www.instagram.com/p/C4ra3V3O-9m/' },
            '03-20': { 'name': 'Cuthbert', 'source': 'https://www.instagram.com/p/C4vJ325uCF5/' },
            '03-21': { 'name': 'Thomas Cranmer', 'source': 'https://www.instagram.com/p/C4xqiSUO28D/'},
            '03-22': { 'name': 'James DeKoven', 'url': 'https://en.wikipedia.org/wiki/James_DeKoven', 'source': 'https://www.instagram.com/p/C4zErm9uhil/'}
            '03-23': { 'name': 'Gregory the Illuminator', 'url': 'https://en.wikipedia.org/wiki/Gregory_the_Illuminator', 'source': 'https://www.instagram.com/p/C43F6aQO40V/'}
            '03-24': { 'name': 'Walter Hilton of Thurgarton', 'url': 'https://en.wikipedia.org/wiki/Walter_Hilton', 'prec':3},
            '03-24': { 'name': 'Óscar Romero', 'url': 'https://en.wikipedia.org/wiki/Óscar_Romero', 'source': 'https://www.instagram.com/p/C43upVCOY05/'}
            '03-25': { 'name': 'The Annunciation of our Lord', 'source': 'https://www.instagram.com/p/C5fxTOjuVlq/' },
            '03-26': { 'name': 'Harriet Monsell', 'url': 'https://en.wikipedia.org/wiki/Harriet_Monsell', 'prec':3},
            '03-27': { 'name': 'Charles Henry Brent', 'url': 'https://en.wikipedia.org/wiki/Charles_Brent','source': 'https://www.instagram.com/p/C4_vq7kOdnb/'}
            '03-29': { 'name': 'John Keble', 'url': 'https://en.wikipedia.org/wiki/John_Keble', 'source': 'https://www.instagram.com/p/C5OGi-lOGhC/'}
            '03-31': { 'name': 'John Donne', 'source': 'https://www.instagram.com/p/C5OJnsSuML-/'},

            '04-01': { 'name': 'Frederick Denison Maurice', 'url': 'https://en.wikipedia.org/wiki/Frederick_Denison_Maurice', 'prec':3},
            '04-01': { 'name': 'Mary of Egypt', 'url': 'https://en.wikipedia.org/wiki/Mary_of_Egypt', 'source': 'https://www.instagram.com/p/C5WubupuY2B/'}
            '04-01': { 'name': 'Frederick Denison Maurice', 'url': 'https://en.wikipedia.org/wiki/F._D._Maurice', 'source': 'https://www.instagram.com/p/C5OocItuiTn/'}
            '04-02': { 'name': 'James Lloyd Breck', 'url': 'https://en.wikipedia.org/wiki/James_Lloyd_Breck', 'source': 'https://www.instagram.com/p/C5TOddZud_1/'}
            '04-02': { 'name': 'Sakachuwescum', 'url': 'https://en.wikipedia.org/wiki/Henry_Budd', 'source': 'https://www.instagram.com/p/C5QjoK-u8bm/'}
            '04-04': { 'name': 'Benedict the African', 'url': 'https://en.wikipedia.org/wiki/Benedict_the_Moor', 'source': 'https://www.instagram.com/p/C5rLSbauanm/'}
            '04-07': { 'name': 'Tikhon of Moscow', 'url': 'https://en.wikipedia.org/wiki/Patriarch_Tikhon_of_Moscow', 'source': 'https://www.instagram.com/p/C5bD9q0O7ln/'}
            '04-08': { 'name': 'William Augustus Muhlenberg', 'url': 'https://en.wikipedia.org/wiki/William_Augustus_Muhlenberg', 'source': 'https://www.instagram.com/p/C5ewjs3us-m/'}
            '04-09': { 'name': 'Dietrich Bonhoeffer', 'source': 'https://www.instagram.com/p/C5ihJhwu87l/'},
            '04-10': { 'name': 'William Law', 'source': 'https://www.instagram.com/p/C5k_MJCuTOM/' },
            '04-11': { 'name': 'George Selwyn', 'source': 'https://www.instagram.com/p/C5nvg-cu5eH/'},
            '04-12': { 'name': 'Adoniram Judson', 'url': 'https://en.wikipedia.org/wiki/Adoniram_Judson', 'source': 'https://www.instagram.com/p/C5qMqjFOZi_/'}
            '04-14': { 'name': 'Hermione of Ephesus', 'url': 'https://en.wikipedia.org/wiki/Hermione_of_Ephesus','source':'https://www.instagram.com/p/C5tLwNFu_rq/'}
            '04-15': { 'name': 'Damien of Molokai', 'url': 'https://en.wikipedia.org/wiki/Father_Damien', 'source': 'https://www.instagram.com/p/C5yJrcJgAHV/'}
            '04-16': { 'name': 'Isabella Gilmore', 'url': 'https://en.wikipedia.org/wiki/Isabella_Gilmore', 'prec':3},
            '04-17': { 'name': 'Kateri Tekakwitha', 'url': 'https://en.wikipedia.org/wiki/Kateri_Tekakwitha', 'source': 'https://www.instagram.com/p/C53ONvTO8ap/'}
            '04-19': { 'name': 'Alphege', 'source': 'https://www.instagram.com/p/C58eObhOqQ9/' },
            '04-21': { 'name': 'Anselm', 'source': 'https://www.instagram.com/p/C5_fx-DOlyp/' },
            '04-23': { 'name': 'George', 'source': 'https://www.instagram.com/p/C6G_iISOn_V/' },
            '04-23': { 'name': 'Michael Ramsay', 'url': 'https://en.wikipedia.org/wiki/Michael_Ramsey', 'source': 'https://www.instagram.com/p/C6JRaHaO4Rg/'}
            '04-24': { 'name': 'Mellitus', 'url': 'https://en.wikipedia.org/wiki/Mellitus', 'prec':3},
            '04-25': { 'name': 'Mark the Evangelist', 'source': 'https://www.instagram.com/p/C6Lv4AXLL3a/' },
            '04-27': { 'name': 'Christina Rossetti', 'source': 'https://www.instagram.com/p/C6R8pWiu7zE/'},
            '04-28': { 'name': 'Peter Chanel', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Peter_Chanel', 'prec':3},
            '04-29': { 'name': 'Catherine of Siena', 'source': 'https://www.instagram.com/p/C6V5FqUuDev/' },
            '04-30': { 'name': 'Pandita Mary Ramabai', 'source': 'https://www.instagram.com/p/C6Xs1SUOy8Z/'},

            '05-01': { 'name': 'Philip and James, Apostles', 'source': 'https://www.instagram.com/p/C6bNVOBOP02/' },
            '05-02': { 'name': 'Athanasius', 'source': 'https://www.instagram.com/p/C6d7j0OOUUl/' },
            '05-03': { 'name': 'Elisabeth Cruciger', 'url': 'https://en.wikipedia.org/wiki/Elisabeth_Cruciger', 'source': 'https://www.instagram.com/p/C6gbJRUO-bN/'}
            '05-04': { 'name': 'English Saints and Martyrs of the Reformation Era', 'prec':4},
            '05-08': { 'name': 'Julian of Norwich', 'source': 'https://www.instagram.com/p/C6tQGJ2gK6I/' },
            '05-09': { 'name': 'Pachomius the Great', 'url': 'https://en.wikipedia.org/wiki/Pachomius_the_Great', 'source': 'https://www.instagram.com/p/C6_SZOgOKbP/' }
            '05-09': { 'name': 'Gregory the Theologian', 'url': 'https://en.wikipedia.org/wiki/Gregory_of_Nazianzus', 'source': 'https://www.instagram.com/p/C6yTRucOB-p/'}
            '05-09': { 'name': 'Nikolaus Ludwig von Zinzendorf', 'url': 'https://en.wikipedia.org/wiki/Nicolaus_Zinzendorf', 'source': 'https://www.instagram.com/p/C6y6nVFOvzq/'}
            '05-12': { 'name': 'Gregory Dix', 'url': 'https://en.wikipedia.org/wiki/Gregory_Dix', 'prec':3},
            '05-14': { 'name': 'Matthias the Apostle', 'source': 'https://www.instagram.com/p/DGc_8R_Biq2/' },
            '05-16': { 'name': 'Caroline Chisholm', 'url': 'https://en.wikipedia.org/wiki/Caroline_Chisholm', 'prec':3},
            '05-15': { 'name': 'Martyrs of Sudan', 'url': 'https://en.wikipedia.org/wiki/Martyrs%27_Day', 'source': 'https://www.instagram.com/p/C7CG9U6uSap/'}
            '05-19': { 'name': 'Dunstan', 'source': 'https://www.instagram.com/p/C7HcmtXOzR_/' },
            '05-20': { 'name': 'Alcuin', 'source': 'https://www.instagram.com/p/C7KvFbEujVM/' },
            '05-21': { 'name': 'Helena', 'source': 'https://www.instagram.com/p/C7O5WvXOAiq/'},
            '05-23': { 'name': 'Nicolaus Copernicus', 'url': 'https://en.wikipedia.org/wiki/Nicolaus_Copernicus', 'source': 'https://www.instagram.com/p/C7UHUSEsMma/' },
            '05-24': { 'name': 'John and Charles Wesley', 'source': 'https://www.instagram.com/p/DGvTqkTOuP5/' },
            '05-24': { 'name': 'Jackson Kemper', 'url': 'https://en.wikipedia.org/wiki/Jackson_Kemper', 'source': 'https://www.instagram.com/p/C7WdJMUOVQB/'},
            '05-24': { 'name': 'Vincent of Lérins', 'url': 'https://en.wikipedia.org/wiki/Vincent_of_Lérins', 'source': 'https://www.instagram.com/p/C7PgifHvLcv/'}
            '05-25': { 'name': 'The Venerable Bede', 'source': 'https://www.instagram.com/p/C7Y-VDaOEMd/'},
            '05-26': { 'name': 'Augustine of Canterbury', 'source': 'https://www.instagram.com/p/C7Z6AG1OWHy/' },
            '05-26': [ 'name': 'John Calvin', 'url': 'https://en.wikipedia.org/wiki/John_Calvin', 'source': 'https://www.instagram.com/p/C7eAv7vutcP/']
            '05-28': { 'name': 'Lanfranc', 'url': 'https://en.wikipedia.org/wiki/Lanfranc', 'prec':3},
            '05-30': { 'name': 'Josephine Butler', 'source': 'https://www.instagram.com/p/C7l3MIdO0D6/' },
            '05-30': { 'name': 'Joan of Arc', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Joan_of_Arc', 'source': 'https://www.instagram.com/p/C7gpAXZOmcp/' },
            '05-31': { 'name': 'The Visit of the Blessed Virgin Mary to Elizabeth', 'source': 'https://www.instagram.com/p/C7ooTuvMrFp/' },

            '06-01': { 'name': 'Justin', 'source': 'https://www.instagram.com/p/C7rG8tju855/' },
            '06-01': { 'name': 'Nicomedes', 'martyr': 1, 'url': 'https://www.instagram.com/p/C75aCiJMiOg/', 'source': 'https://www.instagram.com/p/C75aCiJMiOg/'},
            '06-02': { 'name': 'Blandina', 'martyr': 1, 'url': 'https://en.wikipedia.org/wiki/Blandina', 'source': 'https://www.instagram.com/p/C7vNsF5OPhh/'},
            '06-03': { 'name': 'Martyrs of Uganda', 'source': 'https://www.instagram.com/p/C7wSr4vugXT/'},
            '06-04': { 'name': 'Petroc', 'url': 'https://en.wikipedia.org/wiki/Saint_Petroc', 'prec':3},
            '06-04': { 'name': 'John XXIII', 'url': 'https://en.wikipedia.org/wiki/Pope_John_XXIII', 'source': 'https://www.instagram.com/p/C7zBfUVO0F1/'}
            '06-05': { 'name': 'Boniface', 'source': 'https://www.instagram.com/p/C71cN4PuIWy/' },
            '06-06': { 'name': 'Ini Kopuria', 'source': 'https://www.instagram.com/p/C734kJPORaY/'},
            '06-08': { 'name': 'Thomas Ken', 'source': 'https://www.instagram.com/p/C79Gb_CuDtQ/' },
            '06-09': { 'name': 'Columba', 'source': 'https://www.instagram.com/p/C7-Vc03uDYF/' },
            '06-10': { 'name': 'Ephrem of Syria', 'source': 'https://www.instagram.com/p/C8B-53KuQfr/'},
            '06-11': { 'name': 'Barnabas the Apostle', 'source': 'https://www.instagram.com/p/C8EqlG9uKvc/' },
            '06-12': { 'name': 'Enmegahbowh', 'url': 'https://en.wikipedia.org/wiki/Enmegahbowh', 'source': 'https://www.instagram.com/p/C8HgRsUOPT1/'},
            '06-13': { 'name': 'Anthony of Padua', 'url': 'https://en.wikipedia.org/wiki/Anthony_of_Padua', 'source': 'https://www.instagram.com/p/DK2BzgCMHSi/'}
            '06-14': { 'name': 'Richard Baxter', 'source': 'https://www.instagram.com/p/DDTJSdHMEwV/'},
            '06-14': { 'name': 'Gilbert Keith Chesterton', 'url': 'https://en.wikipedia.org/wiki/G._K._Chesterton', 'source': 'https://www.instagram.com/p/C8URscFOjou/'},
            '06-14': { 'name': 'Basil the Great', 'url': 'https://en.wikipedia.org/wiki/Basil_of_Caesarea', 'source': 'https://www.instagram.com/p/C8MakrWOAwo/'},
            '06-15': { 'name': 'Evelyn Underhill', 'source': 'https://www.instagram.com/p/C8PcY3tueKy/'},
            '06-16': { 'name': 'Richard of Chichester', 'url': 'https://en.wikipedia.org/wiki/Richard_of_Chichester', 'prec':4, 'readings': ['John 21:15-19'] },
            '06-17': { 'name': 'Samuel and Henrietta Barnett', 'url': 'https://en.wikipedia.org/wiki/Samuel_Augustus_Barnett', 'prec':3},
            '06-18': { 'name': 'Bernard Mizeki', 'url': 'https://en.wikipedia.org/wiki/Bernard_Mizeki', 'prec':3},
            '06-19': { 'name': 'Sundar Singh', 'url': 'https://en.wikipedia.org/wiki/Sadhu_Sundar_Singh', 'prec':3},
            '06-20': { 'name': 'Methodius of Olympus', 'martyr': 1, 'url': 'https://en.wikipedia.org/wiki/Methodius_of_Olympus', 'source': 'https://www.instagram.com/p/DLIxtwYSrto/'}
            '06-22': { 'name': 'Alban', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Alban', 'source': 'https://www.instagram.com/p/C8hTgt0uaqZ/' },
            '06-23': { 'name': 'Etheldreda', 'url': 'https://en.wikipedia.org/wiki/%C3%86thelthryth', 'prec':4, 'readings': ['Matthew 25:1-13'] },
            '06-24': { 'name': 'The Birth of John the Baptist', 'url': 'https://en.wikipedia.org/wiki/Nativity_of_St._John_the_Baptist', 'source': 'https://www.instagram.com/p/C8mVoTyutpy/' },
            '06-27': { 'name': 'Cyril', 'url': 'https://en.wikipedia.org/wiki/Cyril_of_Alexandria', 'source': 'https://www.instagram.com/p/C8uHbkQOO4U/'},
            '06-28': { 'name': 'Irenaeus', 'url': 'https://en.wikipedia.org/wiki/Irenaeus', 'source': 'https://www.instagram.com/p/C8wuSHFOeym/'},
            '06-29': { 'name': 'Peter and Paul, Apostles', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Peter', 'source': 'https://www.instagram.com/p/C8zK37uOFU2/' },
            '06-29': { 'name': 'Samuel Ajayi Crowther', 'url': 'https://en.wikipedia.org/wiki/Samuel_Ajayi_Crowther', 'source': 'https://www.instagram.com/p/C8fJee3J1xc/' },

            '07-01': { 'name': 'Henry, John, and Henry Venn', 'url': 'https://en.wikipedia.org/wiki/Henry_Venn_(Clapham_Sect)', 'prec':3},
            '07-02': { 'name': 'Moses the Black', 'url': 'https://en.wikipedia.org/wiki/Moses_the_Black', 'source': 'https://www.instagram.com/p/C86ycK7OFaD/'},
            '07-03': { 'name': 'Thomas the Apostle', 'source': 'https://www.instagram.com/p/DD13TBKuOPH/' },
            '07-05': { 'name': 'Princess Elisabeth of Hesse and by Rhine', 'url': 'https://en.wikipedia.org/wiki/Princess_Elisabeth_of_Hesse_and_by_Rhine', 'source': 'https://www.instagram.com/p/C9CyArjMBGi/'},
            '07-06': { 'name': 'Thomas More and John Fisher', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Thomas_More', 'source': 'https://www.instagram.com/p/C9FB1VuOCDl/'},
            '07-06': { 'name': 'Jan Hus', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Jan_Hus', 'source': 'https://www.instagram.com/p/C9F76BIO6cY/'},
            '07-11': { 'name': 'Benedict', 'url': 'https://en.wikipedia.org/wiki/Benedict_of_Nursia', 'source': 'https://www.instagram.com/p/C9SCzzzO589/' },
            '07-12': { 'name': 'Nathan Soderblom', 'url': 'https://en.wikipedia.org/wiki/Nathan_Soderblom', 'source': 'https://www.instagram.com/p/C9UrbQaOOed/'},
            '07-13': { 'name': 'Laurence C. Jones', 'url': 'https://en.wikipedia.org/wiki/Laurence_C._Jones', 'source': 'https://www.instagram.com/p/C9SCzzzO589/' },
            '07-14': { 'name': 'John Keble', 'url': 'https://en.wikipedia.org/wiki/John_Keble', 'prec':4, 'readings': ['Lamentations 3:19-26', 'Matthew 5:1-8'] },
            '07-15': { 'name': 'Swithun', 'url': 'https://en.wikipedia.org/wiki/Swithun', 'prec':4, 'readings': ['James 5:7-11,13-18'] },
            '07-15': { 'name': 'Bonaventure', 'url': 'https://en.wikipedia.org/wiki/Bonaventure', 'source': 'https://www.instagram.com/p/C9YEJVVhC2b/' },
            '07-15': { 'name': 'St Olga and St Vladimir', 'url': 'https://en.wikipedia.org/wiki/Vladimir_the_Great', 'source': 'https://www.instagram.com/p/C9cYHsruqVq/' },
            '07-16': { 'name': 'Osmund', 'url': 'https://en.wikipedia.org/wiki/Saint_Osmund', 'prec':3},
            '07-17': { 'name': 'William White', 'url': 'https://en.wikipedia.org/wiki/William_White_(bishop)', 'source': 'https://www.instagram.com/p/C9hqPG9ubXn/'},
            '07-18': { 'name': 'Elizabeth Ferard', 'url': 'https://en.wikipedia.org/wiki/Elizabeth_Ferard', 'prec':3},
            '07-19': { 'name': 'Gregory, and his sister Macrina', 'url': 'https://en.wikipedia.org/wiki/Gregory_of_Nyssa', 'source': 'https://www.instagram.com/p/C9nP1j7OpU_/' },
            '07-19': { 'name': 'Macrina', 'url': 'https://en.wikipedia.org/wiki/Macrina_the_Younger', 'source': 'https://www.instagram.com/p/C9kDOMwuFAQ/' },
            '07-20': { 'name': 'Margaret of Antioch', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Margaret_the_Virgin', 'source': 'https://www.instagram.com/p/C9pdsLNuVqz/'},
            '07-22': { 'name': 'Mary Magdalene', 'url': 'https://en.wikipedia.org/wiki/Mary_Magdalene', 'source': 'https://www.instagram.com/p/C9uKPZfuunw/' },
            '07-23': { 'name': 'Bridget', 'url': 'https://en.wikipedia.org/wiki/Bridget_of_Sweden', 'prec':3},
            '07-24': { 'name': 'Thomas á Kempis', 'url': 'https://en.wikipedia.org/wiki/Thomas_a_Kempis', 'source': 'https://www.instagram.com/p/C9zqu8dONx0/'},
            '07-25': { 'name': 'Christopher', 'martyr': 1, 'url': 'https://en.wikipedia.org/wiki/Saint_Christopher', 'source': 'https://www.instagram.com/p/C9svUIqOzCI/' },
            '07-25': { 'name': 'James the Apostle', 'url': 'https://en.wikipedia.org/wiki/James,_son_of_Zebedee', 'source': 'https://www.instagram.com/p/C92LnIWuGt2/' },
            '07-26': { 'name': 'Parents of the Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Saint_Anne', 'source': 'https://www.instagram.com/p/C93kRcjusCw/' },
            '07-27': { 'name': 'Brooke Foss Westcott', 'url': 'https://en.wikipedia.org/wiki/Brooke_Foss_Westcott', 'prec':3},
            '07-27': { 'name': 'William Reed Huntington', 'url': 'https://en.wikipedia.org/wiki/William_Reed_Huntington', 'source': 'https://www.instagram.com/p/C97f_s-OiOg/'},
            '07-28': { 'name': 'Johann Sebastian Bach', 'url': 'https://en.wikipedia.org/wiki/Johann_Sebastian_Bach', 'source': 'https://www.instagram.com/p/C98Sev-BZow/'},
            '07-29': { 'name': 'Mary, Martha and Lazarus', 'url': 'https://en.wikipedia.org/wiki/Mary,_sister_of_Lazarus', 'source': 'https://www.instagram.com/p/C-ALuUzupd9/' },
            '07-30': { 'name': 'William Wilberforce', 'url': 'https://en.wikipedia.org/wiki/William_Wilberforce', 'source': 'https://www.instagram.com/p/C-C1vfVB8rw/' },
            '07-31': { 'name': 'Ignatius of Loyola', 'url': 'https://en.wikipedia.org/wiki/Ignatius_of_Loyola', 'source': 'https://www.instagram.com/p/C-Fz7WLOtPC/'},

            '08-04': { 'name': 'Jean-Baptiste Vianney', 'url': 'https://en.wikipedia.org/wiki/Jean_Vianney', 'prec':3},
            '08-05': { 'name': 'Oswald', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Oswald_of_Northumbria', 'source': 'https://www.instagram.com/p/C-SM68kOD1S/' },
            '08-06': { 'name': 'The Transfiguration of Our Lord', 'source': 'https://www.instagram.com/p/C-T4E4Kuc54/' },
            '08-07': { 'name': 'John Mason Neale', 'url': 'https://en.wikipedia.org/wiki/John_Mason_Neale', 'source': 'https://www.instagram.com/p/C-WaZW8uoqf/'},
            '08-08': { 'name': 'Dominic', 'url': 'https://en.wikipedia.org/wiki/Saint_Dominic', 'source': 'https://www.instagram.com/p/C-aw9B1OMNW/' },
            '08-09': { 'name': 'Mary Sumner', 'url': 'https://en.wikipedia.org/wiki/Mary_Sumner', 'source': 'https://www.instagram.com/p/C-coZ74OiQC/' },
            '08-09': { 'name': 'Edith Stein', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Edith_Stein', 'source': 'https://www.instagram.com/p/C-udwOnOQBk/' },
            '08-10': { 'name': 'Laurence', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Lawrence_of_Rome', 'source': 'https://www.instagram.com/p/C-fkzhuuszt/' },
            '08-11': { 'name': 'Clare', 'url': 'https://en.wikipedia.org/wiki/Clare_of_Assisi', 'source': 'https://www.instagram.com/p/C-gPXmxhX4q/' },
            '08-12': { 'name': 'Charles Inglis', 'url': 'https://en.wikipedia.org/wiki/Charles_Inglis_(bishop)', 'source': 'https://www.instagram.com/p/C-kShlpusHJ/'},
            '08-13': { 'name': 'Jeremy Taylor', 'url': 'https://en.wikipedia.org/wiki/Jeremy_Taylor', 'source': 'https://www.instagram.com/p/C-m9BsZOdAq/' },
            '08-14': { 'name': 'Maximilian Kolbe', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Maximilian_Kolbe', 'source': 'https://www.instagram.com/p/C-xQ8GpuSR8/'},
            '08-14': { 'name': 'Jonathan Myrick Daniels', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Jonathan_Myrick_Daniels', 'source': 'https://www.instagram.com/p/C-7jf6fO_wo/'},
            '08-15': { 'name': 'The Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Blessed_Virgin_Mary', 'source': 'https://www.instagram.com/p/C-sJUIRuBAY/'},
            '08-16': { 'name': 'Roger Schutz', 'url': 'https://en.wikipedia.org/wiki/Roger_Schutz', 'source': 'https://www.instagram.com/p/C-pjiwOOxQu/'},
            '08-20': { 'name': 'Bernard', 'url': 'https://en.wikipedia.org/wiki/Bernard_of_Clairvaux', 'source': 'https://www.instagram.com/p/C-47xY7Ondc/' },
            '08-24': { 'name': 'Bartholomew the Apostle', 'url': 'https://en.wikipedia.org/wiki/Bartholomew_the_Apostle', 'source': 'https://www.instagram.com/p/C_DUZezuoKA/'},
            '08-25': { 'name': 'Louis', 'url': 'https://en.wikipedia.org/wiki/Louis_of_France', 'source': 'https://www.instagram.com/p/C_E8jbUu3UO/'},
            '08-27': { 'name': 'Monica', 'url': 'https://en.wikipedia.org/wiki/Monica_of_Hippo', 'source': 'https://www.instagram.com/p/C_LF_BrOJWY/' },
            '08-27': { 'name': 'Simeon Bachos', 'url': 'https://en.wikipedia.org/wiki/Ethiopian_eunuch', 'source': 'https://www.instagram.com/p/C_G86kWS_rn/'}
            '08-28': { 'name': 'Augustine', 'url': 'https://en.wikipedia.org/wiki/Augustine_of_Hippo', 'source': 'https://www.instagram.com/p/C_Nm_oDulTa/' },
            '08-29': { 'name': 'The Beheading of John the Baptist', 'url': 'https://en.wikipedia.org/wiki/John_the_Baptist', 'source': 'https://www.instagram.com/p/C_P-y0COnxc/' },
            '08-30': { 'name': 'John Bunyan', 'url': 'https://en.wikipedia.org/wiki/John_Bunyan', 'source': 'https://www.instagram.com/p/C_dMqaXuDs8/' },
            '08-30': { 'name': 'Charles Chapman Grafton', 'url': 'https://en.wikipedia.org/wiki/Charles_Chapman_Grafton', 'source': 'https://www.instagram.com/p/C_SjjfpO-PZ/' },
            '08-31': { 'name': 'Aidan', 'url': 'https://en.wikipedia.org/wiki/Aidan_of_Lindisfarne', 'source': 'https://www.instagram.com/p/C_Wav_iOSSo/' },
            '08-31': { 'name': 'Joseph of Arimathea', 'url': 'https://en.wikipedia.org/wiki/Joseph_of_Arimathea', 'source': 'https://www.instagram.com/p/C-IRmZ0uNW_/' },

            '09-01': { 'name': 'Giles of Provence', 'url': 'https://en.wikipedia.org/wiki/Saint_Giles', 'source': 'https://www.instagram.com/p/C_Y3GSZy7kx/'},
            '09-02': { 'name': 'The Martyrs of Papua New Guinea', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Martyrs_of_Papua_New_Guinea', 'source': 'https://www.instagram.com/p/C_aXTofuOwi/'},
            '09-03': { 'name': 'Gregory the Great', 'source': 'https://www.instagram.com/p/DHGF09gBoxn/' },
            '09-04': { 'name': 'Birinus', 'url': 'https://en.wikipedia.org/wiki/Birinus', 'source': 'https://www.instagram.com/p/C_flWSbuql8/'},
            '09-05': { 'name': 'Mother Teresa of Calcutta', 'url': 'https://en.wikipedia.org/wiki/Mother_Teresa', 'source': 'https://www.instagram.com/p/C_iMniSOHGq/'},
            '09-06': { 'name': 'Allen Gardiner', 'url': 'https://en.wikipedia.org/wiki/Allen_Gardiner', 'prec':3},
            '09-06': { 'name': 'Hannah More', 'url': 'https://en.wikipedia.org/wiki/Hannah_More', 'source': 'https://www.instagram.com/p/C_ni3-NuGp1/'},
            '09-07': { 'name': 'Evertius of Orléans', 'url': 'https://en.wikipedia.org/wiki/Euverte_d%27Orléans', 'source': 'https://www.instagram.com/p/C_tRSn2uiwy/'}
            '09-08': { 'name': 'The Birth of the Blessed Virgin Mary', 'url': 'https://en.wikipedia.org/wiki/Nativity_of_Mary', 'prec':4, 'readings': ['Ruth 4:13-16', 'James 1:17-18', 'Luke 8:19-21'] },
            '09-09': { 'name': 'Charles Fuge Lowder', 'url': 'https://en.wikipedia.org/wiki/Charles_Fuge_Lowder', 'prec':3},
            '09-09': { 'name': 'Constance and Her Companions', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/St._Mary%27s_Episcopal_Cathedral_(Memphis,_Tennessee)', 'source': 'https://www.instagram.com/p/C_sRKc3Oij0/'},
            '09-10': { 'name': 'Alexander Crummell', 'url': 'https://en.wikipedia.org/wiki/Alexander_Crummell', 'source': 'https://www.instagram.com/p/C_vGwjnuZkA/'},
            '09-12': { 'name': 'John Henry Hobart', 'url': 'https://en.wikipedia.org/wiki/John_Henry_Hobart', 'source': 'https://www.instagram.com/p/C_0Va3kuhCE/'},
            '09-13': { 'name': 'John Chrysostom', 'url': 'https://en.wikipedia.org/wiki/John_Chrysostom', 'source': 'https://www.instagram.com/p/C_2_cj1u3hg/' },
            '09-14': { 'name': 'Holy Cross Day', 'url': 'https://en.wikipedia.org/wiki/Feast_of_the_Cross', 'source': 'https://www.instagram.com/p/C_5LfGUO4hB/' },
            '09-15': { 'name': 'Cyprian, Bishop of Carthage', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Cyprian', 'source': 'https://www.instagram.com/p/C_6d6f_hGSC/' },
            '09-16': { 'name': 'Ninian', 'url': 'https://en.wikipedia.org/wiki/Saint_Ninian', 'source': 'https://www.instagram.com/p/C_-mdf9uWcI/' },
            '09-16': { 'name': 'Edward Bouverie Pusey', 'url': 'https://en.wikipedia.org/wiki/Edward_Bouverie_Pusey', 'source': 'https://www.instagram.com/p/DACJbuIBSFP/'},
            '09-17': { 'name': 'Hildegard', 'url': 'https://en.wikipedia.org/wiki/Hildegard_of_Bingen', 'source': 'https://www.instagram.com/p/DATHKHpOqES/' },
            '09-19': { 'name': 'Theodore', 'url': 'https://en.wikipedia.org/wiki/Theodore_of_Tarsus', 'source': 'https://www.instagram.com/p/DADyZdnuQom/'},
            '09-20': { 'name': 'John Coleridge Patteson and companions', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/John_Coleridge_Patteson', 'source': 'https://www.instagram.com/p/DAI8hwyOHnB/' },
            '09-20': { 'name': 'Andrew Kim Taegon', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Andrew_Kim_Taegon', 'source': https://www.instagram.com/p/C7jW99EOmfT/' },
            '09-21': { 'name': 'Matthew the Evangelist', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Matthew_the_Evangelist', 'source': 'https://www.instagram.com/p/DALnkyrO0HM/'},
            '09-25': { 'name': 'Lancelot Andrewes', 'url': 'https://en.wikipedia.org/wiki/Lancelot_Andrewes', 'source': 'https://www.instagram.com/p/DAYhUEBOLtM/' },
            '09-25': { 'name': 'Sergius of Radonezh', 'url': 'https://en.wikipedia.org/wiki/Serge_of_Radonezh', 'source': 'https://www.instagram.com/p/DAVhlDNOWJQ/'},
            '09-26': { 'name': 'Wilson Carlile', 'url': 'https://en.wikipedia.org/wiki/Wilson_Carlile', 'source': 'https://www.instagram.com/p/DAbcjF8uzq9/''},
            '09-27': { 'name': 'Vincent de Paul', 'url': 'https://en.wikipedia.org/wiki/Vincent_de_Paul', 'prec':4, 'readings': ['1 Corinthians 1:25-end', 'Matthew 25:34-40'] },
            '09-29': { 'name': 'Michael and All Angels', 'url': 'https://en.wikipedia.org/wiki/Michaelmas', 'source': 'https://www.instagram.com/p/DAedlnTO7kK/' },
            '09-30': { 'name': 'Jerome', 'url': 'https://en.wikipedia.org/wiki/St._Jerome', 'source': 'https://www.instagram.com/p/DAiV5ZzuQit/'},

            '10-01': { 'name': 'Thérèse of Lisieux', 'url': 'https://en.wikipedia.org/wiki/Therese_of_Lisieux', 'source': 'https://www.instagram.com/p/DBKJ0H6h76c/' },
            '10-01': { 'name': 'Remigius', 'url': 'https://en.wikipedia.org/wiki/Saint_Remigius', 'source': 'https://www.instagram.com/p/DAlVMZvujVZ/'},
            '10-01': { 'name': 'Anthony Ashley Cooper', 'url': 'https://en.wikipedia.org/wiki/Anthony_Ashley-Cooper,_7th_Earl_of_Shaftesbury', 'source': 'https://www.instagram.com/p/DAdjWyYuViy/' },
            '10-03': { 'name': 'George Bell', 'url': 'https://en.wikipedia.org/wiki/George_Bell_(bishop)', 'source': 'https://www.instagram.com/p/DAqZDzXOsCe/'},
            '10-04': { 'name': 'Francis of Assisi', 'url': 'https://en.wikipedia.org/wiki/Francis_of_Assisi', 'source': 'https://www.instagram.com/p/DAs6bPPOBt7/' },
            '10-06': { 'name': 'William Tyndale', 'url': 'https://en.wikipedia.org/wiki/William_Tyndale', 'source': 'https://www.instagram.com/p/DAwiFZUhQbZ/' },
            '10-09': { 'name': 'Robert Grosseteste', 'url': 'https://en.wikipedia.org/wiki/Robert_Grosseteste', 'source': 'https://www.instagram.com/p/DA5vFkMxYDd/'},
            '10-10': { 'name': 'Paulinus', 'url': 'https://en.wikipedia.org/wiki/Paulinus_of_York', 'source': 'https://www.instagram.com/p/DA8n496upKc/' },
            '10-11': { 'name': 'Ethelburga', 'url': 'https://en.wikipedia.org/wiki/Ethelburga_of_Barking', 'prec':3},
            '10-11': { 'name': 'Philip the Deacon', 'url': 'https://en.wikipedia.org/wiki/Philip_the_Evangelist', 'source': 'https://www.instagram.com/p/DA_BZe9uq4k/' },
            '10-12': { 'name': 'Wilfrid', 'url': 'https://en.wikipedia.org/wiki/Wilfrid', 'prec':4, 'readings': ['Luke 5:1-11', '1 Corinthians 1:18-25'] },
            '10-12': { 'name': 'Cecil Frances Alexander', 'url': 'https://en.wikipedia.org/wiki/Cecil_Frances_Alexander', 'source': 'https://www.instagram.com/p/DBBozi-OZq9/'},
            '10-13': { 'name': 'Edward the Confessor', 'url': 'https://en.wikipedia.org/wiki/Edward_the_Confessor', 'source': 'https://www.instagram.com/p/DBCi1RPBYZx/' },
            '10-15': { 'name': 'Samuel Isaac Joseph Schereschewsky', 'url': 'https://en.wikipedia.org/wiki/Samuel_Schereschewsky', 'source': 'https://www.instagram.com/p/DBGhc1ou0vz/'},
            '10-15': { 'name': 'Teresa of Avila', 'url': 'https://en.wikipedia.org/wiki/Teresa_of_%C3%81vila', 'source': 'https://www.instagram.com/p/DBJPCOmO0gy/' },
            '10-16': { 'name': 'Nicholas Ridley and Hugh Latimer', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Nicholas_Ridley_(martyr)', 'source': 'https://www.instagram.com/p/DBLyc0rudbw/' },
            '10-17': { 'name': 'Ignatius', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Ignatius_of_Antioch', 'source': 'https://www.instagram.com/p/DBOPf9oOj4s/'},
            '10-18': { 'name': 'Luke the Evangelist', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Luke_the_Evangelist', 'source': 'https://www.instagram.com/p/DBQ-ok6uuCK/' },
            '10-19': { 'name': 'Henry Martyn', 'url': 'https://en.wikipedia.org/wiki/Henry_Martyn', 'source': 'https://www.instagram.com/p/DBTkKbHOjXU/' },
            '10-21': { 'name': 'Esther John', 'martyr': 1, 'url': 'https://en.wikipedia.org/wiki/Esther_John', 'source': 'https://www.instagram.com/p/DBaBhJLuYLL/'},
            '10-23': { 'name': 'James of Jerusalem', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/James_the_Just', 'source': 'https://www.instagram.com/p/DBeB9AzOBPy/' },
            '10-24': { 'name': 'Hiram Hisanori Kano', 'url': 'https://en.wikipedia.org/wiki/Hiram_Kano', 'source': 'https://www.instagram.com/p/DBgexrAuUOt/'},
            '10-25': { 'name': 'Crispin and Crispinian', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Crispin', 'source': 'https://www.instagram.com/p/DBjcDinuDDn/'},
            '10-26': { 'name': 'Alfred the Great', 'url': 'https://en.wikipedia.org/wiki/Alfred_the_Great', 'source': 'https://www.instagram.com/p/DBl9dT1uEAw/' },
            '10-28': { 'name': 'Simon and Jude, Apostles', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Simon_the_Zealot', 'source': 'https://www.instagram.com/p/DBrP1xhu7R4/' },
            '10-29': { 'name': 'James Hannington', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/James_Hannington', 'source': 'https://www.instagram.com/p/DBtcg9OuOTa/' },
            '10-30': { 'name': 'John Wyclif', 'url': 'https://en.wikipedia.org/wiki/John_Wycliffe', 'source': 'https://www.instagram.com/p/DBvhNauvVpK/' },
            '10-31': { 'name': 'Martin Luther', 'source': 'https://www.instagram.com/p/DGNjM5juUmt/' },
            '10-31': { 'name': 'All Hallows Eve', 'source': 'https://www.instagram.com/p/DByGCxxBSZV/' },

            # All Saints’ Sunday? Has an A B C reading
            '11-01': { 'name': 'All Saints', 'url': 'https://en.wikipedia.org/wiki/All_Saints%27_Day', 'prec':9, 'type': 'Principal Feast'},
            '11-02': { 'name': 'All Souls', 'url': 'https://en.wikipedia.org/wiki/All_Souls%27_Day', 'colour':'purple', 'prec':4, 'readings': ['Lamentations 3:17–26, 31–33', 'Psalm 23 or Psalm 27:1–6,16,17', 'Romans 5:5–11 or 1 Peter 1:3–9', 'John 5:19–25 or John 6:37–40' ], 'source': 'https://www.instagram.com/p/DB4EEpcOb0A/'},
            '11-03': { 'name': 'Richard Hooker', 'url': 'https://en.wikipedia.org/wiki/Richard_Hooker', 'prec':4, 'readings': ['John 16:12-15', 'Ecclesiasticus 44:10-15'], 'source': 'https://www.instagram.com/p/DB4n6E_hAJA/' },
            '11-03': { 'name': 'Martin of Porres', 'url': 'https://en.wikipedia.org/wiki/Saint_Martin_de_Porres', 'source': 'https://www.instagram.com/p/DB7Rn0NBtLB/'},
            '11-06': { 'name': 'Leonard', 'url': 'https://en.wikipedia.org/wiki/Leonard_of_Noblac', 'prec':3},
            '11-06': { 'name': 'William Temple', 'url': 'https://en.wikipedia.org/wiki/William_Temple_(archbishop)', 'source': 'https://www.instagram.com/p/DCBpm8MOLwI/' },
            '11-07': { 'name': 'Willibrord', 'url': 'https://en.wikipedia.org/wiki/Willibrord', 'prec':4, 'readings': ['Isaiah 52:7-10', 'Matthew 28:16-end'], 'source': 'https://www.instagram.com/p/DCEdp0IOINa/' },
            '11-08': { 'name': 'The Saints and Martyrs of England', 'prec':4, 'readings': ['Isaiah 61.4–9', 'Psalm 15', 'Revelation 19:5–10', 'John 17:18–23'] },
            '11-09': { 'name': 'Margery Kempe', 'url': 'https://en.wikipedia.org/wiki/Margery_Kempe', 'prec':3, 'source': 'https://www.instagram.com/p/DCH6zjIh6CG/'},
            '11-10': { 'name': 'Leo the Great', 'url': 'https://en.wikipedia.org/wiki/Pope_Leo_I', 'prec':4, 'readings': ['1 Peter 5:1-11'], 'source': 'https://www.instagram.com/p/DCLGCz_PnG9/' },
            '11-11': { 'name': 'Martin', 'url': 'https://en.wikipedia.org/wiki/Martin_of_Tours', 'prec':4, 'readings': ['1 Thessalonians 5:1-11', 'Matthew 25:34-40'], 'source': 'https://www.instagram.com/p/DCPD0rIOph4/' },
            '11-13': { 'name': 'Charles Simeon', 'url': 'https://en.wikipedia.org/wiki/Charles_Simeon', 'prec':4, 'readings': ['Malachi 2:5-7', 'Colossians 1:3-8', 'Luke 8:4-8'], 'source': 'https://www.instagram.com/p/DCSpiCduZqN/' },
            '11-14': { 'name': 'Samuel Seabury', 'url': 'https://en.wikipedia.org/wiki/Samuel_Seabury_(1729%E2%80%931796)', 'prec':3, 'source': 'https://www.instagram.com/p/DCVZ-mburAO/'},
            '11-15': { 'name': 'Herman of Alaska', 'url': 'https://en.wikipedia.org/wiki/Herman_of_Alaska', 'source': 'https://www.instagram.com/p/DCYC1dVOnKa/'},
            '11-16': { 'name': 'Margaret', 'url': 'https://en.wikipedia.org/wiki/Saint_Margaret_of_Scotland', 'prec':4, 'readings': ['Proverbs 31:10-12,20,26-end', '1 Corinthians 12:13–13:3', 'Matthew 25:34-end'], 'source': 'https://www.instagram.com/p/DCapbKruU3N/' },
            '11-17': { 'name': 'Hugh', 'url': 'https://en.wikipedia.org/wiki/Hugh_of_Lincoln', 'prec':4, 'readings': ['1 Timothy 6:11-16'], 'source': 'https://www.instagram.com/p/DCdOwuBOlGU/' },
            '11-18': { 'name': 'Elizabeth', 'url': 'https://en.wikipedia.org/wiki/Elisabeth_of_Hungary', 'prec':4, 'readings': ['Matthew 25:31-end', 'Proverbs 31:10-end'], 'source': 'https://www.instagram.com/p/DCgzO93OgvN/' },
            '11-19': { 'name': 'Hilda', 'url': 'https://en.wikipedia.org/wiki/Hilda_of_Whitby', 'prec':4, 'readings': ['Isaiah 61:10–62:5'], 'source': 'https://www.instagram.com/p/DCjnTtGOCKh/' },
            '11-20': { 'name': 'Edmund', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Edmund_the_Martyr', 'prec':4, 'readings': ['Proverbs 20:28', 'Proverbs 21:1-4,7'], 'source': 'https://www.instagram.com/p/DCmABk_ORKn/' },
            '11-22': { 'name': 'Cecilia', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Cecilia_(saint)', 'prec':3, 'source': 'https://www.instagram.com/p/DCrs-pLvjcm/'},
            '11-22': { 'name': 'C.S. Lewis', 'url': 'https://en.wikipedia.org/wiki/C._S._Lewis', 'source': 'https://www.instagram.com/p/DC72rGlOxE2/' },
            '11-23': { 'name': 'Clement of Rome', 'source': 'https://www.instagram.com/p/DCs27HCuDQc/' },
            '11-24': { 'name': 'Barbara', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Saint_Barbara', 'source': 'https://www.instagram.com/p/DCzef9hPO1h/'},
            '11-25': { 'name': 'Catherine', 'martyr':1, 'url': 'https://en.wikipedia.org/wiki/Catherine_of_Alexandria', 'prec':3, 'source': 'https://www.instagram.com/p/DCxjbPrus8E/'},
            '11-25': { 'name': 'Isaac Watts', 'url': 'https://en.wikipedia.org/wiki/Isaac_Watts', 'source': 'https://www.instagram.com/p/DC38BELuRBg/'},
            '11-26': { 'name': 'Sojourner Truth', 'url': 'https://en.wikipedia.org/wiki/Sojourner_Truth', 'source': 'https://www.instagram.com/p/DC1XbcIuYTV/'},
            '11-29': { 'name': 'Dorothy Day', 'url': 'https://en.wikipedia.org/wiki/Dorothy_Day', 'source': 'https://www.instagram.com/p/DC72rGlOxE2/' },
            '11-30': { 'name': 'Andrew the Apostle', 'url': 'https://en.wikipedia.org/wiki/Saint_Andrew', 'prec':7, 'readings': ['Isaiah 52:7-10', 'Psalm 19:1-6', 'Romans 10:12-18', 'Matthew 4:18-22'], 'source': 'https://www.instagram.com/p/DC_jj-Juut3/' },

            '12-01': { 'name': 'Charles de Foucauld', 'url': 'https://en.wikipedia.org/wiki/Charles_de_Foucauld', 'prec':3},
            '12-02': { 'name': 'Channing Moore Williams', 'url': 'https://en.wikipedia.org/wiki/Channing_Moore_Williams', 'source': 'https://www.instagram.com/p/DDFAVfsO46P/'},
            '12-03': { 'name': 'Francis Xavier', 'source': 'https://www.instagram.com/p/DDHd3hgulqk/'},
            '12-04': { 'name': 'John of Damascus', 'source': 'https://www.instagram.com/p/DDKH_XxxyOR/'},
            '12-04': { 'name': 'Nicholas Ferrar', 'url': 'https://en.wikipedia.org/wiki/Nicholas_Ferrar', 'source': 'https://www.instagram.com/p/DDOGOb_OxIU/'},
            '12-04': { 'name': 'Clement of Alexandria', 'url': 'https://en.wikipedia.org/wiki/Clement_of_Alexandria', 'source': 'https://www.instagram.com/p/DDMrL3GuG4c/'},
            '12-06': { 'name': 'Nicholas', 'source': 'https://www.instagram.com/p/DDOGOb_OxIU/' },
            '12-07': { 'name': 'Ambrose', 'source': 'https://www.instagram.com/p/DDSIyUhuBZM/' },
            '12-10': { 'name': 'Thomas Merton', 'url': 'https://en.wikipedia.org/wiki/Thomas_Merton', 'source': 'https://www.instagram.com/p/DDZnyIUO41q/'},
            '12-12': { 'name': 'Jane Frances de Chantal', 'url': 'https://en.wikipedia.org/wiki/Jane_Frances_de_Chantal', 'source': 'https://www.instagram.com/p/DDe3uqaOwSD/'},
            '12-13': { 'name': 'Samuel Johnson', 'url': 'https://en.wikipedia.org/wiki/Samuel_Johnson', 'source': 'https://www.instagram.com/p/DDpHHQ6OUOm/'},
            '12-13': { 'name': 'Lucy', 'source': 'https://www.instagram.com/p/DDhPzXtuPtn/' },
            '12-14': { 'name': 'John of the Cross', 'source': 'https://www.instagram.com/p/DDj1oMMuwls/' },
            '12-15': { 'name': 'Nino', 'url': 'https://en.wikipedia.org/wiki/Saint_Nino', 'source': 'https://www.instagram.com/p/DDk7SGjOgPG/'},
            '12-17': { 'name': 'Dorothy Sayers', 'url': 'https://en.wikipedia.org/wiki/Dorothy_L._Sayers', 'source': 'https://www.instagram.com/p/DDrb62uO7q_/'},
            '12-19': { 'name': 'Lillian Trasher', 'url': 'https://en.wikipedia.org/wiki/Lillian_Trasher', 'source': 'https://www.instagram.com/p/DDuAxR5uujs/'},
            '12-20': { 'name': 'Katharina von Bora', 'url': 'https://en.wikipedia.org/wiki/Katharina_von_Bora', 'source': 'https://www.instagram.com/p/DDzY6N7u59i/'},
            '12-23': { 'name': 'John of Kanty', 'url': 'https://en.wikipedia.org/wiki/John_Cantius', 'source': 'https://www.instagram.com/p/DD7R40dRUgZ/'},
            '12-24': { 'name': 'Lottie Moon', 'url': 'https://en.wikipedia.org/wiki/Lottie_Moon', 'source': 'https://www.instagram.com/p/DD3KJPMOrsR/'},
            '12-25': { 'name': 'Christmas', 'source': 'https://www.instagram.com/p/DD_STbbu5tP/'},
            '12-26': { 'name': 'Stephen', 'source': 'https://www.instagram.com/p/DECrED9OHgU/'},
            '12-27': { 'name': 'John the Apostle', 'source': 'https://www.instagram.com/p/DEFbPcOOee9/'},
            # The Holy Family is on Sunday After Christmas
            '12-28': { 'name': 'The Holy Family', 'url': 'https://en.wikipedia.org/wiki/Holy_Family', 'source': 'https://www.instagram.com/p/DENOTZOOYPN/'},
            '12-28': { 'name': 'The Holy Innocents', 'source': 'https://www.instagram.com/p/DEHwrMWOTHK/'},
            '12-29': { 'name': 'Thomas Becket', 'source': 'https://www.instagram.com/p/DEKQYfCuaCM/'},
            '12-31': { 'name': 'Sylvester', 'url': 'https://en.wikipedia.org/wiki/Pope_Sylvester_I', 'source': 'https://www.instagram.com/p/DEPxiTLOa4j/'},
        }
    }

    # Get the feast from the list above
    feast = feasts[relative_to].get(pointer)

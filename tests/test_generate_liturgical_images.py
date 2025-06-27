import subprocess
import sys
from pathlib import Path

dates_to_test = [
    # Same day, different years (cycle test)
    '2023-03-29',
    '2024-03-29',
    '2025-03-29',
    # Various seasons in 2025
    '2025-01-06',  # Epiphany
    '2025-02-26',  # Lent (Ash Wednesday)
    '2025-04-20',  # Easter
    '2025-05-29',  # Ascension
    '2025-12-25',  # Christmas
    # Ordinary Time in 2025
    '2025-06-15',  # After Trinity
    '2025-07-13',  # Mid Ordinary Time
    '2025-08-24',  # Late Ordinary Time
    '2025-09-21',  # Michaelmas season
    '2025-10-19',  # Autumn Ordinary
    '2025-11-16',  # End of Ordinary Time
    # Multiple artwork options (cycle test, 3 years for each)
    '2023-01-02', '2024-01-02', '2025-01-02',  # Vedanayagam Samuel Azariah / Seraphim of Sarov
    '2023-01-13', '2024-01-13', '2025-01-13',  # Hilary / Mungo
    '2023-04-01', '2024-04-01', '2025-04-01',  # Frederick Denison Maurice / Mary of Egypt / F.D. Maurice
    '2023-05-24', '2024-05-24', '2025-05-24',  # John and Charles Wesley / Jackson Kemper / Vincent of Lérins
    '2023-07-15', '2024-07-15', '2025-07-15',  # Swithun / Bonaventure / St Olga and St Vladimir
    '2023-07-19', '2024-07-19', '2025-07-19',  # Gregory and Macrina / Macrina
    '2023-07-25', '2024-07-25', '2025-07-25',  # Christopher / James the Apostle
    '2023-08-09', '2024-08-09', '2025-08-09',  # Mary Sumner / Edith Stein
    '2023-08-14', '2024-08-14', '2025-08-14',  # Maximilian Kolbe / Jonathan Myrick Daniels
    '2023-08-27', '2024-08-27', '2025-08-27',  # Monica / Simeon Bachos
    '2023-08-30', '2024-08-30', '2025-08-30',  # John Bunyan / Charles Chapman Grafton
    '2023-08-31', '2024-08-31', '2025-08-31',  # Aidan / Joseph of Arimathea
    '2023-09-06', '2024-09-06', '2025-09-06',  # Allen Gardiner / Hannah More
    '2023-09-09', '2024-09-09', '2025-09-09',  # Charles Fuge Lowder / Constance and Her Companions
    '2023-09-16', '2024-09-16', '2025-09-16',  # Ninian / Edward Bouverie Pusey
    '2023-09-20', '2024-09-20', '2025-09-20',  # John Coleridge Patteson / Andrew Kim Taegon
    '2023-09-25', '2024-09-25', '2025-09-25',  # Lancelot Andrewes / Sergius of Radonezh
    '2023-10-01', '2024-10-01', '2025-10-01',  # Thérèse of Lisieux / Remigius / Anthony Ashley Cooper
    '2023-10-11', '2024-10-11', '2025-10-11',  # Ethelburga / Philip the Deacon
    '2023-10-12', '2024-10-12', '2025-10-12',  # Wilfrid / Cecil Frances Alexander
    '2023-10-15', '2024-10-15', '2025-10-15',  # Samuel Isaac Joseph Schereschewsky / Teresa of Avila
    '2023-10-31', '2024-10-31', '2025-10-31',  # Martin Luther / All Hallows Eve
    '2023-11-22', '2024-11-22', '2025-11-22',  # Cecilia / C.S. Lewis
    '2023-11-25', '2024-11-25', '2025-11-25',  # Catherine / Isaac Watts
    '2023-12-04', '2024-12-04', '2025-12-04',  # John of Damascus / Nicholas Ferrar / Clement of Alexandria
    '2023-12-13', '2024-12-13', '2025-12-13',  # Samuel Johnson / Lucy
    '2023-12-28', '2024-12-28', '2025-12-28',  # The Holy Family / The Holy Innocents
]

script_path = Path(__file__).parent / 'create_liturgical_image.py'

for date in dates_to_test:
    print(f'Generating image for {date}...')
    result = subprocess.run([sys.executable, str(script_path), date], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f'Error for {date}:')
        print(result.stderr)
    print('-' * 40) 
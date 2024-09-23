from datetime import time
from dozenten import Dozent

# Liste der Dozierenden mit genauen Zeitfenstern (Stunden und Minuten)
dozent1 = Dozent("Herr Müller", {
    "Montag": [(time(9, 0), time(13, 0))],
    "Dienstag": [(time(10, 0), time(14, 0))],
    "Donnerstag": [(time(9, 0), time(12, 0))]
})

dozent2 = Dozent("Frau Schmidt", {
    "Montag": [(time(13, 0), time(16, 0))],
    "Mittwoch": [(time(9, 0), time(12, 0))],
    "Freitag": [(time(10, 0), time(13, 0))]
})

dozent3 = Dozent("Herr Becker", {
    "Dienstag": [(time(8, 0), time(12, 0))],
    "Donnerstag": [(time(11, 0), time(15, 0))],
    "Freitag": [(time(9, 0), time(14, 0))]
})

# Alle Dozierenden in eine Liste packen
dozenten_liste = [dozent1, dozent2, dozent3]

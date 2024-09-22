from dozenten import Dozent

dozent1 = Dozent("Herr Müller", {
    "Montag": [(9, 13)],
    "Dienstag": [(10, 14)],
    "Donnerstag": [(9, 12)]
})

dozent2 = Dozent("Frau Schmidt", {
    "Montag": [(13, 16)],
    "Mittwoch": [(9, 12)],
    "Freitag": [(10, 13)]
})

dozent3 = Dozent("Herr Becker", {
    "Dienstag": [(8, 12)],
    "Donnerstag": [(11, 15)],
    "Freitag": [(9, 14)]
})

dozenten_liste = [dozent1, dozent2, dozent3]

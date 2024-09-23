from datetime import time
from studenten import Student

# Liste der Studierenden mit genauen Zeitfenstern (Stunden und Minuten)
student1 = Student("Max Mustermann", {
    "Montag": [(time(9, 0), time(10, 15)), (time(14, 0), time(15, 45))],
    "Dienstag": [(time(10, 15), time(12, 0))],
    "Mittwoch": [(time(12, 0), time(14, 0))]
}, 60)

student2 = Student("Anna Beispiel", {
    "Montag": [(time(8, 0), time(9, 0))],
    "Mittwoch": [(time(13, 0), time(14, 0))],
    "Freitag": [(time(9, 0), time(10, 0))]
}, 45)

student3 = Student("Lisa Müller", {
    "Dienstag": [(time(9, 0), time(10, 0))],
    "Donnerstag": [(time(11, 0), time(13, 0))],
    "Freitag": [(time(10, 0), time(12, 0))]
}, 30)

student4 = Student("Tom Schmidt", {
    "Montag": [(time(14, 0), time(15, 0))],
    "Mittwoch": [(time(10, 0), time(11, 0))],
    "Donnerstag": [(time(9, 0), time(10, 0))]
}, 60)

student5 = Student("Clara Weber", {
    "Montag": [(time(9, 0), time(11, 0))],
    "Freitag": [(time(14, 0), time(15, 0))]
}, 45)

student6 = Student("Ben Fischer", {
    "Dienstag": [(time(8, 0), time(9, 0)), (time(15, 0), time(16, 0))],
    "Donnerstag": [(time(12, 0), time(14, 0))]
}, 60)

student7 = Student("Emma Schröder", {
    "Mittwoch": [(time(10, 0), time(12, 0))],
    "Freitag": [(time(11, 0), time(12, 0))]
}, 30)

student8 = Student("Lukas Meier", {
    "Montag": [(time(9, 0), time(10, 0)), (time(16, 0), time(17, 0))],
    "Dienstag": [(time(13, 0), time(14, 0))]
}, 45)

student9 = Student("Sophia Neumann", {
    "Montag": [(time(8, 0), time(9, 0))],
    "Mittwoch": [(time(15, 0), time(16, 0))]
}, 60)

student10 = Student("Felix Wagner", {
    "Dienstag": [(time(9, 0), time(10, 0))],
    "Donnerstag": [(time(14, 0), time(16, 0))]
}, 60)

student11 = Student("Marie Becker", {
    "Montag": [(time(14, 0), time(15, 0))],
    "Dienstag": [(time(10, 0), time(12, 0))]
}, 30)

student12 = Student("Elias Bauer", {
    "Donnerstag": [(time(8, 0), time(9, 0))],
    "Freitag": [(time(14, 0), time(15, 0))]
}, 45)

student13 = Student("Lea Hoffmann", {
    "Dienstag": [(time(11, 0), time(12, 0))],
    "Mittwoch": [(time(9, 0), time(10, 0))]
}, 30)

student14 = Student("Jonas Peters", {
    "Montag": [(time(12, 0), time(13, 0))],
    "Freitag": [(time(8, 0), time(9, 0))]
}, 45)

student15 = Student("Mia Köhler", {
    "Donnerstag": [(time(10, 0), time(11, 0)), (time(14, 0), time(15, 0))]
}, 60)

student16 = Student("David Lang", {
    "Dienstag": [(time(10, 0), time(11, 0))],
    "Mittwoch": [(time(12, 0), time(13, 0))]
}, 45)

student17 = Student("Hannah Wolf", {
    "Montag": [(time(14, 0), time(16, 0))],
    "Freitag": [(time(9, 0), time(11, 0))]
}, 60)

student18 = Student("Paul Krause", {
    "Dienstag": [(time(9, 0), time(10, 0))],
    "Donnerstag": [(time(13, 0), time(14, 0))]
}, 45)

student19 = Student("Julia Lehmann", {
    "Montag": [(time(11, 0), time(12, 0))],
    "Mittwoch": [(time(14, 0), time(15, 0))]
}, 30)

student20 = Student("Lena Schwarz", {
    "Donnerstag": [(time(12, 0), time(14, 0))],
    "Freitag": [(time(10, 0), time(11, 0))]
}, 60)

student21 = Student("Tim Krüger", {
    "Montag": [(time(9, 0), time(10, 0))],
    "Mittwoch": [(time(15, 0), time(16, 0))]
}, 45)

student22 = Student("Nina Braun", {
    "Dienstag": [(time(14, 0), time(15, 0))],
    "Donnerstag": [(time(9, 0), time(10, 0))]
}, 30)

student23 = Student("Jan Richter", {
    "Mittwoch": [(time(8, 0), time(9, 0)), (time(14, 0), time(15, 0))],
    "Freitag": [(time(11, 0), time(12, 0))]
}, 60)

student24 = Student("Laura Busch", {
    "Dienstag": [(time(10, 0), time(12, 0))],
    "Donnerstag": [(time(15, 0), time(16, 0))]
}, 45)

student25 = Student("Sarah Keller", {
    "Montag": [(time(14, 0), time(16, 0))],
    "Freitag": [(time(8, 0), time(10, 0))]
}, 60)

# Alle Studierenden in eine Liste packen
studenten_liste = [
    student1, student2, student3, student4, student5, student6, student7,
    student8, student9, student10, student11, student12, student13, student14,
    student15, student16, student17, student18, student19, student20, student21,
    student22, student23, student24, student25
]

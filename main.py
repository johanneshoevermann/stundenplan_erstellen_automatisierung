import pprint
from studentendaten import *
from dozentendaten import *
from timefunctions import convert_time_to_datetime, get_intervals
from intervalle import *


""" def get_zeittupel(person, tag):
    for entry in person.verfuegbare_zeiten[tag]:
        anfangszeit, endzeit = entry
        tstart = convert_time_to_datetime(anfangszeit)
        tend = convert_time_to_datetime(endzeit)

        periods = get_intervals(tstart, tend, 15)

        if isinstance(person, Student):
            if person.unterrichtsdauer == 30:
                return Zweiergruppen(periods)
            elif person.unterrichtsdauer == 45:
                return Dreiergruppen(periods)
            elif person.unterrichtsdauer == 60:
                return Vierergruppen(periods)
            else:
                return "Fehler: keine sinvolle Unterrichtslänge vom Studenten angegeben."

        if isinstance(person, Dozent):
            return Zweiergruppen(periods), Dreiergruppen(periods), Vierergruppen(periods)
 """

# pprint.pprint(get_zeittupel(dozent2, "Montag"))


def common_data(doz_list, stud_list):
    for x in doz_list:
        for y in stud_list:
            if x == y:
                print(f"Gemeinsame Zeit gefunden:\n{x}")
                return x
    else:
        print("Kein gemeinsamer Zeitslot.")


def find_match(dozent, student, tag):
    a, b, c = dozent.get_time_tupel(tag)

    if student.unterrichtsdauer == 30:
        common_data(a, student.get_time_tupel(tag))
    if student.unterrichtsdauer == 45:
        common_data(b, student.get_time_tupel(tag))
    if student.unterrichtsdauer == 60:
        common_data(c, student.get_time_tupel(tag))


dozent = dozent2
student = student1
tag = "Mittwoch"
find_match(dozent, student, tag)

# print(student1.get_time_tupel("Montag"))

# print(dozent1.get_time_tupel("Montag"))

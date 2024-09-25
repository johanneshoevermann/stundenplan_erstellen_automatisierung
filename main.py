import pprint
from studentendaten import *
from dozentendaten import *
from timefunctions import convert_time_to_datetime, get_intervals
from intervalle import *


def get_zeittupel(person, tag):
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


pprint.pprint(get_zeittupel(dozent2, "Montag"))

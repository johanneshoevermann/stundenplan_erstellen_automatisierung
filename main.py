import datetime
from studentendaten import *
from dozentendaten import *
from timefunctions import convert_time_to_datetime, get_intervals
from dozentenintervalle import Vierergruppen

# bei mehreren Zeitfenstern gibt es hier wohl ein problem da die Varaiablen überschireben werden.
for entry in dozent1.verfuegbare_zeiten["Montag"]:
    anfangszeit, endzeit = entry

tstart = convert_time_to_datetime(anfangszeit)
tend = convert_time_to_datetime(endzeit)

periods = get_intervals(tstart, tend, 15)

gruppen = Vierergruppen(periods)

for gruppe in gruppen:
    print(f"\n{gruppe}")

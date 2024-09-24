import datetime
from studentendaten import *
from dozentendaten import *
from timefunctions import convert_time_to_datetime, get_intervals
from dozentenintervalle import Vierergruppen

# periods = []


# def wer_hat_wann_zeit():
#     for dozent in dozenten_liste:
#         for x in dozent.verfuegbare_zeiten:
#             print(f"{dozent.name}, Zeiten {x}: {
#                   dozent.verfuegbare_zeiten[x]}\n")
#             print(f"Folgende Studenten haben ebenfalls am {x} Zeit: ")
#             for student in studenten_liste:
#                 try:
#                     print(f"{student.name}, Zeiten {x}: {
#                         student.verfuegbare_zeiten[x]}")
#                 except:
#                     pass
#             print("\n")
#         print("\n\n\n")


# # diese Zeiten sollen später aus einem anderen File kommen. Die sind hier nur solange ich die Funktionen hier schreibe.
# tstart = datetime.time(9, 0)
# tend = datetime.time(13, 0)


# def convert_time_to_datetime(time):
#     date = datetime.date.today()
#     print(date)
#     date_time = datetime.datetime.combine(date, time)
#     return (date_time)


# def get_intervals(start, end, interval):
#     tstart = start
#     tend = end
#     tinterval = datetime.timedelta(minutes=interval)

#     period_start = tstart
#     while period_start < tend:
#         period_end = min(period_start + tinterval, tend)
#         periods.append((period_start, period_end))
#         period_start = period_end

#     return periods


# new_start = convert_time_to_datetime(tstart)
# new_end = convert_time_to_datetime(tend)


# get_intervals(new_start, new_end, 15)


# def Vierergruppen(list):
#     gruppen = []

#     for i in range(0, len(list), 1):
#         gruppen.append(list[i:i+4])

#     return gruppen


# gruppen = Vierergruppen(periods)

# for gruppe in gruppen:
#     print(f"\n{gruppe}")

# bei mehreren Zeitfenstern gibt es hier wohl ein problem da die Varaiablen überschireben werden.
for entry in dozent1.verfuegbare_zeiten["Montag"]:
    anfangszeit, endzeit = entry

tstart = convert_time_to_datetime(anfangszeit)
tend = convert_time_to_datetime(endzeit)

periods = get_intervals(tstart, tend, 15)

gruppen = Vierergruppen(periods)

for gruppe in gruppen:
    print(f"\n{gruppe}")

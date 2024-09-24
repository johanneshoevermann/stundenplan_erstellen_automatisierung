from studentendaten import *
from dozentendaten import *
import datetime


def wer_hat_wann_zeit():
    for dozent in dozenten_liste:
        for x in dozent.verfuegbare_zeiten:
            print(f"{dozent.name}, Zeiten {x}: {
                  dozent.verfuegbare_zeiten[x]}\n")
            print(f"Folgende Studenten haben ebenfalls am {x} Zeit: ")
            for student in studenten_liste:
                try:
                    print(f"{student.name}, Zeiten {x}: {
                        student.verfuegbare_zeiten[x]}")
                except:
                    pass
            print("\n")
        print("\n\n\n")


# wer_hat_wann_zeit()

# for intervall in dozent1.verfuegbare_zeiten["Montag"]:
    print(intervall)


# tstart = datetime.time(9, 0)
# tend = datetime.time(13, 0)
# interval = datetime.timedelta(minutes=30)

# periods = []

# period_start = tstart
# while period_start < tend:
#     print(period_start)
#     newTime = period_start + interval
#     period_end = min(period_start + interval, tend)
#     periods.append((period_start, period_end))
#     period_start = period_end

# print(periods)

# date_and_time = datetime.datetime(2021, 8)
# print("Original time:")
# print(date_and_time)

# # Calling the timedelta() function
# time_change = datetime.timedelta(minutes=75)
# new_time = date_and_time + time_change

# # Printing the new datetime object
# print("changed time:")
# print(new_time)

tstart = datetime.time(9, 0)
tend = datetime.time(13, 0)


def convert_time_to_datetime(time):
    date = datetime.date.today()
    print(date)
    date_time = datetime.datetime.combine(date, time)
    return (date_time)


# convert_time_to_datetime(tstart)

def get_intervals(start, end, interval):
    tstart = start
    tend = end
    tinterval = datetime.timedelta(minutes=interval)

    periods = []

    period_start = tstart
    while period_start < tend:
        period_end = min(period_start + tinterval, tend)
        periods.append((period_start, period_end))
        period_start = period_end

    print(periods)


new_start = convert_time_to_datetime(tstart)
new_end = convert_time_to_datetime(tend)


get_intervals(new_start, new_end, 30)

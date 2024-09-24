import datetime


def convert_time_to_datetime(time):
    date = datetime.date.today()
    print(date)
    date_time = datetime.datetime.combine(date, time)
    return (date_time)

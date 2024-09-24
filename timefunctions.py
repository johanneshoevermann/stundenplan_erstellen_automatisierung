import datetime


def convert_time_to_datetime(time):
    date = datetime.date.today()
    date_time = datetime.datetime.combine(date, time)
    return (date_time)


def get_intervals(start, end, interval):
    periods = []
    tstart = start
    tend = end
    tinterval = datetime.timedelta(minutes=interval)

    period_start = tstart
    while period_start < tend:
        period_end = min(period_start + tinterval, tend)
        periods.append((period_start, period_end))
        period_start = period_end

    return periods

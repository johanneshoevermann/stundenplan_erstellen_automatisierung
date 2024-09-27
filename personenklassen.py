""" class Person:
    def __init__(self, name, verfuegbare_zeiten):
        self.name = name
        self.verfuegbare_zeiten = verfuegbare_zeiten


class Student(Person):
    def __init__(self, name, verfuegbare_zeiten, unterrichtsdauer):
        super().__init__(name, verfuegbare_zeiten)
        self.unterrichtsdauer = unterrichtsdauer
        


class Dozent(Person):
    pass
  """


import datetime


class Person:
    def __init__(self, name, verfuegbare_zeiten):
        self.name = name
        self.verfuegbare_zeiten = verfuegbare_zeiten

    def convert_time_to_datetime(self, time):
        date = datetime.date.today()
        date_time = datetime.datetime.combine(date, time)
        return (date_time)

    def get_intervals(self, start, end, interval):
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

    @staticmethod
    def Vierergruppen(list):
        gruppen = []

        for i in range(0, len(list) - 3):
            gruppen.append(list[i:i+4])

        return gruppen

    @staticmethod
    def Dreiergruppen(list):
        gruppen = []

        for i in range(0, len(list) - 2):
            gruppen.append(list[i:i+3])

        return gruppen

    @staticmethod
    def Zweiergruppen(list):
        gruppen = []

        for i in range(0, len(list) - 1):
            gruppen.append(list[i:i+2])

        return gruppen


class Student(Person):
    def __init__(self, name, verfuegbare_zeiten, unterrichtsdauer):
        super().__init__(name, verfuegbare_zeiten)
        self.unterrichtsdauer = unterrichtsdauer

    def get_time_tupel(self, tag):
        for entry in self.verfuegbare_zeiten[tag]:
            anfangszeit, endzeit = entry
            tstart = self.convert_time_to_datetime(anfangszeit)
            tend = self.convert_time_to_datetime(endzeit)

            periods = self.get_intervals(tstart, tend, 15)

            if self.unterrichtsdauer == 30:
                return self.Zweiergruppen(periods)
            elif self.unterrichtsdauer == 45:
                return self.Dreiergruppen(periods)
            elif self.unterrichtsdauer == 60:
                return self.Vierergruppen(periods)
            else:
                return "Fehler: keine sinvolle Unterrichtslänge vom Studenten angegeben."


class Dozent(Person):
    def __init__(self, name, verfuegbare_zeiten):
        super().__init__(name, verfuegbare_zeiten)

    def get_time_tupel(self, tag):
        for entry in self.verfuegbare_zeiten[tag]:
            anfangszeit, endzeit = entry
            tstart = self.convert_time_to_datetime(anfangszeit)
            tend = self.convert_time_to_datetime(endzeit)

            periods = self.get_intervals(tstart, tend, 15)

        return self.Zweiergruppen(periods), self.Dreiergruppen(periods), self.Vierergruppen(periods)

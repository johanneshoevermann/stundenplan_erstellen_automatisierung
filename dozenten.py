class Dozent:
    def __init__(self, name, verfuegbare_zeiten):
        self.name = name
        self.verfuegbare_zeiten = verfuegbare_zeiten

    def __repr__(self):
        return f"Dozent({self.name}, {self.verfuegbare_zeiten})"

class Person:
    def __init__(self, name, verfuegbare_zeiten):
        self.name = name
        self.verfuegbare_zeiten = verfuegbare_zeiten


class Student(Person):
    def __init__(self, name, verfuegbare_zeiten, unterrichtsdauer):
        super().__init__(name, verfuegbare_zeiten)
        self.unterrichtsdauer = unterrichtsdauer


class Dozent(Person):
    pass

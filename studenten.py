class Student:
    def __init__(self, name, verfuegbare_zeiten, unterrichtsdauer):
        self.name = name
        self.verfuegbare_zeiten = verfuegbare_zeiten
        self.unterrichtsdauer = unterrichtsdauer

    # Methode, um eine gut lesbare Repräsentation eines Objektes der Klasse ausgeben zu können. Dient mir, dem Entwickler, um einfach sehen zu können, welche Daten in einem Objekt enthalten sind.

    def __repr__(self):
        return f"Student({self.name}. {self.verfuegbare_zeiten}, {self.unterrichtsdauer} Minuten)"

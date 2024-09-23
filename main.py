from studentendaten import *
from dozentendaten import *


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


wer_hat_wann_zeit()

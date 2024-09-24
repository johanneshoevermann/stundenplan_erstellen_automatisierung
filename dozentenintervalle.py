from dozentendaten import *


def Vierergruppen(list):
    gruppen = []

    for i in range(0, len(list), 1):
        gruppen.append(list[i:i+4])

    return gruppen

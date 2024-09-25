def Vierergruppen(list):
    gruppen = []

    for i in range(0, len(list), 1):
        gruppen.append(list[i:i+4])

    return gruppen


def Dreiergruppen(list):
    gruppen = []

    for i in range(0, len(list), 1):
        gruppen.append(list[i:i+3])

    return gruppen


def Zweiergruppen(list):
    gruppen = []

    for i in range(0, len(list), 1):
        gruppen.append(list[i:i+2])

    return gruppen

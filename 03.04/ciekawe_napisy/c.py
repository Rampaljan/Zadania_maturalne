plik = open("03.04/ciekawe_napisy/_NAPIS.TXT", "r")

tabela = []

for line in plik:
    wiersz = line.strip()
    tabela.append(wiersz)


powtarzajace_sie = []

for element in tabela:
    wystapienia = 0
    for porownanie in tabela:
        if element == porownanie:
            wystapienia += 1

    if wystapienia > 1 and element not in powtarzajace_sie:
        powtarzajace_sie.append(element)

for element in powtarzajace_sie:
    print(element)


# FHJLMU
# GC
# QULA
# CEGKZ
# BZYFFLOICLUNWLTH
# SWIFT
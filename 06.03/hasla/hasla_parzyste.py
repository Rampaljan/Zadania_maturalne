plik = open("06.03\hasla\hasla.txt","r")

parzyste = 0
nieparzyste = 0

for line in plik:
    wiersz = line.strip()
    if len(wiersz) % 2 == 0:
        parzyste+=1
    else:
        nieparzyste+=1

print(f"""Parzyste: {parzyste}
Nieparzyste: {nieparzyste}""")

    
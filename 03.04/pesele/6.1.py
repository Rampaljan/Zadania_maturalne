plik = open("03.04\pesele\dane.txt","r")

kobiety = 0
mezczyzni = 0

for line in plik:
    wiersz = line.strip()
    if int(wiersz[9]) %2 == 0:
        kobiety+=1
    else:
        mezczyzni+=1

print(f"Mężczyźni: {mezczyzni}, Kobiety: {kobiety}")

# Mężczyźni: 558, Kobiety: 442
def sumacyfr(x):
    suma = 0
    for letter in x:
        suma += int(letter)

    return suma


plik = open("22.05\_2020\liczby.txt","r")

ile = 0

for line in plik:
    wiersz = line.strip()
    if sumacyfr(wiersz) == 11:
        print(wiersz)

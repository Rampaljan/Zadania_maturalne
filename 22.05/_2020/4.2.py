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


# Output:
# 290
# 17120
# 31025
# 14510
# 3521
# 425
# 13502
# 3125
# 12512
# 40070
# 33140
# 12161
# 30233
# 20234
plik = open("29.05\_2015\liczby.txt","r")

by_8 = 0
by_2 = 0
for line in plik:
    wiersz = line.strip()

    wiersz = int(wiersz, 2)

    if wiersz % 2 == 0:
        by_2 += 1

    if wiersz % 8 == 0:
        by_8 += 1

print(by_2, by_8)

#Output:
#500 123
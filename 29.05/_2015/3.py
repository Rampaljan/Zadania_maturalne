plik = open("29.05\_2015\liczby.txt","r")

biggest = 0
biggest_nr = 0

#tu sobie zamieniłem 250 jedynek z binarnego na dec, bo to najwieksza mozliwa jaka moze byc
smallest = 1809251394333065553493296640760748560207343510400633813116524750123642650623
smallest_nr = 0

nr = 0

for line in plik:
    nr+=1

    wiersz = line.strip()

    wiersz = int(wiersz, 2)

    if wiersz > biggest:
        biggest = wiersz
        biggest_nr = nr

    if wiersz < smallest:
        smallest = wiersz
        smallest_nr = nr

print(smallest_nr, biggest_nr)

#Output:
#859 925
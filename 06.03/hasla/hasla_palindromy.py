plik = open("06.03\hasla\hasla.txt","r")

for line in plik:
    wiersz = line.strip()
    if wiersz == wiersz[::-1]:
        print(wiersz)

#Output:

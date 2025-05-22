plik = open("22.05\_2014\PARY_LICZB.TXT","r")

ile = 0

for line in plik:
    wiersz = line.strip()
    wiersz= wiersz.split(' ')
    a = int(wiersz[0])
    b = int(wiersz[1])

    if b%a == 0 or a%b == 0:
        ile += 1

print(ile)

#Output:
#10
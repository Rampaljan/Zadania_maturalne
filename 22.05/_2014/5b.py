plik = open("22.05\_2014\PARY_LICZB.TXT","r")

ile = 0

for line in plik:
    wiersz = line.strip()
    wiersz= wiersz.split(' ')
    a = int(wiersz[0])
    b = int(wiersz[1])

    while a != b:
        if a>b:
            a = a-b
        if b>a:
            b = b-a
        
    if a == 1:
        ile+=1


print(ile)
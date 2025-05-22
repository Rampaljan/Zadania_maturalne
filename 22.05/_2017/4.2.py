plik = open("22.05\_2017\liczby.txt","r")

suma = 0

for line in plik:
    wiersz = line.strip()
    wiersz = wiersz.split(' ')
    
    a = int(wiersz[0])
    b = int(wiersz[1])
    c = int(wiersz[2])

    while a != b:
        if a>b:
            a = a-b
        if b>a:
            b = b-a

    b = c

    while a != b:
        if a>b:
            a = a-b
        if b>a:
            b = b-a

    suma += a

    print(wiersz, a)

print(suma)
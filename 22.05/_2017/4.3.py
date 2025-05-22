plik = open("22.05\_2017\liczby.txt","r")

ile_rownych_35 = 0
najwieksza_suma = 0
ile_najwiekszej_sumy = 0

for line in plik:
    wiersz = line.strip()
    wiersz = wiersz.split(' ')
    
    a = int(wiersz[0])
    b = int(wiersz[1])
    c = int(wiersz[2])

    suma = a + b + c

    if suma == 35:
        ile_rownych_35 += 1

    if suma > najwieksza_suma:
        najwieksza_suma = suma
    
    if suma == najwieksza_suma:
        ile_najwiekszej_sumy += 1


print(najwieksza_suma, ile_najwiekszej_sumy)
    
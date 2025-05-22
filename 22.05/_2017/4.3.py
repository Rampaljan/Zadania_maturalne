def sumacyfr(x):
    suma = 0
    for letter in x:
        suma += int(letter)

    return suma


plik = open("22.05\_2017\liczby.txt","r")

ile_rownych_35 = 0
najwieksza_suma = 0
ile_najwiekszej_sumy = 0

for line in plik:
    wiersz = line.strip()
    wiersz = wiersz.split(' ')
    
    a = wiersz[0]
    b = wiersz[1]
    c = wiersz[2]

    sum_a = sumacyfr(a)
    sum_b = sumacyfr(b)
    sum_c = sumacyfr(c)

    

    suma = sum_a + sum_b + sum_c

    if suma == 35:
        ile_rownych_35 += 1

    if suma > najwieksza_suma:
        najwieksza_suma = suma
        ile_najwiekszej_sumy = 0
    
    if suma == najwieksza_suma:
        ile_najwiekszej_sumy += 1


print(ile_rownych_35, najwieksza_suma, ile_najwiekszej_sumy)

#Output:
# 4 88 2
    
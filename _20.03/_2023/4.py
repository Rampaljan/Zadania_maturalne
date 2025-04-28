plik = open("Depresja\_20.03\_2023\_anagram.txt")

nie_ma_zera = 0
najw_suma = 0
liczba_najwiekszej_sumy = 0

for line in plik:
    wiersz = line.strip()

    liczba = str(int(wiersz, 2))
    if "0" not in liczba:
        nie_ma_zera += 1

    suma = 0
    if "1" in liczba:
        suma += 1
    if "2" in liczba:
        suma += 2
    if "3" in liczba:
        suma += 3
    if "4" in liczba:
        suma += 4
    if "5" in liczba:
        suma += 5
    if "6" in liczba:
        suma += 6
    if "7" in liczba:
        suma += 7
    if "8" in liczba:
        suma += 8
    if "9" in liczba:
        suma += 9

    if suma > najw_suma:
        najw_suma = suma
        liczba_najwiekszej_sumy = liczba

print(nie_ma_zera, liczba_najwiekszej_sumy)


#Output:
# 728 7896
plik = open("27.03\_2022\liczby.txt","r")

najw_rozn = 0
liczba_z_najw_rozn = 0

for line in plik:
    wiersz = line.strip()
    wiersz_reversed = wiersz[::-1]

    rozn = abs(int(wiersz)-int(wiersz_reversed))
    if rozn > najw_rozn:
        najw_rozn = rozn
        liczba_z_najw_rozn = int(wiersz)


print(liczba_z_najw_rozn, najw_rozn)
    

# Odpowiedz:
# 1129 8082
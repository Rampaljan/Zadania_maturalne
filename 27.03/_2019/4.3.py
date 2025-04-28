plik = open("27.03\_2019\pierwsze.txt","r")
ile_liczb = 0

for line in plik:
    wiersz = line.strip()
    suma = 0
    for letter in wiersz:
        suma += int(letter)

    suma_sumy = 0
    suma = str(suma)
    for letter in suma:
        suma_sumy += int(letter)

    suma_sumy = str(suma_sumy)
    
    if len(suma_sumy) == 2:
        ile_liczb += 1

print(ile_liczb)


    

#Odpowiedź:
# 27

    
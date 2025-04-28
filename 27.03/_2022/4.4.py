plik = open("27.03\_2022\liczby.txt", "r")

liczby = []

for line in plik:
    wiersz = line.strip()

    czy_istnieje = False
    for element in liczby:
        if element["liczba"] == wiersz:
            element["ilosc"] += 1

            czy_istnieje = True
            break

    if not czy_istnieje:
        liczby.append({
            "liczba": wiersz,
            "ilosc": 1
        })

poj = 0
pod = 0
pot = 0

for element in liczby:
    if element["ilosc"] == 2:
        pod+=1
    if element["ilosc"] == 3:
        pot+=1

print(len(liczby), pod, pot)


# Output:
# 85 13 1



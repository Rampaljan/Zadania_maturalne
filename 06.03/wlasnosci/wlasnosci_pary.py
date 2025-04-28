plik = open("06.03\wlasnosci\wlasnosci.txt","r")

liczby = []

for line in plik:
    wiersz = line.strip()

    reprezentacja = ""

    if "0" in wiersz:
        reprezentacja += "1"
    else:
        reprezentacja += "0"
    if "1" in wiersz:
        reprezentacja += "1"
    else:
        reprezentacja += "0"
    if "2" in wiersz:
        reprezentacja += "1"
    else:
        reprezentacja += "0"
    if "3" in wiersz:
        reprezentacja += "1"
    else:
        reprezentacja += "0"
    if "4" in wiersz:
        reprezentacja += "1"
    else:
        reprezentacja += "0"
    if "5" in wiersz:
        reprezentacja += "1"
    else:
        reprezentacja += "0"
    if "6" in wiersz:
        reprezentacja += "1"
    else:
        reprezentacja += "0"
    if "7" in wiersz:
        reprezentacja += "1"
    else:
        reprezentacja += "0"
    if "8" in wiersz:
        reprezentacja += "1"
    else:
        reprezentacja += "0"
    if "9" in wiersz:
        reprezentacja += "1"
    else:
        reprezentacja += "0"


    liczby.append({
        "liczba":wiersz,
        "reprezentacja": reprezentacja
    }
    )
     
pary = []

for i in range(len(liczby)):
    for j in range(i+1, len(liczby)):
        if liczby[i]["reprezentacja"] == liczby[j]["reprezentacja"]:
            pary.append((liczby[i]["liczba"], liczby[j]["liczba"]))

# Wyświetlenie wyników
print("Ilość par liczb z taką samą reprezentacją:")
print(len(pary))


print(liczby)
#Output:
# Ilość par liczb z taką samą reprezentacją:
# 23515

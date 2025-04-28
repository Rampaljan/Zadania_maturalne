plik = open("2018\dane\komputery.txt", "r")

pojemnosci = []

for line in plik:
    wiersz = line.strip()
    
    stripped = wiersz.split("\t")
    temp = stripped[2]

    istnieje_w_bazie_ta_pojemnosc = False
    for i in range(len(pojemnosci)):
        if pojemnosci[i]["poj"] == temp:
            pojemnosci[i]["il"] += 1
            istnieje_w_bazie_ta_pojemnosc = True
            break
    
    if not istnieje_w_bazie_ta_pojemnosc:
        pojemnosci.append({
            "poj": temp,
            "il": 1
        })


# Sortowanie nierosnąco według liczby komputerów
pojemnosci = sorted(pojemnosci, key=lambda x: x["il"], reverse=True)

# Ograniczenie do 10 najczęstszych pojemności
pojemnosci = pojemnosci[:10]


for i in range(len(pojemnosci)):
    print(pojemnosci[i])

#Output:
# {'poj': '300', 'il': 173}
# {'poj': '200', 'il': 31}
# {'poj': '500', 'il': 31}
# {'poj': '800', 'il': 29}
# {'poj': '700', 'il': 28}
# {'poj': '600', 'il': 26}
# {'poj': '400', 'il': 20}
# {'poj': '290', 'il': 11}
# {'poj': '160', 'il': 10}
# {'poj': '220', 'il': 10}
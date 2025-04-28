
def suma_cyfr(n):
    suma_cyfr = 0
    for i in n:
        suma_cyfr += int(i)
    return suma_cyfr

dane = open("anagram1.txt")
suma = 0
prawie_suma = 0

for liczby in dane:
    ile0 = 0
    ile1 = 0
    i = 0
    liczba = liczby.strip()
    while i < len(liczba):
        if liczba[i] == "0":
            ile0 += 1
        else:
            ile1 += 1
        i += 1
    if ile0 == ile1:
        suma += 1
    if ile0 + 1 == ile1 or ile0 - 1 == ile1:
        prawie_suma += 1

print("Liczba liczb zrównoważonych:", suma)
print("Liczba liczb prawie zrównoważonych:", prawie_suma)
dane.close()

dane = open("anagram1.txt")
print("Anagramy cyfrowe:")

for liczby in dane:
    liczba = liczby.strip()
    if len(liczba) == 8:
        ile0 = 0
        ile1 = 0
        i = 0
        liczba = liczby.strip()
        while i < len(liczba):
            if liczba[i] == "0":
                ile0 += 1
            else:
                ile1 += 1
            i += 1
        if ile0 == ile1 or ile0 + 2 == ile1:
            print(liczba)

dane.close()

dane = open("anagram1.txt")
i = 0
max = 0
dziesietna = 0
dziesietna1 = 0

for liczby in dane:
    liczba = liczby.strip()
    if i % 2 == 0:
        dziesietna = int(liczba, 2)
    else:
        dziesietna1 = int(liczba, 2)
    if abs(dziesietna - dziesietna1) > max:
        max = abs(dziesietna - dziesietna1)
    i += 1

print("Największa wartość bezwzględna różnicy między sąsiednimi liczbami:",bin(max).strip("0b"))
dane.close()

dane = open("anagram1.txt")
suma0 = 0
max_suma = 0

for liczby in dane:
    czy0 = True
    liczba = int(liczby.strip(), 2)
    for i in range (len(str(liczba))):
        if str(liczba)[i] == "0":
            czy0 = False
            break
    if czy0 == True:
        suma0 += 1
    unikalne = set(str(liczba))
    if suma_cyfr(unikalne) > max_suma:
        max_suma += 1
print("Liczba liczb, w których nie występuje 0:", suma0)
dane.close()

dane = open("anagram1.txt")

for liczby in dane:
    liczba = int(liczby.strip(), 2)
    unikalne = set(str(liczba))
    if suma_cyfr(unikalne) == max_suma:
        print("Liczba o największej sumie różnych cyfr:", liczba)
        break
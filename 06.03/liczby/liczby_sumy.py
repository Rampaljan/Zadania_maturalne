plik = open("06.03\liczby\liczby.txt","r")

suma_wszystkich = 0

for line in plik:
    line = line.strip()
    suma = 0
    for i in range(len(line)):
        suma += int(line[i])
        suma_wszystkich += int(line[i])
    if suma > 30:
        print(line)

print(f"Wszystkie cyfry z pliku: {suma_wszystkich}")




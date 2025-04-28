plik = open("06.03\liczby\liczby.txt","r")

najwieksza_parzysta = 0

for line in plik:
    wiersz = line.strip()
    if int(wiersz) % 2 == 0 and int(wiersz) > najwieksza_parzysta:
        najwieksza_parzysta = int(wiersz)

print(najwieksza_parzysta)
    
# Output:
# 29966
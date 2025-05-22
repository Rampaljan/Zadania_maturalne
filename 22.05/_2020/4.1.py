plik = open("22.05\_2020\liczby.txt","r")

ile = 0

for line in plik:
    wiersz = line.strip()
    
    if int(wiersz)%2 != 0:
        ile += 1

print(ile)

# Output:
# 612
plik = open("22.05\_2017\liczby.txt","r")

ile = 0

for line in plik:
    wiersz = line.strip()
    wiersz = wiersz.split(' ')
    
    a = int(wiersz[0])
    b = int(wiersz[1])
    c = int(wiersz[2])

    if a < b < c:
        ile +=1

print(ile)

# Output:
# 139
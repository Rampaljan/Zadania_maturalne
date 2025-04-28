plik = open("Depresja\_20.03\_2023\_anagram.txt")
zrownowazone = 0
prawie_zrownowazone = 0


for line in plik:
    wiersz = line.strip()

    zera = 0
    jedynki = 0

    for letter in wiersz:
        if letter == "0":
            zera += 1
        if letter == "1":
            jedynki += 1
    
    if zera == jedynki:
        zrownowazone += 1

    if abs(zera - jedynki) == 1:
        prawie_zrownowazone += 1

print(zrownowazone)
print(prawie_zrownowazone)

plik.close()
#Output:
# 118
# 219
plik = open("29.05\_2015\liczby.txt","r")

count = 0
for line in plik:
    wiersz = line.strip()

    zera = 0
    jedynki = 0

    for letter in wiersz:
        if letter == "0":
            zera += 1
        if letter == "1":
            jedynki += 1
        

    if zera > jedynki:
        count +=1

print(count)


#Output:
#422
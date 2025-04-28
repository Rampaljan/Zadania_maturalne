plik = open("13.03\_napisy\_napisy.txt","r")
cyfry = 0
for line in plik:
    wiersz = line.strip()
    for letter in wiersz:
        if letter.isdigit():
            cyfry+=1
print(cyfry)

#Output:
#11844
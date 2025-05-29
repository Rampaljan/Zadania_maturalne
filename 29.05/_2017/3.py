plik = open("29.05\_2017\_binarne.txt","r")

biggest = 0
for line in plik:
    wiersz = line.strip()
    wiersz = int(wiersz, 2)

    if wiersz > biggest and wiersz <= 65535:
        biggest = wiersz

print(biggest, bin(biggest))

#Output:
# 54885 0b1101011001100101
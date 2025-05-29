plik = open("29.05\_2017\_binarne.txt","r")

count = 0
smallest_length = 9999999999999999999999999999999999999999

for line in plik:
    wiersz = line.strip()

    i1 = 0
    i2 = 1
    i3 = 2
    i4 = 3


    while i4 <= len(wiersz)+1:
        
        l1 = wiersz[i1]
        l2 = wiersz[i2]
        l3 = wiersz[i3]
        l4 = wiersz[i4]

        sekcja = l1 + l2 + l3 + l4
        
        i1 += 4
        i2 += 4
        i3 += 4
        i4 += 4

        if int(sekcja, 2) > 9:
            count+= 1
            if len(wiersz) < smallest_length:
                smallest_length = len(wiersz)
            break
    
print(count, smallest_length)

#Output:
# 359 4





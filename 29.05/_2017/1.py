plik = open("29.05\_2017\_binarne.txt","r")

count = 0

longest = 0
for line in plik:
    wiersz = line.strip()
    
    first = wiersz[:len(wiersz)//2]
    second = wiersz[len(wiersz)//2:]

    if first == second:
        print(first, second)
        count += 1
        if len(wiersz) > len(str(longest)):
            longest = wiersz

print(count, len(longest), longest)

#Output:
# 18 32 00100101100011100010010110001110

plik = open("29.05\_2013\dane.txt","r")


count = 0
for line in plik:
    wiersz = line.strip()
    
    if wiersz[0] == wiersz[-1:]:
        count += 1

print(count)

#Output:
# 447
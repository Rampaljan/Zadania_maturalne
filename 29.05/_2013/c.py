plik = open("29.05\_2013\dane.txt","r")

smallest = 2000000
biggest = 0
count = 0
for line in plik:
    wiersz = line.strip()

    last_digit = wiersz[0]
    for i in range(0, len(wiersz)):
        
        if wiersz[i] < last_digit:
            break
        else:
            last_digit = wiersz[i]
        
        if i + 1 == len(wiersz):
            count += 1
            if int(wiersz) > biggest:
                biggest = int(wiersz)
            if int(wiersz) < smallest:
                smallest = int(wiersz)

print(count)
print(smallest)
print(biggest)        
        
#Output:
# 49
# 24
# 1133357
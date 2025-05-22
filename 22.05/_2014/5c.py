plik = open("22.05\_2014\PARY_LICZB.TXT","r")

ile = 0

for line in plik:
    wiersz = line.strip()
    wiersz= wiersz.split(' ')

    sum_a = 0
    a = wiersz[0]
    for letter in a:
        sum_a += int(letter)

    sum_b = 0
    b = wiersz[1]
    for letter in b:
        sum_b += int(letter)

    if sum_a == sum_b:
        ile += 1

    

print(ile)

# Output:
# 48
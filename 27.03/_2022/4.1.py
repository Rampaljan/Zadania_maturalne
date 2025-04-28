plik = open("27.03\_2022\liczby.txt","r")

for line in plik:
    wiersz = line.strip()
    wiersz_reversed = wiersz[::-1]
    
    if int(wiersz_reversed)%17 == 0:
        print(wiersz_reversed)


# Output:
# 1156
# 102
# 51
# 765
# 119
# 119
# 731
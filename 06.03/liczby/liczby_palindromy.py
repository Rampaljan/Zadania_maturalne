plik = open("06.03\liczby\liczby.txt","r")

for line in plik:
    wiersz = line.strip()
    if wiersz == wiersz[::-1]:
        print(wiersz)

#Output:
# 787
# 25152
# 16161
# 16261
# 15351
# 252
# 25752
# 11211
# 66
# 20802
# 7007
# 0
# 989
# 10101
# 27172
# 696
# 8888
# 55
# 14841
# 10101
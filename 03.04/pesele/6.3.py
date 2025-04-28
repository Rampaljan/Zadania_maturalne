plik = open("03.04\pesele\dane.txt","r")

for line in plik:
    wiersz = line.strip()

    suma = 1 * int(wiersz[0]) + 3 * int(wiersz[1]) + 7 * int(wiersz[2]) + 9 * int(wiersz[3]) + int(wiersz[4]) + 3 * int(wiersz[5]) + 7 * int(wiersz[6]) + 9 * int(wiersz[7]) + int(wiersz[8]) + 3 * int(wiersz[9]) + int(wiersz[10])

    if suma % 10 != 0:
        print(wiersz)

# 72040163352
# 46020791664
# 93071087527
# 92011957236
# 91031889675
# 58082023664
# 55123056262
# 94080371827
# 88091348655
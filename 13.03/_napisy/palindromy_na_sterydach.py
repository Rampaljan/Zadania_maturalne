plik = open("13.03\_napisy\_napisy.txt","r")

for line in plik:
    wiersz = line.strip()

    litera_z_konca = wiersz[len(wiersz) - 1] + wiersz
    litera_z_poczatku = wiersz + wiersz[0]

    if litera_z_poczatku == litera_z_poczatku[::-1]:
        print(litera_z_poczatku[len(litera_z_poczatku)//2])

    if litera_z_konca == litera_z_konca[::-1]:
        print(litera_z_konca[len(litera_z_poczatku)//2])
            
#Output:
# Z
# A
# D
# A
# N
# I
# E
# M
# A
# T
# U
# R
# A
# L
# N
# E
    
    
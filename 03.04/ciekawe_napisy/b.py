plik = open("03.04\ciekawe_napisy\_NAPIS.TXT","r")

for line in plik:
    wiersz = line.strip()

    for i in range(len(wiersz)):
        if i == 0:
            last_letter = wiersz[i]
        else:
            if wiersz[i] < wiersz[i-1]:
                break
        if i == len(wiersz) - 1:
            print(wiersz)

    
# FHJLMU
# BEJNOSY
# MNS
# # AEIOUY
# LVV
# HHO
# BDL
# JT
# BJQR
# AHJS
# FHJLMU
# DIT
# CEGKZ
# BCV
# CEGIKOT
# CEGKZ
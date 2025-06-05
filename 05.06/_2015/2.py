plik = open("05.06\_2015\_nowe.txt","r")

tab = []

for line in plik:
    wiersz = line.strip()
    tab.append({
        "slowo": wiersz,
        "wystapienia": 0,
        "odbicia": 0
    })


plik2 = open("05.06\_2015\slowa.txt","r")

for line in plik2:
    wiersz = line.strip()

    for i in range(len(tab)):
        if tab[i]["slowo"] == wiersz:
            tab[i]["wystapienia"] += 1

        if tab[i]["slowo"] == wiersz[::-1]:
            tab[i]["odbicia"] += 1

for i in range(len(tab)):
    print(tab[i]["slowo"], tab[i]["wystapienia"], tab[i]["odbicia"])
    

#Output:
# hxqsf 4 5
# erraegrdsj 0 0
# cpcxpzj 3 1
# arphlqleftqm 10 1
# wdt 0 4
# dohzvwt 6 1
# bpgy 2 1
# uxmwceunjvol 11 1
# ilgpjtqibbq 5 1
# mfgoqaznahf 5 4
# evyiolwscoj 5 0
# wyv 0 7
# csuhvnnkgnx 0 4
# fory 5 0
# hqtbdk 5 5
# pjkrdku 4 5
# culp 4 2
# lntslth 4 5
# uiizzqjm 2 5
# mta 4 8
# lhsisobbb 4 5
# d 9 9
# li 0 2
# tbbw 0 4
# rceij 5 0


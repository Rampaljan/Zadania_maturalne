plik = open("06.03\hasla\hasla.txt","r")

for line in plik:
    wiersz = line.strip()
    for i in range(len(wiersz)):
        if (ord(wiersz[i]) + ord(wiersz[i-1])) == 220:
            print(wiersz)
    

#Output:
# amodda
# damod
# damodd
# dompmod
# dompmod
# edamo
# edamod
# isksad
# iughd
# jkaokor
# kisksa
# kkompo
# komok
# komok
# kompiel
# kompo
# kompoc
# kompok
# kompoot
# kompooto
# kompost
# kompot
# komput
# komu
# komunikat
# moddam
# mpokko
# mpootoo
# nruiugh
# nruiughd
# okisks
# okkomp
# omnibus
# omo
# omo
# ompioroip
# ompoci
# ompokk
# ompooto
# ompootoo
# ruiughd
# ruiughdf
# sokisk
# sunruiug
# ughdf
# ughdfbk
# uiughdf
# uiughdfb
# unruiug
# unruiug
# unruiugh
# wasprze
# zedamo
# plkjjklp
# plkjjklp
# mops
# polewa
# komputer
# komputerek
# kolomp
# plomp
# plomp
# plolp
# plolp
# komput    
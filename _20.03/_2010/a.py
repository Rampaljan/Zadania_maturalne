plik = open("20.03\_2010\_anagram.txt","r")
for line in plik:
    wiersz = line.strip()
    

    lista = wiersz.split(" ")
    wielkosc = len(lista[0])
    for i in range(1,5):
        wielkosc_after = len(lista[i])
        if wielkosc != wielkosc_after:
            break
        else:
            if i == 4:
                print(wiersz)

#Output:
# abcd cdba dbac cbad dcba
# wrona rossa slowo gwert rezas
# grant hello zakon lloeh hello
# kabaret kabanos kabaret gertyfu kabaret
# ola ala aga oal ola
# rezas rossa zaser sarez rezas
# foto foto tofo tofo foto
# romans romans normag masrom ansrom
# ekran ranek lampa zakon ekran
# korba orkan delpu pudel udelp
# czek azer reza zare rzea
# cebula romans romans mansro romans
# kruk kruk buka zuka nuka
# agent rossa serce cerse sdfrt
# qwerty wertyq wertyu magnor normag
# glob lobg bogl glbo gblo
# triada dariat aadrit iatdar adatri
# kotek tekok teokk kokte otekk
# obrus bruso soubo seawo rusob
# rower werro werro owerr erwor
# ipfon ipfon fonip ipfon zakop
# nerka drewn korba korba korba
# patyk wrona wrona wrona wrona
# foto tofo foot ftoo ootf
# spiker kerspi erspik erspki kiersp
# burza orkan lukde pudeh lerfy


    





        





    
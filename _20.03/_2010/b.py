plik = open("2010\_anagram.txt","r")
for line in plik:
    wiersz = line.strip()
    
    lista = wiersz.split(" ")
    lista_info = []

    for slowo in lista:
        reprezentacja = ""

        if "a" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "b" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "c" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "d" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "e" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "f" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "g" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "h" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "i" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "j" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "k" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "l" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "m" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "n" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "o" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "p" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "q" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "r" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "s" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "t" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "u" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "v" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "w" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "x" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "y" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"
        if "z" in slowo:
            reprezentacja += "1"
        else:
            reprezentacja += "0"

        lista_info.append({
            "slowo":slowo,
            "reprezentacja":reprezentacja
        })
    
    ilosc = 0
    for i in range(len(lista_info)):
        #trzy warunki: te same znaki, ta sama długość, nie porównujemy samego do siebie
        if lista_info[i]["reprezentacja"] == lista_info[0]["reprezentacja"] and i != 0 and len(lista_info[i]["slowo"]) == len(lista_info[0]["slowo"]):
            # print(lista_info[0]["slowo"], lista_info[i]["slowo"])
            ilosc +=1
    
    if ilosc == 4:
        print(wiersz)   


#Output:
# abcd cdba dbac cbad dcba
# foto foto tofo tofo foto
# glob lobg bogl glbo gblo
# triada dariat aadrit iatdar adatri
# kotek tekok teokk kokte otekk
# rower werro werro owerr erwor
# foto tofo foot ftoo ootf
# spiker kerspi erspik erspki kiersp 




        





    
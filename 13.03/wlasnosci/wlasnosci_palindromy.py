plik = open("06.03\wlasnosci\wlasnosci.txt","r")

def binary(n): 
    wynik = ''
    while n > 0:
        wynik = str(n % 2) + wynik
        n //= 2
    return(wynik)

palindromiczne = 0

for line in plik:
    wiersz = line.strip()
    n = int(wiersz)
    n_binarnie = binary(n)
    
    print(n_binarnie)
    ilosc_zer = 0
    if n_binarnie[len(n_binarnie) - 1] == "0":
        ilosc_zer +=1
        i = 2
        while n_binarnie[len(n_binarnie) - i] == "0":
            ilosc_zer +=1
            i+=1
    
    przedzera = ''
    for i in range(ilosc_zer):
         przedzera += "0"

    n_binarnie = przedzera + n_binarnie
    print(n_binarnie)
    if n_binarnie == n_binarnie[::-1]:
            palindromiczne+=1


print(palindromiczne)


#Output:
#107
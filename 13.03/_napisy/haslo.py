plik = open("13.03\_napisy\_napisy.txt","r")

aktualny_wiersz = 1
haslo = ""
bruh = 0
for line in plik:
    wiersz = line.strip()
    if aktualny_wiersz%20 ==0:
        haslo += wiersz[bruh]
        bruh +=1
    aktualny_wiersz +=1
   

print(haslo)

#Output:
#SZYBKOROZWIAZUJEPROGRAMISTYCZNEZADANIAZINFORMATYKI
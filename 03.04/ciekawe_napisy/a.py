plik = open("03.04\ciekawe_napisy\_NAPIS.TXT","r")

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

ile_pierwszych = 0

for line in plik:
    wiersz = line.strip()

    suma = 0
    for letter in wiersz:
        suma +=  ord(letter)

    if isPrime(suma):
        ile_pierwszych +=1

print(ile_pierwszych)


#122

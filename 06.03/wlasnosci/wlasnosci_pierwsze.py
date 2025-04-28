plik = open("06.03\wlasnosci\wlasnosci.txt","r")

najwieksza = 0
najmniejsza = 1000000
ilosc = 0

def is_prime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True

for line in plik:
    wiersz = line.strip()
    n = int(wiersz)
    if is_prime(n):
        ilosc+=1
        if n > najwieksza:
            najwieksza = n
        if n < najmniejsza:
            najmniejsza = n

print(f"""
Liczba liczb pierwszych: {ilosc}
Największa liczba: {najwieksza}
Najmniejsza liczba: {najmniejsza}
""")
    

#Output:
# Liczba liczb pierwszych: 501
# Największa liczba: 99767
# Najmniejsza liczba: 311
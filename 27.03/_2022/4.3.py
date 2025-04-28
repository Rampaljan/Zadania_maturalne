def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

plik = open("27.03\_2022\liczby.txt","r")

for line in plik:
    wiersz = line.strip()
    wiersz_reversed = wiersz[::-1]

    if isPrime(int(wiersz)) and isPrime(int(wiersz_reversed)):
        print(wiersz)


# Odpowiedz:
# 157
# 31
# 347
# 929
# 941
# 761
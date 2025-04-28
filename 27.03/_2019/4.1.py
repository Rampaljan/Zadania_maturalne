def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

plik = open("27.03\_2019\liczby.txt","r")

for line in plik:
    wiersz = line.strip()
    n = int(wiersz)

    if n >= 100 and n <= 5000:
        if isPrime(n):
            print(n)


# #Odpowiedź
# 563
# 2087
# 163
# 2423
# 3581
# 911
# 997
# 113
# 1049
# 1511
# 2467
# 283
# 3559
# 521
# 4201
# 877
# 1301
# 2749
# 4919
# 1213
# 2039
# 4111
# 3331
# 401
# 2221
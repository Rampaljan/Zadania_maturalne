def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

plik = open("27.03\_2019\pierwsze_przyklad.txt","r")

for line in plik:
    wiersz = line.strip()
    n = int(wiersz)
    n_reversed = int(wiersz[::-1])


    if isPrime(n_reversed):
        print(n)

# #Odpowiedź:
# 701
# 709
# 1033
# 167
# 1109
# 1619
# 1009
# 179
# 1499
# 76001
# 1601
# 31873
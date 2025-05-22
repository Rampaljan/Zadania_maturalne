def is_prime(x):
    dzielniki = 0
    for i in range(1, x+1):
        if x%i == 0:
            dzielniki += 1
    if dzielniki == 2:
        return True
    else:
        return False


plik = open("22.05\_2020\liczby.txt","r")

ile = 0

for line in plik:
    wiersz = line.strip()
    a = int(wiersz)

    if a >= 4000 and a <= 5000:
        if is_prime(a):
            print(a)
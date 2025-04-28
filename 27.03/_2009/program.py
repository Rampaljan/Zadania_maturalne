# Zadanie 5. Liczby pierwsze (8 pkt)
# Liczba pierwsza to liczba naturalna większa od 1, która ma dokładnie dwa dzielniki naturalne:
# 1 i samą siebie.
# Przykłady liczb pierwszych:
# 7
# 11
# 29
# Liczba 21 nie jest liczbą pierwszą, ponieważ oprócz liczby 1 i 21 jej dzielnikami są także
# 3 i 7.
# W pliku o nazwie liczby.txt umieszczono w kolejnych wierszach 500 liczb całkowitych
# dodatnich, po jednej w wierszu, z których każda liczba ma co najwyżej 6 cyfr. Napisz
# program, za pomocą którego otrzymasz tylko te liczby z pliku liczby.txt, które są
# kwadratami liczb pierwszych. Na przykład liczba 49 jest kwadratem liczby pierwszej –
# 2 49 7 = . Wyniki zapisz w pliku zad_5.txt. Twój program powinien działać poprawnie
# również wtedy, gdy plik liczby.txt będzie zawierał 500 innych liczb całkowitych
# dodatnich, o co najwyżej 6 cyfrach, każda liczba w osobnym wierszu.
# Do oceny oddajesz plik o nazwie zad_5.txt oraz plik ...........................................................
# tu wpisz nazwę pliku
# zawierający tekst źródłowy programu

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

plik = open("27.03\_2009\liczby.txt","r")

for line in plik:
    wiersz = line.strip()
    n = int(wiersz)

    for i in range(2, n):
        if i**2 == n and isPrime(i):
            print(n)

# #Odpowiedź:
# 5041
# 1369
# 32041
# 844561
# 4
# 96721
# 9
# 942841
# 49
# 1849
# 528529
# 121
# 961
# 169


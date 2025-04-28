# Anagramy cyfrowe to liczby utworzone z tego samego zestawu cyfr w różnych
# kolejnościach. Przy tym pierwsza cyfra liczby nie może być równa zero.
# Przykład:
# Z liczby 209 zapisanej dziesiętnie można utworzyć 4 anagramy: 209, 290, 902, 920.
# Z liczby dwójkowej 11100 można utworzyć 6 różnych anagramów: 10011, 10101, 10110,
# 11001, 11010, 11100.
# Znajdź wszystkie takie liczby dwójkowe 8-cyfrowe w pliku anagram.txt, z których można
# utworzyć największą liczbę anagramów. Wypisz te liczby w kolejności, w jakiej występują
# w pliku anagram.txt.
# Dla danych z pliku przyklad.txt prawidłową odpowiedzią jest:
# 10001011
# 10111000
# 10100111
# 11111000
# 10011100
# 11100011
# 10111010
# 10100011
# 10011010
# 10110001
# 11011010


plik = open("Depresja\_20.03\_2023\_anagram.txt")

for line in plik:
    wiersz = line.strip()
    if len(wiersz) == 8:

        zera = 0
        jedynki = 0

        for letter in wiersz:
            if letter == "0":
                zera += 1
            if letter == "1":
                jedynki += 1
        
        if zera == jedynki or zera + 2 == jedynki:
            print(wiersz)

#Output:
# 10110101
# 11010100
# 10100101
# 11001001
# 10110100
# 11001101
# 11000110
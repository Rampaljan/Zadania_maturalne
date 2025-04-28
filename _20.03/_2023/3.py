plik = open("Depresja\_20.03\_2023\_anagram.txt")

current = 0
last = 0

biggest_differnece = 0

for line in plik:
    wiersz = line.strip()
    
    liczba = int(wiersz, 2)

    last = current
    current = liczba
    
    print(wiersz, liczba, current, last, biggest_differnece)

    if abs(current - last) > biggest_differnece:
        biggest_differnece = abs(current - last)
        
print(bin(biggest_differnece))


#Output:
# 10011000111001



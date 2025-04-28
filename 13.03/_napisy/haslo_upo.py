plik = open("13.03\_napisy\_napisy.txt", "r")
haslo = ""
for line in plik:
    wiersz = line.strip()
    pair = ""
    for letter in wiersz:
        if letter.isdigit():
            pair += letter
            if len(pair) == 2:
                num = int(pair)
                if 65 <= num <= 90:
                    haslo += chr(num)
                pair = ""
    if haslo.endswith("XXX"):
        break

print(haslo)

#Output:
#LITWOOJCZYZNOMOJATYJESTESJAKZDROWIEILECIETRZEBACENICTENTYLKOSIEDOWIEKTOCIESTRACILNATENCZASWOJSKICHWYCILNATASMIEPRZYPIETYSWOJROGBAWOLIDLUGICENTKOWANYKRETYJAKWAZBOAXXX
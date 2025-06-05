plik = open("05.06\_2015\slowa.txt","r")

_1 = 0
_2 = 0
_3 = 0
_4 = 0
_5 = 0
_6 = 0
_7 = 0
_8 = 0
_9 = 0
_10 = 0
_11 = 0
_12 = 0



for line in plik:
    wiersz = line.strip()

    if len(wiersz) == 1:
        _1 += 1
    elif len(wiersz) == 2:
        _2 += 1
    elif len(wiersz) == 3:
        _3 += 1
    elif len(wiersz) == 4:
        _4 += 1
    elif len(wiersz) == 5:
        _5 += 1
    elif len(wiersz) == 6:
        _6 += 1
    elif len(wiersz) == 7:
        _7 += 1
    elif len(wiersz) == 8:
        _8 += 1
    elif len(wiersz) == 9:
        _9 += 1
    elif len(wiersz) == 10:
        _10 += 1
    elif len(wiersz) == 11:
        _11 += 1
    elif len(wiersz) == 12:
        _12 += 1

print(f"1: {_1}")
print(f"2: {_2}")
print(f"3: {_3}")
print(f"4: {_4}")
print(f"5: {_5}")
print(f"6: {_6}")
print(f"7: {_7}")
print(f"8: {_8}")
print(f"9: {_9}")
print(f"10: {_10}")
print(f"11: {_11}")
print(f"12: {_12}")
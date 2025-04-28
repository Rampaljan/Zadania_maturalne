plik = open("03.04\pesele\dane.txt","r")

listopad = 0
for line in plik:
    wiersz = line.strip()
    actual_msc = ""
    actual_msc += wiersz[2]
    actual_msc += wiersz[3]

    if actual_msc == "11" or actual_msc == "31":
        listopad +=1        

print(f"Osoby z listopada: {listopad}")

# Osoby z listopada: 90

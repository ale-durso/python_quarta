#Scrivere programma che rileva il vendor associato a un MAC address.
file = open("./mac-vendors-export.csv","r",encoding="utf-8") #oggeto file, encoding utf-8 formatta il file
righe = file.readlines()#lista di stringhe che contiene il file
file.close()
byte = input("Dammi i primi 3 byte ->")

for riga in righe[1:]:
    campi = riga.split(",")
    mac = campi[0]
    vendor = campi[1]
    if mac[:len(byte)] == byte:
        print(mac,"->",vendor)

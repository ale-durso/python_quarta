def main():
    file = open("./mac-vendors-export.csv","r",encoding="utf-8") 
    righe = file.readlines()
    file.close()

    mac_adress = []
    vendor = []
    for riga in righe[1:]:
        campi = riga.split(",")
        mac_adress.append(campi[0])
        vendor.append(campi[1])
    mac = input("Inserisci il mac intero ->")
    for m,v in zip(mac_adress,vendor):
        if m[0:8] == mac[0:8]:
            print(f"il produttore è {v}")
#stampare anche la data di produzione
        
   
if __name__=="__main__":#dunder(duble undersocre)
    main()

def main():
    file = open("./mac-vendors-export.csv","r",encoding="utf-8") 
    righe = file.readlines()
    file.close()

    mac_adress = []
    vendor = []
    date = []
    for riga in righe[1:]:
        campi = riga.split(",")
        mac_adress.append(campi[0])
        vendor.append(campi[1])
        date.append(campi[-1])
    mac = input("Inserisci il mac intero ->")
        #gestire anche il - come separatore dei byte del mac
        #usare il metodo replace delle stringhe
        #usare IA per scrivere funzione py che restituisca il mac della schede di rete del wifi del prorpio pc(farlo in una fanzione e integrarla)
    for m,v,d in zip(mac_adress,vendor,date):
        if m[0:8] == mac[0:8]:
            print(f"il produttore è {v}")
        print(f" -> data:  {d}")


#stampare anche la data di produzione
        
   
if __name__=="__main__":#dunder(duble undersocre)
    main()

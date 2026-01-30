#un dizionario in py è una sequenza di coppie chiave:valore
def main():
    elenco = {"AB-32-B4-FF-F4-32":"Luca",
              "65-A0-A4-11-F4-19":"Mario"}
    mac = "AB-32-B4-FF-F4-32"
    if mac in elenco:
        print(elenco[mac])
    else:
        print("mac non trovato")
    #aggiungiamo un nuvo elenco
    elenco["FF-FF-FF-FF-FF-FF"]="broadcast"
    print(elenco)
if __name__=="__main__":
    main()
#dizionari hanno {}, controllo se mac esiste e lo stampo(mac solo con 3)
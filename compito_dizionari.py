#Caricare su un dizionario mac address e vendor a partire dal file csv dei Mac address. Fare la ricerca del vendor usando il dizionario
import uuid
def getMyMac():
    mac = uuid.getnode()
    mac_str = ':'.join(f"{(mac>>i)&0xff:02x}"for i in range(40 ,- 1 ,-8))
    return mac_str
def preparaMac(mac_str):
    mac_str = mac_str.replace("-",":")
    return mac_str.upper()

def main():
    file = open("./mac-vendors-export.csv","r",encoding="utf-8")
    righe = file.readlines() #righe è una lista di stringhe
    file.close()
    dizionario ={}
    dizionarioData ={}
    mac = input("Dammi il mac da ricercare->").upper()
    for riga in righe[1:]: #riga è una stringa
        campi = riga.split(",") #campi -> lista di stringhe
        dizionario[campi[0]] = campi[1] #campi [0] è la chiave, campi[1] è il vendor
        dizionarioData[campi[0]] = campi[-1]
    if mac in dizionario:
       print(dizionario[mac])
       print(dizionarioData[mac])
    myMac = getMyMac()
    myMacPrepared = preparaMac(myMac)
    print3byte = myMacPrepared[:8]
    if (print3byte in dizionario):
        print(f"Il produttore del dispositivo : {myMacPrepared} è {dizionario[print3byte]}")
    else:
        print(f"Il produttore del dispositivo : {myMacPrepared} è ignoto")


if __name__=="__main__":
    main()
    

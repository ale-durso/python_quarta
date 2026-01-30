#Unione di dizionari
#Dati due dizionari, crearne uno nuovo che contenga tutte le chiavi. Se una chiave è
#presente in entrambi, sommare i valori.
def dizUnito(diz,dizFin):
    for chiave in diz:
        if chiave in dizFin:
            dizFin[chiave]+=diz[chiave]
        else:
            dizFin[chiave] = diz[chiave]
            
    return dizFin


def main():
    vendite_gennaio = {"mele": 120, "pere": 85, "arance": 200}
    vendite_febbraio = {"mele": 95, "banane": 150, "arance": 180}
    diz = {}
    diz = dizUnito(vendite_gennaio,diz)
    diz = dizUnito(vendite_febbraio,diz)
    print(diz)

if __name__=="__main__":
    main()

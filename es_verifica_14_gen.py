def temp_media(dati):
    somma = 0
    for i in dati:
        somma += i["temp"]
    return somma/len(dati)
def filtra_citta(dati,nome):
    lista = []
    for i in dati:
        if i["citta"] == nome:
            lista.append(i["temp"])
    return lista
def temp_per_citta(dati):
    diz = {}
    for i in dati:
        if i["citta"] not in diz:
            n = filtra_citta(dati,i["citta"])
            diz[i["citta"]] = n
    return diz
#def temp_per_citta(dati):
    diz = {}
    for i in dati:
        if i["citta"] in diz:
           diz[i["citta"]].append(i["temp"])
        else:

            diz[i["citta"]] = [i["temp"]]
    return diz

def main():
    dati = [
        {"citta": "Milano", "temp": 12},
        {"citta": "Roma", "temp": 18},
        {"citta": "Milano", "temp": 14},
        {"citta": "Napoli", "temp": 20},
        {"citta": "Roma", "temp": 17},
        {"citta": "Napoli", "temp": 22},
        {"citta": "Milano", "temp": 10},
    ]
    media = temp_media(dati)
    print(f"{media:.2f}")
    rilevazioni = filtra_citta(dati,"Milano")
    print(rilevazioni)
    temp_citta = temp_per_citta(dati)
    print(temp_citta)
if __name__=="__main__":
    main()
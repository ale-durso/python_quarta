#Registro presenze
#Un dizionario associa nomi di studenti a liste di date (stringhe) in cui erano presenti.
#Scrivere funzioni per: (a) contare le presenze di uno studente, (b) trovare chi ha più
#presenze, (c) trovare chi era presente in una certa data.
def contaPresenze(diz,studente):
    presenze = 0
    for chiave in diz:
        if chiave == studente:
            for _ in diz[chiave]:
                presenze += 1
    return presenze

def piuPresenze(diz):
    max = None
    max_presenze = 0
    for chiave in diz:
        presenze = contaPresenze(diz,chiave)
        if presenze > max_presenze:
           max = chiave
           max_presenze = presenze
    return max,max_presenze
def trovaPresenza(diz,data):
    presenze = []
    for chiave in diz:
        for dat in diz[chiave]:
            if dat == data:
                presenze.append(chiave)
    return presenze


def main():
    presenze = {
    "Marco": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15"],
    "Sara": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-16", "2024-01-17"],
    "Luca": ["2024-01-10", "2024-01-11"],
    "Elena": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15", "2024-01-16"]
    }
   
    presenz = contaPresenze(presenze,"Marco")
    print(presenz)
    max, max_pres = piuPresenze(presenze)
    print(f"L'alunno/a con maggiori presenze è {max} con {max_pres} presenze")
    trovati = trovaPresenza(presenze,"2024-01-11")
    print(trovati)
if __name__=="__main__":
    main()
#Rimozione duplicati
#Data una lista, restituire una nuova lista contenente gli stessi elementi ma senza duplicati,
#mantenendo l’ordine di prima apparizione.
#elementi = ["mela", "pera", "mela", "banana", "pera", "arancia", "mela"]
def duplicati(lista):
    nuova = []
    for i in lista:
        if i in nuova:
            pass
        else:
            nuova.append(i)
    return nuova
            
def main():
    elementi = ["mela", "pera", "mela", "banana", "pera", "arancia", "mela"]
    nuova = duplicati(elementi)
    print(nuova)
if __name__=="__main__":
    main()
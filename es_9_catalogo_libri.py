#Catalogo libri
#Una lista contiene dizionari con chiavi titolo, autore, anno, prezzo. Scrivere funzioni
#per: (a) cercare libri di un autore, (b) calcolare il prezzo medio, (c) trovare il libro più
#recente.
def cercaLIbro(lista,autore):
    trovati = []
    for libro in lista:             #ogni libro è un dizionario
        if libro["autore"].lower()==autore.lower():
            trovati.append(libro)
    return trovati

def prezzoMedio(lista):
    somma = 0
    for l in lista:
        somma += l["prezzo"]
    return somma/len(lista)

def libroRecente(lista):
    recente = lista[0]
    for l in lista:
        if l["anno"]>recente["anno"]:
            recente = l
    return recente
def main():
    libri = [
    {"titolo": "Il nome della rosa", "autore": "Umberto Eco", "anno": 1980, "prezzo": 15.50},
    {"titolo": "1984", "autore": "George Orwell", "anno": 1949, "prezzo": 12.00},
    {"titolo": "Il pendolo di Foucault", "autore": "Umberto Eco", "anno": 1988, "prezzo": 18.00},
    {"titolo": "Fahrenheit 451", "autore": "Ray Bradbury", "anno": 1953, "prezzo": 11.50},
    {"titolo": "Il mondo nuovo", "autore": "Aldous Huxley", "anno": 1932, "prezzo": 13.00}
    ]
    libro = cercaLIbro(libri,"Umberto Eco")
    print(libro)
    prezzo = prezzoMedio(libri)
    print(prezzo)
    recente= libroRecente(libri)
    print(recente)
    print(f"Il libro piu recente è {recente} del {recente["anno"]}")


if __name__=="__main__":
    main()
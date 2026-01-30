#Filtro prodotti
#Una lista contiene dizionari con chiavi nome, categoria, prezzo. Scrivere una funzione
#che restituisca solo i prodotti di una certa categoria con prezzo inferiore a un valore dato.
def retProdotti(lista,cat,prezzo):
    prodotti = []
    for prod in lista:
        if prod["categoria"].lower() == cat.lower():
            if prod["prezzo"] < prezzo:
                prodotti.append(prod)
    return prodotti
        


def main():
    prodotti = [
    {"nome": "Laptop", "categoria": "elettronica", "prezzo": 899.99},
    {"nome": "Mouse", "categoria": "elettronica", "prezzo": 29.99},
    {"nome": "Scrivania", "categoria": "arredamento", "prezzo": 199.99},
    {"nome": "Tastiera", "categoria": "elettronica", "prezzo": 79.99},
    {"nome": "Sedia", "categoria": "arredamento", "prezzo": 149.99},
    {"nome": "Monitor", "categoria": "elettronica", "prezzo": 349.99}
    ]
    
    prod = retProdotti(prodotti,"elettronica",70)
    print(prod)
if __name__ =="__main__":
    main()
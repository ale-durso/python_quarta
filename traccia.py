def leggi_registro(nome_file):
    """Restituisce un dizionario {nome: [voti]}."""
    file = open(nome_file,"r")
    righe = file.readlines()
    file.close()
    
    diz={}
    for riga in righe:
        campi = riga.split(";")
        print(campi)
        voti = []
        for v in campi[1:]:
            voti.append(int(v)) 
        diz[campi[0]] = voti
    return diz
        

def calcola_media(voti):
    """Restituisce la media di una lista di voti."""
    return sum(voti)/ len(voti)

    

def classifica(registro):
    """
    Restituisce una lista di tuple (nome, media) 
    ordinata per media decrescente.
    """
    lista = []
    for nome in registro:
        media = calcola_media(registro[nome])
        lista.append((media,nome))
    lista.sort(reverse=True)
    listaFin = []
    for media,nome in lista:
        listaFin.append((nome,media))
    return listaFin


def stampa_podio(classifica):
    """Stampa i primi 3 della classifica (usa slicing)."""
    primi = classifica[:3]
    for nome, media in primi:
        print(f"{nome} -> {media}")

def trova_insufficienti(classifica):
    """Restituisce la lista degli studenti con media < 6."""
    insuff = []
    for nome, media in classifica:
        if media < 6:
            insuff.append((nome, media))
    return insuff

def main():
    registro = leggi_registro("./registro.txt")
    for nome in registro:
        print(f"{nome}:{registro[nome]}")
    cls = classifica(registro)
    print(cls)
    stampa_podio(cls)

    print("\nStudenti insufficienti:")
    insuff = trova_insufficienti(cls)
    for nome, media in insuff:
        print(f"{nome} -> {media}")

if __name__=="__main__":
    main()

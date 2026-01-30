#Voti per materia
#Un dizionario associa nomi di materie a liste di voti. Scrivere funzioni per: (a) calcolare
#la media di una materia, (b) trovare la materia con media più alta, (c) aggiungere un
#voto a una materia.
def mediaMateria(diz,materia):
    somma = 0
    for chiave in diz:
        if chiave == materia:
            for i in diz[chiave]:
                somma += i
    return somma/len(diz[chiave])
def mediaPiuAlta(diz):
    max = None
    med_max = 0
    for chiave in diz:
        med = mediaMateria(diz,chiave)
        if med > med_max:
            med_max = med
            max = chiave
    return med_max, max
def aggiungiVoto(diz,materia,voto):
    for chiave in diz:
        if chiave == materia:
            diz[chiave].append(voto)
    #diz[materia].append(voto)          modo più veloce
    
def main():
    voti_materie = {
    "Matematica": [6, 7, 5, 8, 7],
    "Italiano": [7, 8, 7, 6],
    "Inglese": [8, 8, 9, 7, 8],
    "Informatica": [9, 8, 9, 10, 8]
    }
    media = mediaMateria(voti_materie,"Inglese")
    print(media)
    mediaAlta,materia = mediaPiuAlta(voti_materie)
    print(f"La media più alta è {mediaAlta} di {materia}")
    aggiungiVoto(voti_materie,"Inglese",10)
    print(voti_materie)


if __name__ =="__main__":
    main()
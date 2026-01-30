#Voto più frequente
#Dato un dizionario che associa nomi di studenti ai loro voti (un voto per studente),
#trovare quale voto compare più spesso.
def votiFrequenti(diz,diz2):
    for studente in diz:
        voto = diz[studente]
        if voto in diz2:
            diz2[voto] +=1
        else:
            diz2[voto]= 1
    return diz2

def votoFrequente(diz2):
    max = 0
    for voto in diz2:
        if diz2[voto] > max:
            max = diz2[voto]
            votoFin = voto
    return votoFin
  
def main():
    studenti_voti = {
    "Marco": 7,
    "Sara": 8,
    "Luca": 6,
    "Elena": 8,
    "Paolo": 7,
    "Giulia": 8,
    "Andrea": 6,
    "Chiara": 7
    }
    diz={}#la chiave e il voto e il valore e il numero di occorrenze
    voti = votiFrequenti(studenti_voti,diz)
    print(voti)
    votoPiuFrequente = votoFrequente(voti)
    print(votoPiuFrequente)
    print(f"il voto più frequente è {votoPiuFrequente} che è presente {diz[votoPiuFrequente]} volte")
if __name__=="__main__":
    main()

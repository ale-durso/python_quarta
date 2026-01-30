#Squadre e giocatori
#Un dizionario associa nomi di squadre a liste di giocatori. Scrivere funzioni per: (a)
#trovare la squadra con più giocatori, (b) verificare se un giocatore è in una squadra, (c)
#trasferire un giocatore da una squadra all’altra.
def squadraPiuGiocatori(diz):
    max = None
    max_n = 0
    for chiave in diz:
        n = len(diz[chiave])
        if n >max_n:
            max = chiave
            max_n = n
    return max, max_n
def verificaAppartenenza(diz,squadra,giocatore):
    for chiave in diz:
        if chiave == squadra:
            if giocatore in diz[chiave]:
                    return True
                
                
            
    return False

def trasferisciGiocatore(diz,giocatore,squadraN):
    for chiave in diz:
        for g in diz[chiave]:
            if g == giocatore:
                diz[squadraN].append(g)
                diz[chiave].remove(g)
    return diz


def main():
    squadre = {
    "Juventus": ["Vlahovic", "Chiesa", "Locatelli", "Bremer"],
    "Inter": ["Lautaro", "Thuram", "Barella", "Bastoni", "Calhanoglu"],
    "Milan": ["Leao", "Theo", "Reijnders"]
    }
    max_squadra, n_squadra = squadraPiuGiocatori(squadre)
    print(f"La squadra con più giocatori è {max_squadra} con {n_squadra} giocatori")
    presenza = verificaAppartenenza(squadre,"Juventus","Chiesa")
    print(presenza)
    squadre_nuove = trasferisciGiocatore(squadre,"Leao","Juventus")
    print(squadre_nuove)
if __name__ =="__main__":
    main()
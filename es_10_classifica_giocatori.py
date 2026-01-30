#Classifica giocatori
#Una lista contiene dizionari con chiavi nome, punteggio. Scrivere una funzione che
#stampi la classifica ordinata per punteggio decrescente, numerando le posizioni.
def classifica(lista):
    posiz = 1
    while len(lista) > 0:
        max = lista[0]
        for giocatore in lista:
            if giocatore["punteggio"] > max["punteggio"]:
                max = giocatore
        print(f"{posiz} - {max["nome"]} -> {max["punteggio"]}")
        lista.remove(max)
        posiz +=1

def main():
    giocatori = [
    {"nome": "Player1", "punteggio": 4500},
    {"nome": "Player2", "punteggio": 7200},
    {"nome": "Player3", "punteggio": 3100},
    {"nome": "Player4", "punteggio": 8900},
    {"nome": "Player5", "punteggio": 5600}
    ]
    classifica(giocatori)
if __name__=="__main__":
    main()
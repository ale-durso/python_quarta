import random
    #simulare n partite a pari e dispari
    #input utente:
    #-n numero di partite
    #-nome primo giocatore
    #-nome secondo giocatore

    #per simulare le partite usiamo u dizionario
    #es -> n=3
def main():
    nome1 = input("Dammi il nome del primo giocatore->")
    nome2 = input("Dammi il nome del secondo giocatore->")
    n_partite = int(input("Dimmi quante partite->"))
    lista1 = []
    lista2 = []
    lista_nomi = [nome1,nome2]
    for numero in range(n_partite):
        rand1 = random.randint(1,5)
        rand2 = random.randint(1,5)
        lista1.append(int(rand1))
        lista2.append(int(rand2))
    lista_num = [lista1,lista2]
    diz= {}
    for nomi,num in zip(lista_num,lista_nomi):
        diz[num] = nomi

    print(diz)
    listaVincitori = []
    somma = 0
    for l1,l2 in zip(lista1,lista2):
        somma = l1 + l2
        if somma % 2 == 0:
            listaVincitori.append(f"Ha vinto {nome1}")
        else:
            listaVincitori.append(f"Ha vinto {nome2}")
    print(listaVincitori)
if __name__ =="__main__":
    main()
    #le singole giocate sono generate con random.randit()
    #creare una lista che contiene i nomi dei vincitori per ogni partita 
    #ipotesi: il primo giocatore vince se esce pari

#modularità: suddividere il codice in funzioni
#COSTANTE è una variabile globale ma è accessibile da tutte le funzioni soltanto in lettura 
COSTANTE = 3.14
def prima_lettera_maiuscola(stringa):
    """  
    la funzione restituisce stringa con 
    la lettera iniziale maiuscola
    """
    #stringa è una variabile locale alla funzione
    s = stringa[0].upper() + stringa[1:].lower()
    return s
def media(lista):
    """
    La funzione restituisce la media dei valori presenti in lista e il numero di elementi di lista
    """
    somma = 0.
    n_lista = len(lista)
    for val in lista:
        somma = somma + val
    return somma / n_lista, n_lista

def main():
    print(help(prima_lettera_maiuscola))
    nome = input("Dammi un nome")
    print(prima_lettera_maiuscola(nome))
    voti = [7.8,6.8,9.7]
    m,n = media(voti)
    print(m)
    print(n)

if __name__=="__main__":
    main()
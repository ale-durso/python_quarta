#Traduttore di parole
#Dato un dizionario italiano-inglese e una frase in italiano, restituire la frase tradotta. Se
#una parola non è nel dizionario, lasciarla invariata.
def traduttore(diz,frase):
    parole = frase.split()
    #print(parole)
    nuova_frase = ""
    for parola in parole:
        if parola in diz:
            nuova_frase += diz[parola] + " "
        else:
            nuova_frase += parola + " "
    return nuova_frase
def main():
    dizionario = {
    "ciao": "hello",
    "mondo": "world",
    "casa": "house",
    "gatto": "cat",
    "cane": "dog",
    "libro": "book",
    "albero": "tree"
    }
    frase = "ciao mondo il gatto è in casa"
    traduzione = traduttore(dizionario,frase)
    print(traduzione)  
if __name__=="__main__":
    main()

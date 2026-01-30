#Contatore di caratteri
#Data una stringa, costruire un dizionario che associ a ogni carattere il numero di volte
#che compare.
#testo = "abracadabra"
def contatore(string):
    diz = {}
    for i in string:
        if i in diz:
            diz[i] += 1
        else:
            diz[i] = 1
    return diz

def main():
    testo = "abracadabra"
    cont = contatore(testo)
    print(cont)
if __name__=="__main__":
    main()
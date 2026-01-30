#Conta righe e parole
#Leggere un file di testo e stampare: numero di righe, numero di parole, numero di
#caratteri (esclusi gli spazi).
#File testo.txt:
#Python è un linguaggio di programmazione.
#È semplice da imparare e molto potente.
#Viene usato in molti ambiti diversi.
def numeroParole(righe):
    cont_p = 0
    cont_c = 0
    for riga in righe:
        parole = riga.split()
        for parola in parole:
            cont_p += 1
            for car in parola:
                if car != " " and car != "\n":
                    cont_c += 1
    return cont_p, cont_c
def main():
    file = open("es_16_testo.txt","r")
    righe = file.readlines()
    file.close()
    print(len(righe))
    parole, caratteri = numeroParole(righe)
    print(parole)
    print(caratteri)
if __name__=="__main__":
    main()
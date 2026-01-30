def main():
    file = open("./dati.csv","r") #oggeto file
    righe = file.readlines()#lista di stringhe che contiene il file
    file.close()

    prima_riga = righe[0]
    #unpacking = (spacchettamento)
    titolo1, titolo2, titolo3 = prima_riga[:-1].split(",")
    print(titolo1)
    print(titolo2)
    print(titolo3)
    print(righe)
    print(prima_riga)
    for k in righe:
        print(k[:-1].split(","))
if __name__=="__main__":#dunder(duble undersocre)
    main()
    

#leggere tutte le altre righe del file e stamparle, usare un ciclo for pythonico (senza range  )
ALFABETO = "abcdefghijklmnopqrstuvwxyz"

def stampaFrequenze(dizionario,alfabeto):
    """
    La funzione stampa le frequenza delle lettere fornite.
    input:
        -dizionaro: contiene le frequenza assolute per tutte le lettere
        -alfabeto: stringa contenente le lettere di interesse
    Output:
        -None
    """
    for lettera in alfabeto:
        if lettera in dizionario:
            print(f"{lettera} - {dizionario[lettera]}")
        else:
            print(f"{lettera} - 0") 
def main():
    print("Apertura file...")
    file = open("./promessi_sposi.txt","r")
    testo = file.read()
    file.close()
    print(f"Letti : {len(testo)} caratteri")
    print()


    diz = {}
    tot_lettere = 0
    print("="*30)
    for c in testo:
        c=c.lower()
        if c.isalpha():
            tot_lettere += 1
            if c in diz:
                diz[c] += 1
            else:
                diz[c] = 1
    totale = 0
    for k in diz:
        totale += diz[k]
    stampaFrequenze(diz,ALFABETO) 
    for lett in diz:
        freq = (diz[lett] *100)/tot_lettere
        print(f"lettera: {lett} -> {diz[lett]} ->{freq:.2f}%")
    print(tot_lettere)
    print("="*30)

if __name__=="__main__":
    main()
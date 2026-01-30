#Pari e dispari
#Data una lista di interi, scrivere una funzione che restituisca due liste separate: una con
#i numeri pari e una con i dispari.
#numeri = [3, 8, 12, 7, 2, 15, 20, 9, 4]
def pariEdispari(numeri):
    pari=[]
    dispari=[]
    for i in numeri:
        if i % 2 == 0:
            pari.append(i)
        else:
            dispari.append(i)
    return pari,dispari

def main():
    numeri = [3,8,12,7,2,15,20,9,4]
    pari,dispari = pariEdispari(numeri)
    print(f"Pari : {pari}")
    print(f"Dispari: {dispari}")


if __name__=="__main__":
    main()
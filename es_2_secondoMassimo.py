#Secondo massimo
#Scrivere una funzione che trovi il secondo valore più grande in una lista di numeri (senza
#usare sort o sorted).
#valori = [45, 12, 78, 34, 67, 23, 89, 56]
def secondoMassimo(lista):
    max = 0
    for i in lista:
        if max < i:
            max = i
    return max

def main():
    valori = [45, 12, 78, 34, 67, 23, 89, 56]
    max_1 = secondoMassimo(valori)
    valori.remove(max_1)
    max_2 = secondoMassimo(valori)
    print(max_2)

if __name__=="__main__":
    main()
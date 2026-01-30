#Elementi comuni
#Date due liste, restituire una nuova lista con gli elementi presenti in entrambe.
#lista_a = [1, 5, 8, 12, 15, 20]
#lista_b = [3, 5, 10, 12, 18, 20, 25]
def comuni(lista1,lista2):
    elementi_comuni = []
    for i1,i2 in zip(lista1,lista2):
        if i1 in lista2:
            elementi_comuni.append(i1)
    return elementi_comuni

    

def main():
    lista_a = [1, 5, 8, 12, 15, 20]
    lista_b = [3, 5, 10, 12, 18, 20, 25]
    elemcomuni = comuni(lista_a,lista_b)
    print(elemcomuni)

   
if __name__=="__main__":
    main()
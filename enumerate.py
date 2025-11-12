def main_0():
    lista = ["alice","luca","giovanni"]
    nome_max = None
    len_max = 0
    for nome in lista:
        if len(nome)>len_max:
            nome_max = nome
            len_max = len(nome)
    print(nome_max)
    print(len_max)
if __name__=="__main__":#dunder(duble undersocre)
    main_0()

def main():
    lista = ["alice","luca","giovanni"]
  
    for i, nome in enumerate(lista):
       print(f"{i} - {nome}")
if __name__=="__main__":#dunder(duble undersocre)
    print(__name__)
    main()
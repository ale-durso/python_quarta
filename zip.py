def main():
    #modificare il codice sotto per stampare la media di ogniuno, il numero di voti per ogniuno, stamperre il voto max e min
    lista_nomi = ["alice","luca","giovanni"]
    lista_voti = [[6, 10, 5],[7,6],[8,10,9,8]]
    #voglo stampare il voto a fianco di ogni nome
    for nome, voto in zip(lista_nomi,lista_voti):
        somma = 0
        voto_min = voto[0]
        voto_max = voto[0]
        for k in voto:
            somma = somma + k
            if k < voto_min:
                voto_min = k
            if k > voto_max:
                voto_max = k
        media = somma / len(voto)
      
        print(f"{nome}: {voto} media: {media} n° voti: {len(voto)} voto max: {voto_max} voto min: {voto_min}")

if __name__=="__main__":#dunder(duble undersocre)
    main()
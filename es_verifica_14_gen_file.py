def carica_regioni(nome_file):
    righe = nome_file.readlines()
    diz = {}
    for riga in righe:
        campi = riga.split(";")
        diz[campi[0]] = campi[1][:-1]
    return diz

def main():
    file = open("regioni.txt","r")
    diz = carica_regioni(file)
    print(diz)
if __name__ =="__main__":
    main()
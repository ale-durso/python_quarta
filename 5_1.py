# Conta righe e parole


def main():
    file = open("es_16_testo.txt", "r")
    righe = file.readlines()
    file.close()

    numero_parole = 0
    numero_caratteri = 0

    for riga in righe:
        parole = riga.split()

        for parola in parole:
            numero_parole += 1

            for carattere in parola:
                if carattere.isalpha():    
                    numero_caratteri += 1  

    print(f"Numero righe: {len(righe)}")
    print(f"Numero parole: {numero_parole}")
    print(f"Numero caratteri: {numero_caratteri}")

if __name__ == "__main__":
    main()
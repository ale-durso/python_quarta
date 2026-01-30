# Traduttore di parole


def main():
    dizionario = {
        "ciao": "hello",
        "mondo": "world",
        "casa": "house",
        "gatto": "cat",
        "cane": "dog",
        "libro": "book",
        "albero": "tree"
    }

    frase = "ciao mondo il gatto è in casa"

    parole = frase.split()
    nuova_frase = ""

    for parola in parole:
        if parola in dizionario:
            nuova_frase += dizionario[parola] + " "
        else:
            nuova_frase += parola + " "

    print(f"La frase tradotta è: {nuova_frase}")

if __name__ == "__main__":
    main()
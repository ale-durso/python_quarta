# Numeri da file

def main():
    file = open("numeri.txt", "r")
    numeri = file.readlines()
    file.close()

    somma = 0
    count = 0

    minimo = 1000
    massimo = 0

    for num in numeri:
        n = int(num)
        somma += n
        count += 1

        if n > massimo:
            massimo = n
        if n < minimo:
            minimo = n
    
    print(f"Somma: {somma}")
    print(f"Media: {somma / count}")
    print(f"Minimo: {minimo}")
    print(f"Massimo: {massimo}")

if __name__ == "__main__":
    main()
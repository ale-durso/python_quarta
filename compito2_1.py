#Scrivi unu programma che permetta all'utente di effettuare le quattro operazioni aritmetiche.
#Per prima cosa chiede all'utente quale operazione desidera eseguire(0:somma, 1:sottrazione, 2:moltiplicazione, 3:divisione)
#poi chiede all'utente 2 numeri e stampa il risultato dell'operazione
print("0:somma")
print("1:sottrazione")
print("2:moltiplicazione")
print("3:divisione")

scelta = int(input("->"))
n1 = int(input("Dammi il primo numero: "))
n2 = int(input("Dammi il secondo numero: "))

if scelta == 0:
    x = n1 + n2
elif scelta == 1:
    x = n1 - n2
elif scelta == 2:
    x = n1 * n2
elif scelta == 3:
    x = n1 / n2
print(x)
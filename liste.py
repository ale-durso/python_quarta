#in py abbiamo le collezioni.tra le collezioni abbiamo :
#liste,tuple,dizionari,set.

#vediamo le liste

#creare una lista
l = [3, 3.14, 10, "ciao", True]

#per accedere agli elementi ci sono le stesse regole di indicizzazione e slicing delle stringe
print(f"Lultimo elemento della lista è: {l[-1]}")
print(l)
print(f"Tutta la lista senza il primo e lultimo elemento è: {l[1:-1]}")

l.append("NUOVO")#non restituisce nulla ma modifica l
print(l)
l.pop()#rimuove l'ultimo elemento dalla lista
print(l)



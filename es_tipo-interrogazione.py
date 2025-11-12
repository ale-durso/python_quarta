#stringa = input("Dammi una stringa ->")
#stringa = stringa[1:-1]
#stringa = stringa[::-1]
#if stringa[0] == 'C':
#    print("ok")
#else:
# print("no")

#chiedere all' utente una stringa e chiedere un numero intero, sostituire gli ultimi n caratteri con "*"

a = input("Inserisci una stringa-> ")
n = int(input("Dammi un numero->"))
if n <= len(a):
   str = a[:len(a)-n]
   str2 = n * "*"
   strFinale = str + str2
   print(strFinale)
#scrivere che un programma che chiede stringa ,mette in minuscolo e verifica se è palindroma
a=input("Dammi una stringa ->")
a=a.lower()
if a == a[:-1]:
   print(f"La stringa {a} è palindroma")
else :
   print(f"La stringa {a} non è palindroma")

#chiedere un numero e stampare tutti i quadrati fino al numero chiesto
a = int(input("Dammi un numero-> "))
if a>=0:
   for i in range(a+1):
      print(i**2, end=" ")
#scorre stringa e se stringa inizia con c stampa

l=["ciao","python","casa"]
for parola in l:
   if parola[0] == "c":
      print(f"{parola} Inizia con c")
#concantenati
string = "" #sringa vuota
for i in l:
   string = string + " " + i
   print(string)
#invento una lista di stringhe
lista=["luca","mario","giovanni"]
max = 0
nomemax=""
for nome in lista:
   n = len(nome)
   if n > max:
      max = n
      nomemax = nome
 print(nomemax)
#creare una nuova lista ma con i nomi in maiuscolo
lista=["luca","mario","giovanni"]
lista2=[]
for nome in lista:
   n = nome.upper()
print(lista2)   













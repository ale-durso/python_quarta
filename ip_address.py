ip = input("Inserisci un insdirizzo ip ->")
ottetti_str = ip.split(".") #metodo delle stringhe che suddivide una stringa cercando il carattere separatore che gli passiamo
print(ottetti_str)

ottetti = [] #lista vuota
for s in ottetti_str:
    ottetti.append(int(s))
print(ottetti)
print(bin(ottetti[3])[2:])

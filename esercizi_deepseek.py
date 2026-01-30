#n1 = int(input("Dammi un numero-> "))
#n2 = int(input("Dammi un numero-> "))
#operazione = input("Quale operazione? ( + - * /) ->")
#if operazione == "+":
#    ris = n1 +n2
#    print(ris)
#elif operazione == "-":
#    ris = n1 - n2
#    print(ris)
#elif operazione == "*":
#    ris = n1*n2
#    print(ris)
#elif operazione == "/":
#    ris = n1/n2
#    print(ris)
#else:
#    print("ERRORE")
num =input("Dammi un numero binario->")
int(num,2)
print(num)
num2 = int(input("Dammi un numero ->"))
binario = bin(num2)[2:]
while len(binario) < 8:
    binario = "0" + binario
print(binario)
#scrivere un programma che verifica che la somma dei primi n numeri è un quadrato perfetto
import math

a=int(input("Dammi un numero-> "))
somma =0
if a >= 1:
    for i in range(1, 2*a+1, 2):
        print(i)
        somma += i
radiceIntera = math.isqrt(somma)       
print(f"somma: {somma}, quadrato perfetto: {radiceIntera**2 == somma}")


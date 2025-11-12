n = int(input("Inserisci quanti numeri di Fibonacci vuoi-> "))
a, b = 1,1 #inizzializzazione,NON dichiarazione
if n>2:
   for i in range(n):
              
     print(a, end=" - ")
     a, b = b, a+b

elif n==2:
    print(a,end=" - ")
    print(b)
elif n==1:
    print(a)
#completare i vari casi    
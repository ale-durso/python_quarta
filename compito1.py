# Crea un programma in py che chieda all'utente il suo nome e lo stampa sempre con l'iniziale maiuscola
nome = input("Dammi il tuo nome-> ")
print(f"{nome[0].upper()}{nome[1:]}")
#crea un programma in py che chiede all'utente un numero intero e stampa se il numero è divisibile per 2,3,5.(Hint:Usare % per il resto divisione)
num = int(input("Dammi un numero -> "))
if num % 2 == 0:
    print(f"Il numero è divisibile per 2")
elif num % 3 == 0:
    print(f"Il numero è divisibile per 3")    
elif num % 5 == 0:
    print(f"Il numero è divisibile per 5") 
else:
 print(f"{num} non è divisibile per nessuno")          

#crea un programma in py che chiede all'utente una frase e stampi la stringa un carattere si e uno no (caratteri alternati)
frase = input("Scrivi una frase -> ")
print(f"{frase[::2]}")
#crea un programma in py che chiede all'utente una frase e stampi la stringa al contrario
stringa = input("Scrivi una stringa ->")
print(f"{stringa[::-1]}")
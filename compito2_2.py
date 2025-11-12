#Scrivere un programma in py che calcoli quanti sono i quadrati perfetti minoti di 200
import math

cont = 0
n=1

while n**2 < 200:
    cont = cont +1
    n = n +1
print(f"n° quadrati perfetti minori di 200: {cont}")    
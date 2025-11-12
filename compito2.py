#Scrivi un programma in py nel quale assegni alla variabile lista_voti una lista con tutti i tuoi voti(al meno 6 voti).Sfrutta lindicizzazione per:
#stampare la lista senza il primo e l'ultimo voto;
#sostituire il quarto voto con un 10
#stampare i primi 3 voti della lista

lista_voti =[7,5,8,9,10,4,8]
print(f"Lista senza primo e ultimo voto: {lista_voti[1:-1]}")

lista_voti[3] = 10
print(f"Lista con il quarto voto sostituito{lista_voti}")

print(f"Primi 3 voti della lista: {lista_voti[:3]}")
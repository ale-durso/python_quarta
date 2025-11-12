#in python possiamo delimitare con "" oppure con ''
stringa = "ciao mondo!"
print(stringa)
# esemipio di indicizzazione(estraggo 1 elemento(carattere) dalla stringa) della stringa
print(f"L'ultimo carattere della stringa è {stringa[-1]}")

# esempio di slicing delle stringhe (estraggo delle sotto stringhe)
#indice di sinistra incluso mentre quello di destra escluso(2:5 prende ci[AO ]mondo!)
print(f"la sottostringa 2-5 è {stringa[2:5]}.")

#assegnazione multipla(solo in python)(vale per ogni tipo di dato)
nome, cognome = "Mario","Rossi"

x = nome + " " + cognome  #è una stringa(concatenazione)
print(x)

#concatenazione di una stringa con se stessa più volte 

y = (nome+" ")*5
print(y)
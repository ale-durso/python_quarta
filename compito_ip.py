# chiede all' utente un numero binario  gestito 
#se la lunghezza del bin e minore dei bit agiungo a sinistra tanti zero quanti me ne servono
ip = input("Inserisci un insdirizzo ip ->")
ottetti_str = ip.split(".")
print(ottetti_str)
ottetti = [] 
for s in ottetti_str:
    ottetti.append(int(s))
print(ottetti)
for k in ottetti:
    n_bin = bin(k)[2:]
    while len(n_bin) < 8:
        n_bin = '0' + n_bin
    print(n_bin)
    

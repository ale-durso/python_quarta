# Programma che converte un indirizzo IP in una stringa binaria di 32 bit senza zfill

ip = input("Inserisci un indirizzo IP -> ")

ottetti = ip.split(".")

binario_32 = ""

for s in ottetti:
    num = int(s)
    b = bin(num)[2:]  # converte in binario senza '0b'
    # aggiunge gli zeri a sinistra se necessario
    
    while len(b) < 8:
        b = '0' + b
    binario_32 += b

print(f"\nIndirizzo IP: {ip}")
print(f"Stringa binaria 32 bit: {binario_32}")

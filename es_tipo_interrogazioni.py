#lista=["luca","mario","giovanni"]
#lista2=[]
#for nome in lista:
#   lista2.append(nome.upper())
#print(lista2)   

#file = open("./nomeFile","r")
#righe = file.readlines()
#file.close()
#for riga in righe:
#   if(riga[0] == "#"):
#      print(riga)

def oscuraPassword(s):
   nCaratteri = len(s)
   
   return s[0] +((nCaratteri-1)*'*')
def main():
   lista = ["ciao","unoduetre"]
   passwordOscurate = []
   for password in lista:
      passwordOscurate.append(oscuraPassword(password))
   print(passwordOscurate)
if __name__ =="__main__":
   main()
###
m = "A0-FF-51-b3-d1-ff"
campi = m.split("-")
for k in campi:
   if k != "FF":
      print(campi)
###
file = open("vori.csv","r")
righe = file.readlines()
somma = 0
for riga in righe:
   elementi = riga.split(",")
   somma += int(elementi[1])
media = somma/len(righe) 
###
mac = input("Dammi il mac adress->")
file = open("elenco.csv","r")
righe = file.readline()
file.close()
campi = righe.split(",")
for riga in righe:
   if mac == campi[1]:
      print(riga)
###
def trova(mac1,mac2):
   g1 = mac1.split("-")
   g2 = mac2.split("-")
   uguali = 0
   for element1, element2 in zip(g1,g2):
      if element1 == element2:
         uguali += 1
   return uguali
###
file = open("Voto.csv","r")
righe = file.readlines()
file.close()

listaVoti = []
listaNomi = []

for riga in righe[1:]:
   campi = righe.split(",")
   listaVoti.append(campi[0])
   listaVoti.append(campi[0])
print(listaNomi)
print(listaVoti)
#farli interi
###
#chiave nome, valore voto
nomi = ["Luca","Mario","Alice"]
voti=[8,7,10]
diz={}
for n,v in zip(nomi,voti):
   diz[n] = v
print(f"Il voto di alice è {diz["alice"]}")
###
# es csv 192,168,1,1
file = open("file.csv","r")
righe = file.readlines()
file.open()
for riga in righe:
   ip = riga.replace(",",".")
   print(ip)
   campi = riga.split(",")
   ip_rete = campi[-1]
   if ip_rete == "0":
      print(ip_rete)
###
def controllo(ip):
   gruppi = ip.split(".")
   if len(gruppi) == 4:
      return true
   else:
      return false

def main():
   ip = input("Inserisci ip")

if __name__ == "__main__":
   main()
###
file = open("./ip.csv","r")
ip = file readLines()
file.close()
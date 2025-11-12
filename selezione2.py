print("Premi A per inserie.")
print("Premi B per modificare.")
print("Premi C per cancellare.")

tasto = input("-> ")
tasto = tasto.upper() #trasforma tasto in maiuscolo, lower per minuscolo

if tasto == "A":
 print("L'utente vuole inserie")
elif tasto == "B":
  print("L'utente vuole modificare")
elif tasto == "C":
  print("L'utente vuole cancellare")
else:
  print("Tasto non valido")

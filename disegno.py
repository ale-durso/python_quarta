import turtle

def main():
    file = open("disegno.txt","r")
    righe = file.readlines()
    file.close()
    
    for riga in righe:
        campi = riga.split(" ")
        if campi[0] == "avanti":
            turtle.forward(campi[1])
        elif campi[0] == "destra":
            turtle.right(campi[1])
        elif campi[0] == "colore":
            turtle.color(campi[1])
        elif campi[0] == "salta":
            turtle.goto(campi[1],campi[2])
        elif campi[0] == "cerchio":
            pass
    turtle.mainloop()
if __name__=="__main__":
    main()
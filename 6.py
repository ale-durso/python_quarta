# Poligono regolare


import turtle
def sposta(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def poligono(lati, lunghezza):
    angolo = 360 / lati

    for _ in range(lati):
        turtle.forward(lunghezza)
        turtle.left(angolo)
def main():
    nPoligoni = 4
    lato = 90
    shift = 180
    x_0,y_0 = -340, -lato/2
    for i in range(nPoligoni):
        y=y_0
        x=x_0 + shift * i
        sposta(x,y)
        poligono(i+3,lato)
    turtle.mainloop()

if __name__=="__main__":
    main()
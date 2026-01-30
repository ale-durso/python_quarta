#scrivere un programma che disegna 100 quadrati casuali(posizione,colore,lato)
import turtle
import random

class Quadrato:
    def __init__(self, lato, x, y, colore):
        self.lato = lato
        self.x = x
        self.y = y
        self.colore = colore

    def __str__(self):
        #deve ritornare una stringa
        return f"({self.x}, {self.y})"

    def area(self):
        return self.lato ** 2

    def perimetro(self):
        return self.lato * 4

    def disegna(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.colore)

        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(self.lato)
            turtle.right(90)
        turtle.end_fill()


def main():
    turtle.speed(0)
    turtle.colormode()
    COLORI = ["red","blue","green","yellow"]
    for _ in range(100):
        #colore = random.choice(COLORI)
        colore = (random.random(),random.random(),random.random())#tupla, immutabile una volta creata
        lato = random.randint(10, 40)
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)

        q = Quadrato(lato, x, y, colore)
        q.disegna()

    turtle.mainloop()


if __name__ == "__main__":
    main()

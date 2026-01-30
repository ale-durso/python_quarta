import turtle

def main():
    n = int(input("Dammi un numero->"))

    for l in range(n):
        turtle.forward(100)
        turtle.left(360/n)
    turtle.mainloop()
if __name__=="__main__":
    main()
#chiedere all utente numero > 2 e disegnare il poligono regolare a n lati

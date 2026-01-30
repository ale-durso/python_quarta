#in Python tutto è un oggetto! anche int o float sono oggetti!
#Anche le funzioni sono oggetti.

#Creare classi ci permettie di creare nuovi oggetti!
import math
import turtle
class Punto():
    #costruttore
    def __init__(self,x,y): #self è come this in java
        #attributi (in Python tutto è pubblico)
        self.x = x
        self.y = y
    def __str__(self):
        #deve ritornare una stringa
        return f"({self.x}, {self.y})"
    def distanza_origine(self):
        #ritorna la distanza del punto da l'origine 0,0
        return math.sqrt(self.x**2 + self.y**2)
    def scambia_coordinate(self):
        #questo metodo ritorna un nuovo punto con x e y scabiati
        x,y = self.y, self.x
        return Punto(x,y)
    def disegna(self):
        #questo metodo usa turte per disegnare il punto
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.circle(1)
        turtle.mainloop()
    def distanza(self,altro):
        #questo metodo restituisce la distanza tra il punto e altro
        #altro è una istanza di un altro punto
        return math.sqrt((self.x-altro.x)**2 + (self.y - altro.y)**2)
def main():
    a = Punto(1,2) #istanzza di punto in coordinate 1,2
    b = Punto(3,4)
    print(a)
    print(a.scambia_coordinate())
    print(f"Il punto dista {a.distanza_origine():.2f} dall' origine")
    print(f"Distanza da b: {a.distanza(b)}")
    a.disegna()
if __name__ =="__main__":
    main()

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print("Punto({0}, {1})".format(self.x, self.y))

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        return (dx ** 2 + dy ** 2) ** 0.5

p1 = Punto(3, 4)
p2 = Punto(7, 1)

p1.mostrar()  
p2.mostrar()  

print("La distancia entre p1 y p2:", p1.calcular_distancia(p2))  

p1.mover(1, 1)
p1.mostrar()  

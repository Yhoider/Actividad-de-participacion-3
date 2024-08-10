class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangulo:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def calcular_perimetro(self):
        
        lado1 = abs(self.punto2.x - self.punto1.x)
        lado2 = abs(self.punto2.y - self.punto1.y)

        
        perimetro = 2 * (lado1 + lado2)
        return perimetro

    def calcular_area(self):
        
        lado1 = abs(self.punto2.x - self.punto1.x)
        lado2 = abs(self.punto2.y - self.punto1.y)
  
        area = lado1 * lado2
        return area

    def es_cuadrado(self):
        
        lado1 = abs(self.punto2.x - self.punto1.x)
        lado2 = abs(self.punto2.y - self.punto1.y)

        
        return lado1 == lado2

punto1 = Punto(1, 1)
punto2 = Punto(4, 4)


rectangulo = Rectangulo(punto1, punto2)


print("Perímetro:", rectangulo.calcular_perimetro())
print("Área:", rectangulo.calcular_area())
print("Es un cuadrado:", rectangulo.es_cuadrado())
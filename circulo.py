class Circulo:
    def __init__(self, cx, cy, radio):
        self.centro = (cx, cy)
        self.radio = radio

    def area(self):
        return 3.14159 * (self.radio ** 2)

    def perimetro(self):
        return 2 * 3.14159 * self.radio

    def pertenece(self, px, py):
        distancia = ((px - self.centro[0]) ** 2 + (py - self.centro[1]) ** 2) ** 0.5
        return distancia <= self.radio

circulo = Circulo(3, 3, 5)
print("area es", circulo.area())
print("perpmetro es", circulo.perimetro())
print("el punto (2, 3) pertenece al circulo", circulo.pertenece(2, 3))
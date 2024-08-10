class vehículo:

    def __init__(self, velocidad_maxima, kilometraje) :
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

vehículo = vehículo (180, 100000)

print ("La velocidad_maxima del vehicculo es:", vehículo.velocidad_maxima, "Kilometros")
print ("El kilometraje del vehicculo es:", vehículo.kilometraje, "Km/h")

        
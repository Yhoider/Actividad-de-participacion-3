class Carta:
    corazon = "Corazon"
    diamante = "Diamantes"
    trebol = "Trébol"
    picas = "Picas"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

    def mostrar(self):
        print("{0} de {1}".format(self.valor, self.pinta))


carta1 = Carta("As", Carta.diamante)
carta2 = Carta("Rey", Carta.trebol)

carta1.mostrar()  
carta2.mostrar()  

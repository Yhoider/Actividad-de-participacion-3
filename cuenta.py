class cuentabancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def deposito (self, deposito):
        self.deposito = deposito
        print ("Se deposito {}".format (deposito))
        self.balance += deposito
        print ("El dinero en la cuenta es {}".format(self.balance))


    def retiro (self, retiro):
        self.retiro = retiro
        while retiro > self.balance:
            print ("No tienes suficente dinero en la cuenta para hacer este retiro ")
            retiro = int(input("Ingresa una cantidad inferior:"))
            if retiro <= self.balance:
                break
        
        print ("Se retiro {} de la cuenta".format(retiro))
        self.balance -= retiro
        print("Quedan {} en la cuenta".format(self.balance))

    def cuota_manejo (self):
        _cuota_manejo = self.balance * 0.02
        self.balance -= _cuota_manejo
        print("Cuota de manejo de {0} aplicada. Nuevo balance: {1}".format(_cuota_manejo, self.balance))

    def mostrar_detalles (self):
        print ("Nombre del propietario:",self.propietarios)
        print ("Dinero en la cuenta:", self.balance)
        print ("Numero de cuenta:", self.numero_cuenta)
        

cuenta = cuentabancaria (190778, "Javier Palacios", 10000)
cuenta.deposito (20000)
cuenta.retiro (10000)
cuenta.cuota_manejo ()
cuenta.mostrar_detalles ()
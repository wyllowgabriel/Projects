class vehiculos():

    def __init__(self, marca, modelo):
        
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arranacar(self):

     self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True
    
    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \n Marcha: {self.enMarcha} \nAcelerando: {self.acelera} \n Frenando: {self.frena}")

class furgoneta(vehiculos):

    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta esta cargada."
        else:
            return "La furgoneta no esta cargada."

class moto(vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy hacer el caballito."
    
    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \n Marcha: {self.enMarcha} \nAcelerando: {self.acelera} \n Frenando: {self.frena}\n {self.hcaballito}")

class vElectricos(vehiculos):
    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)

        self.autonomia = 100
    
    def cargaEnergia(self):

        self.cargando = True

miMoto = moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado()

mifurgoneta = furgoneta("Renout", "Kangoo")

mifurgoneta.arranacar()

mifurgoneta.estado()

mifurgoneta.carga(True)

class bicicletaElectrica(vElectricos, vehiculos):
    pass

miBici = bicicletaElectrica("Orbea", "Hhd")
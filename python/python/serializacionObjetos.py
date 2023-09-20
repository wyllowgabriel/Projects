import pickle

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


coche1 = vehiculos("Mazda", "MX5")

coche2 = vehiculos("seat", "Leon")

coche3 = vehiculos("Renault", "Megane")

coches = [coche1, coche2, coche3]

fichero = open("losCoches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)

ficheroApertura = open("losCoches", "rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:

    print(c.estado())
class Coche():
  
    def __init__(self):

        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if(self.__enMarcha):
            chequeo = self.__chequeoInterno()

        if(self.__enMarcha and chequeo):
            return "El coche esta en marcha."
        
        elif(self.__enMarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar."
        
        else:

            return "El coche esta parado"  


    def estado(self):
       print(f"El coche tiene {self.__ruedas} ruedas. Un ancho de {self.__anchoChasis} y un largo de {self.__largoChasis}") 

    
    
    def __chequeoInterno(self):
        print("Realizando chequeo interno")

        self.gasolina = "Ok"
        self.aceite = "Ok"
        self.puertas = "Cerradas"

        if (self.gasolina == "Ok" and self.aceite == "Ok"  and self.puertas == "Cerradas"):

            return True

        else:

            return False



miCoche = Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("A continuación creamos otro objeto")

miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche2.estado()

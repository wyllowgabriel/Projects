import pickle

class persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(f"Se ha creado una persona con el nombre de: {self.nombre}")

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class listaPersonas:

    personas = []

    def __init__(self):
       
        listaDePersonas = open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        
        except:
            print("El fichero esta vacío.")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasFichero()

    def mostrarPersonas (self):
        for p in self.personas:
            print(p)

    def guardarPersonasFichero(self):
        listaDePersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

miLista = listaPersonas()
persona = persona("Sandra", "femenino", 29)
miLista.agregarPersonas(persona)

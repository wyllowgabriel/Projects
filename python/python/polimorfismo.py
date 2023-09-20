class coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas.")


class moto():

    def desplazamiento(self):
        print("Me desolazo utilizando dos ruedas.")


class camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas.")


# Ejemplo de polimorfismo
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo = camion()
# Al llamar este metodo y pasar este objeto a parámetro este obijeto (miVehiculo) se armazena en (vehiculo) y la margia del polimorfismo hace que se trasforme en um metrodo camión. 
desplazamientoVehiculo(miVehiculo)
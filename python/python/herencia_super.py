class persona():

    def __init__(self, nombre, edad, lugarResidencia):
        
        self.nombre = nombre

        self.edad = edad

        self.lugarResidencia = lugarResidencia

    def descripcion(self):
        
        print(f"Nombre: {self.nombre} edad: {self.edad} Residencia: {self.lugarResidencia}")


class empleado(persona):
        
    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residenciaEmpleado):

        super().__init__(nombreEmpleado, edadEmpleado, residenciaEmpleado)

        self.salario = salario

        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print(f"Salario: {self.salario} Antiguedad: {self.antiguedad}")

Manuel = empleado(1500, 15, "Manuel", 55, "Colombia")

Manuel.descripcion()
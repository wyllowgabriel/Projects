def evaluacion(nota):
    valoracion = "aprovado"
    if nota <5:
        valoracion = "suspenso"
    return valoracion

print(evaluacion(4))

"de otra forma"

print("Student grade evaluation program.")

studentNote = int(input("Put your final note: "))

def evaluacion(nota):
    valoracion = "Passed"
    if nota <5:
        valoracion = "suspense"
    return valoracion

print(evaluacion(studentNote))
print("Scholarship program of the year 2022.")
distanciaEscolar = int(input("Put the distance to the school in km: "))
print(distanciaEscolar)

numeroHermanos = int(input("Put the number of brothers:"))
print(numeroHermanos)

salarioFamiliar = int(input("Put the annual family salary: "))
print(salarioFamiliar)

if distanciaEscolar > 40 and numeroHermanos > 2 and salarioFamiliar <= 20000:
    print("You have the right to a scholarship.")
else:
    print("You aren't entitled to a scholarship.")


"Agregando el operador or"

print("Scholarship program of the year 2022.")
distanciaEscolar = int(input("Put the distance to the school in km: "))
print(distanciaEscolar)

numeroHermanos = int(input("Put the number of brothers:"))
print(numeroHermanos)

salarioFamiliar = int(input("Put the annual family salary: "))
print(salarioFamiliar)

if distanciaEscolar > 40 and numeroHermanos > 2 or salarioFamiliar <= 20000:
    print("You have the right to a scholarship.")
else:
    print("You aren't entitled to a scholarship.")

"Operador in"

print("Opitative subjects of the year 2022.")
print("Computer graphics - Software testing - Usability and accessibility")
option = input("Put the subject  chosen: ")
subjects = option.lower()

if subjects in ("computer graphics", "software testing", "usability and accessibility"):
    print(f"Chosen subject: {subjects}")
else:
    print("The chosen subject is not available.")
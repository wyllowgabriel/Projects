def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def divide(num1, num2):
#Ejemplo de lo que tengo que hacer si se ocurre una excepción.
    try:
        return num1/num2
        # Hay que poner el tipo de error
    except ZeroDivisionError:
        print("Cannot be divided by 0")
        return "Wrong operation"
while True:
    try:
        op1 = int(input("Put the first number: "))
        op2 = int(input("Put the second number: "))
        break
    except ValueError:
        print("The entered value are not correct")
operacion = input("Put the operation to realize (sume, subtraction, multiplication, division): ")

if operacion == "sume":
    print(suma(op1,op2))
elif operacion == "subtraction":
    print(resta(op1, op2))
elif operacion == "multiplication":
    print(multiplicar(op1, op2))
elif operacion == "division":
    print(divide(op1, op2))
else:
    print("Operation not contemplated.")

print("Operation executed.")

# Otro ejemplo

def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("Negative ages are not allowed.")
    if edad < 20:
        return "You are very young."
    elif edad < 40:
        return "You are young."
    elif edad < 65:
        return "You are mature."
    elif edad < 80:
        return "Take care of yourself."
    elif edad < 100:
        return "Watch out, raise you arm God cam."
print(evaluaEdad())
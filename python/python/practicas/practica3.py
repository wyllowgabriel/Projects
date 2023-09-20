def sume():
    return firstNumber + secondNumber

def subtract():
    return firstNumber - secondNumber

def multiplication():
    return firstNumber * secondNumber

def division():
    return firstNumber / secondNumber

def integerDivision():
    return firstNumber // secondNumber

def exponent():
    return firstNumber ** secondNumber

def module():
    return firstNumber % secondNumber

def getNumberFromUser(userMessage):
    return int(input(userMessage))

def getNumbersFromUser():
    firstNumber = getNumberFromUser("Put the first number:")
    secondNumber = getNumberFromUser("Put the second number:")
    return firstNumber, secondNumber

def option():
    option = getNumberFromUser("Choose one of the following options. \n 1. Sume\n 2. Subtract\n 3. Multiplication\n 4. Division\n 5. integer division\n 6. Exponent\n 7. Module\n ")
    return option

option = option()
firstNumber, secondNumber = getNumbersFromUser()
if option == 1:
    print(sume())
elif option == 2:
    print(subtract())
elif option == 3:
    print(multiplication())
elif option == 4:
    print(division())
elif option == 5:
    print(integerDivision())
elif option == 6:
    print(exponent())
else:
    print(module())

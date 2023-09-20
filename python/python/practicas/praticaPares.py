def checkAndPrint(num):
    result=checkNumber(num=num)
    if result:
        printNumber(num=num)

def printNumber(num, segundo=6):
    print(f"{num}-{segundo}")

def checkNumber(num):
    return ( (num % 2) == 0 )

def getNumberFromUser(userMessage):
    return int(input(userMessage))

def getNumbersFromUser():
    firstNumber = getNumberFromUser("Put the fist number: ")
    secondNumber = getNumberFromUser("Put the second number greater than the first: ")
    if firstNumber > secondNumber:
        print("The fist number is higher then second.")
    return firstNumber, secondNumber
   
firstNumber, secondNumber = getNumbersFromUser()

while firstNumber < secondNumber:
    checkAndPrint(firstNumber)
    firstNumber = firstNumber + 1
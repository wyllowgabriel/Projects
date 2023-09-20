print("Hello, welcome to the program to determine which the greater number between three numbers.\n")
firstNumber = int(input("Put the first number: "))
secondNumber = int(input("Put the second number: "))
thirdNumber = int(input("Put the third number: "))

if firstNumber > secondNumber and thirdNumber:
    print("The largest number is (", firstNumber, ").")
elif secondNumber > thirdNumber :
    print("The largest number is (", secondNumber,").")
elif firstNumber == secondNumber == thirdNumber:
    print("All numbers are the same.")
else :
    print("The largest number is (",thirdNumber,").")


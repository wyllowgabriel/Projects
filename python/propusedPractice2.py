print("Welcome to the program that  determines  if a number is ever or odd.")
number = int(input("Please put a whole number: "))

module = number % 2

if module ==  0:
    print("The number (",number, ") is over.")
else:
    print("The number (", number, ") is odd.")
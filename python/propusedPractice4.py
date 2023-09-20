print("Single variable calculator")

print("\n * Option menu * \n")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Integer division")
print("6. Exponent")
print("7. Modue or remainder")
option = int(input("Put the option desired: "))

if option == 1:
    print("You chose sum.")
    number = int(input("Put the first number: "))
    number += int(input("Put the second number: "))
    print ("The result of the sum is:" , number)
elif option == 2:
    print("You chose subtraction.")
    number = int(input("Put the first number: "))
    number -= int(input("Put the second number: "))
    print("The result of the subtraction is:", number,)
elif option == 3:
    print("You choose multiplication.")
    number = int(input("Put the first number: "))
    number *= int(input("Put the first number: "))
    print("The result of the multiplication is:", number,)
elif option == 4:
    print("You choose division.")
    number = float(input("Put the first number: "))
    number /= float(input("Put the second number: "))
    print("The result of the division is:", number,)
elif option == 5:
    print("You choose interger division.")
    number = int(input("Put the first number: "))
    number //= int(input("Put the second number: "))
    print("The result of the interger division is:", number,)
elif option == 6:
    print("You choose exponent.")
    number = int(input("Put the first number: "))
    number **= int(input("Put the second number: "))
    print("The result of the exponet is", number,)
elif option == 7:
    print("You choose modue or remainder.")
    number = int(input("Put the first number: "))
    number %= int(input("Put the second number: "))
    print("The result of the exponet is:", number,)
else:
    print("The option does not exist.")
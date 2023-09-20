from unittest import result


multiplier = int(input("What multiplication table do you want to see?: "))

print("The table of 5 is: ")
for number in range(0,11):
    result = multiplier * number
    print(f"{multiplier} x {number} = {result}")

print("End.")
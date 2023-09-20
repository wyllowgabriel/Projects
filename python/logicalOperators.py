"Conjunction"

print("Conjuntion (and)")

numberOne = int(input("Put a number greater than 2 and less than 5: "))

if numberOne > 2 and numberOne < 5:
    print("The number", numberOne, " meets the condition.\n")
else:
    print("The number", numberOne, " does not meet the condition.\n")

"disjunction"
print("disjuntion (or)")
word = input("To fulfill the condition write yes or si: ")

if word == "yes" or word == "si":
    print("The condition has been met.")
else:
  print("The condicional has not been met.")

"Denial"
print("Denial (not)")

numberOne = int(input("Put a number same to 5: "))
if not numberOne == 5:
    print("\n The nu,ber is different  from 5 and the condition is met.\n")
else :
    print("\n The number is same from 5 and the condition is not met.\n")
    



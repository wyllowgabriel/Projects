print("Hello, welcome to the vacation system of the multinational company Rappi.\n")
name = input("Put your name: ")
keyCode = int(input("Enter the password of the department: "))
yearsWorked = float(input("Put how many years they work in the company: "))

if keyCode == 1:
    if yearsWorked >= 1 and yearsWorked < 2:
        print(name,"you heve 6 days of vacations.")
    elif yearsWorked >= 2  and yearsWorked <= 6: 
         print(name, "you have 14 days of vacations.")
    elif yearsWorked >= 7:
        print(name, "you have 20 days of vacations.")
    else:
        print(name, "you don't have vacation days." )
elif keyCode == 2:
    if yearsWorked >= 1 and yearsWorked < 2:
        print(name, "you heve 7 days of vacations.")
    elif yearsWorked >= 2  and yearsWorked <= 6: 
         print(name, "you have 15 days of vacations.")
    elif yearsWorked >= 7:
        print(name, "you have 22 days of vacations.")
    else:
        print(name, "you don't have vacation days." )
elif keyCode == 3:
    if yearsWorked >= 1 and yearsWorked < 2:
        print(name, "you heve 10 days of vacations.")
    elif yearsWorked >= 2  and yearsWorked <= 6: 
         print(name, "you have 20 days of vacations.")
    elif yearsWorked >= 7:
        print(name, "you have 30 days of vacations.")
    else:
        print(name, "you don't have vacation days." )
else:
    print ("Password not found")
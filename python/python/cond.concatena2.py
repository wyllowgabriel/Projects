"condicional con concatenación"
edad = 7 

if 0<edad<100:
    print("The age is correct")
else :
    print("The age is incorrect")


"Otro ejemplo"

salaryPresident = int(input("Put the salary of the president: "))
print(f"Salary president: {salaryPresident}")

salaryDirector = int(input("Put the salary of the director: "))
print(f"Salary director: {salaryDirector}")

salaryBoss = int(input("Put the salary of the boss: "))
print(f"Salary boss: {salaryBoss}")

salaryAdministrative = int(input("Put the salary of the administrative: "))
print(f"Salary administrative: {salaryAdministrative}")

if salaryAdministrative < salaryBoss < salaryDirector  < salaryPresident:
    print("Everything works correctly.")
else:
    print("Something is wrong in this company.")
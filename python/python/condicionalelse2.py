print("Access verification")

edadUsuario=int(input("Put your age: "))

if edadUsuario < 18:
    print("Sorry, you can't pass.")
elif edadUsuario > 100:
    print("The age is incorrect.")
else:
    print("You can pass.")

print("The program has ended")

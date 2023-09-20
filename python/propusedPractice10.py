longitud = int(input("How many integers will the list contain? "))

list = []

x = 0

number = 0
while x < longitud:
    number = int(input("Put an integer: "))
    list.append(number)
    #list.append(int(input("Put an integer:")))
    x = x + 1

print(list)
print(f"The sume of the numbers of thr list is: {sum(list)}")

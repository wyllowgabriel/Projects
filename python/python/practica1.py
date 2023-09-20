import os

myPath = os.path.dirname(__file__)

myList = os.listdir(myPath)

length = len(myList)

x = 0

while x < length:
    print(myList[x])
    x = x + 1

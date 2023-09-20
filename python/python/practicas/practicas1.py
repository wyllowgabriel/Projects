def getPersonInfo():
    dataName={}
    number = input("Put your phone number: ")
    # name = input("Put your name: ")
    # address = input("Put in street name: ")
    dataName["number"] = number
    dataName["name"] = input("Put your name: ")
    dataName["address"] = input("Put in street name: ")
    return dataName

def renderMenu():
    fMenu = open("menu.txt", "r")
    contents = fMenu.read()
    fMenu.close()
    print(contents)
    return contents
    

dataFilePath="dataName.json"
portada = "Restaurant app"
print(portada.center(30,"-"))

option = int(input("\n Option: \n 1. Delivery \n 2. Orders \n 3. Bar \n 4. See orders \n Which option do you want? "))

if option == 1:
    option1 = 2
    while option1 == 2:

        portada1 = "Delivery menu"
        print(portada1.center(30,"-"))
        print("\n Do you have registration?")
        option5 = int(input("1.Yes\n2.No\n"))
        
        if option5 == 2:
            import json, os
            dataBase = dict()
            if os.path.exists(dataFilePath):
                tf = open(dataFilePath, "r")
                dataBase = json.load(tf)
                tf.close()

            dataName=getPersonInfo()
            dataBase[dataName["number"]]=dataName
            tf = open(dataFilePath, "w")
            json.dump(dataBase,tf)
            tf.close()

            renderMenu()
            menu = input("Select Menu number: ")
        elif option5 == 1:
            number1 = input("Put your phone name: ")
            import json, os
            
            
        else:
            print("The option does not exist, try again.")
            
        



        #portada2 = "Address"
        #print(portada2.center(30,"-"))

        #name = input("Name: ")
        #Address = input("Address: ")
        #number = int(input("Phone number: "))
        #Note = input("Note: ")
        #option1 = int(input("Conclude? \n 1.Yes \n 2.No "))
    
    print("Order placed.")
elif option == 2:
    portada3 = "Table orders"
    option2 = 2
    while option2 == 2:
        print(portada3.center(30,"-"))
        table = int(input("Put the number of the table: "))
        request = input("Request: ")
        tables = {table:request}
        observation = input("Observation: ")
        observations = {table:observation}
        option2 = int(input("Conclude? \n 1.Yes \n 2.No "))
elif option == 3:
    option3 = 2
    while option3 == 2:
        portada4 = "Bar"
        print(portada4.center(30,"-"))
        numberBar = int(input("What is the order number?"))
        requestBar = input("Request: ")
        requestBar1 = {numberBar:requestBar}
        option3 = int(input("Conclude? \n 1.Yes \n 2.No"))
else :
    portada5 = "See orders"
    print(portada5.center(30,"-"))
    option4 = int(input("What do you want to see?\n 1.Delivery orders\n 2.Orders tables\n 3.Bar orders"))

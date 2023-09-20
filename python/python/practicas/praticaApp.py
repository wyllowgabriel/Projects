#def getPersonInfo():
    dataName = {}
    putNumber()
    dataName ["number"] = number
    dataName ["Name"]= input("Put your name")
    dataName ["address"] = input("Put your address")
    return dataName


#def putInformationTables():
    dataTables = {}
    tableNumber = getNumberFromUser("Put the number table: ")
    dataTables ["tableNumber"] = tableNumber
    dataTables ["order"] = input("Put the menu number:")
    dataTables ["observations:"]
    return dataTables


#def putNumber():
    number = input("Put your number: ")
    return number

#def renderMenu():
    fMenu = open("menu.txt","r")
    contents = fMenu.read()
    fMenu.close()
    print(contents)
    return contents

#def getNumberFromUser(userMessage):
    return int(input(userMessage))

#def option1():
    option = getNumberFromUser("\n Option: \n 1. Delivery \n 2. Orders \n 3. Bar \n 4. See orders \n Which option do you want? ")
    return option

#def optionYesNo():
    option1 = getNumberFromUser("1.Yes\n2. No ")
    return option1

#def coverPage():
    return print(portada.center(30,"-"))

#def importJson():
    dataFilePath = "datadataName.json"
    import json,os
    dataBase = dict()
    if os.path.exists (dataFilePath):
        tf = open(dataFilePath, "r")
        dataBase = json.load(tf)
        tf.close()

#def importJsonTable():
    dataFilePathTable = "datatables.json"
    import json,os
    dataBaseTables = dicTables()
    if os.path.exists(dataFilePathTable):
        tf = open(dataFilePathTable, "r")
        dataBaseTables = json.load(tf)
        tf.close()

 #def rendermenu1():
    renderMenu()
    menu = getNumberFromUser("Select menu number: ")
    return menu

 #def putNumber():
    number = input("Put your number: ")
    return number

#def writingSavingDate():
    dataName = getPersonInfo()
    dataBase[dataName["number"]] = dataName
    tf = open(dataFilePath, "w")
    json.dump(dataBase, tf)
    tf.close()

#def wrintingSavingTabledate():
    dataTables = putInformationTables()
    dataBaseTables[dataTables["tableNumber"]] = dataTables
    tf = open(dataFilePathTable, "w")
    json.dump(databasetable, tf)
    tf.close()
    

def conterBar(conter):
    from io import open
    conterBar = open("conterBar.txt","w")
    conter 
    conterBar.write(conter)
    conterBar.close()

     
def deliveryMenu():
    option1 = 2
    while option1 == 2:
        portada = "Delivery menu"
        coverPage()
        print("Do you have to register?")
        optionYesNo()
        if option1 == 1:
            importJson()
            writingSavingDate()
            rendermenu1()
        elif option1 == 2:
            putNumber()
            importJson()
            #print(dataName[number[name]])
            #print(dataName[number[address]])
            rendermenu1()
        else:
            print("The option does not exist, try again.")
        optionYesNo()     

def tableOrders():
    option1 = 2
    while option1  == 2:
        portada = "Table orders"
        coverPage()
        putInformationTables()
        importJsonTable()
        wrintingSavingTabledate()
        renderMenu()
        optionYesNo()

def barOrders():
    option1 = 2
    while option1 == 2:
        portada = "Bar"
        coverPage()





portada = "Restaurant app"
coverPage()
option = option1()
if option == 1:
    deliveryMenu()
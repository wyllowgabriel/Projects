def renderMenu():
    from io import open

    fmenu = open("menu1.txt", "r")
    contents = fmenu.read()
    fmenu.close()
    print(contents)
    return contents

def getPersonInfo():
    dataName = {}
    number = input("Put your number: ")
    dataName["number"] = number
    dataName["name"] = input("Put your name: ")
    dataName["andress"] = input("Put in street name: ")
    return dataName

def getNumberFronUser(userMessage):
    return int(input(userMessage))

def putInformationTables():
    dataTables = {}
    tableNumber = getNumberFronUser("Put the number table: ")
    dataTables ["tableNumber"] = tableNumber
    dataTables ["order"] = input("Put the menu order: ")
    dataTables ["observatios"] = input("Put the observation: ")
    return dataTables

def putInformationBar():
    dataBar = {}
    barNumber = getNumberFronUser("What is the number order?")
    dataBar["barNumber"] = barNumber
    dataBar["request:"] = input ("request: ")
    return dataBar


def option():
    option = getNumberFronUser("\n Option: \n 1. Delivery \n 2. Orders \n 3. Bar \n 4. See orders \n Which option do you want? ")
    return option

def optionYesNo():
    option1 = getNumberFronUser("1. Yes\n2. No\n")
    return option1

#def coverPage():
    return print(portada.center(30,"-"))

def importJson():
    dataFilePath = "dataDataName.json"
    import json,os
    dataBase = dict()
    if os.path.exists (dataFilePath):
        tf = open(dataFilePath, "r")
        dataBase = json.load(tf)
        tf.close()
    dataName = getPersonInfo()
    dataBase[dataName["number"]] = dataName
    tf = open(dataFilePath, "w")
    json.dump(dataBase,tf)
    tf.close()

def importJsonRead():
    dataFilePath = "dataDataName.json"
    import json
    with open(dataFilePath, "r") as j:
        dataBase = json.load(j)
    return dataBase

def importJsonTable():
    dataFilePathTable = "dataTables.json"
    import json, os
    dataBaseTable = dict()
    if os.path.exists (dataFilePathTable):
        tf = open(dataFilePathTable, "r")
        dataBaseTable = json.load(tf)
        tf.close
    dataTables = putInformationTables()
    dataBaseTable[dataTables["tableNumber"]] = dataTables
    tf = open(dataFilePathTable, "w")
    json.dump(dataBaseTable, tf)
    tf.close()

def importJsonBar():
    dataFilePathBar = "dataBar.json"
    import json, os
    dataBaseBar = dict()
    if os.path.exists (dataFilePathBar):
        tf = open(dataFilePathBar, "r")
        dataBaseBar = json.load(tf)
        tf.close
    dataBar = putInformationBar()
    dataBaseBar[dataBar["barNumber"]] = dataBar
    tf = open(dataFilePathBar, "w")
    json.dump(dataFilePathBar, tf)
    tf.close()

def renderMenu1():
     renderMenu()
     menu = getNumberFronUser("Select menu mumber: ")
     return menu
    
def deliveryMenu():
    option1 = 2
    while option1 == 2:
        portada = "Delivery menu"
        print(portada.center(30,"-"))
        print("Do you have to register?")
        option1 = optionYesNo()
        if option1 == 2:
            importJson()
            renderMenu1()
        elif option1 == 1:
            number = input("Put your number: ")
            dataBase = importJsonRead()
            print(dataBase[dataName[number[name]]])
            #print(dataName[number[address]])
        else:
            print("The option does not exist, try again.")
def tableOrders():
    option1 = 2 
    while option1 == 2:
        portada = "Table orders"
        print(portada.center(30,"-"))
        putInformationTables()
        importJsonTable()
        renderMenu1()
        option1 = 1

def barOrders():
    option1 = 2
    while option1 == 2:
        portada = "Bar"
        print(portada.center(30, "-"))
        putInformationBar()
        importJsonBar()

def seeOrders():
    portada = "See orders"
    print(portada.center(30, "-"))
    option = int(input("What do you want to see?\n 1.Delivery orders\n 2.Orders tables\n 3.Bar orders"))
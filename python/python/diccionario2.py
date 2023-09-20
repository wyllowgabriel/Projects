myDictionary = {"Alemani":"Berlin", "Francia":"Paris", "Reino Unido":"London", "España": "Madrid"}
print(myDictionary["Francia"]) 

"Para poner mas claves"

myDictionary = {"Alemani":"Berlin", "Francia":"Paris", "Reino Unido":"London", "España": "Madrid"}
myDictionary["Italia"] = "Roma"
print(myDictionary) 

"Para madificar una clave"

myDictionary = {"Alemani":"Berlin", "Francia":"Paris", "Reino Unido":"London", "España": "Madrid"}
myDictionary["Italia"] = "Lisboa"
print(myDictionary)
myDictionary["Italia"] = "Roma"
print(myDictionary)

"Diccionario con otros tipos de datos"

myDictionary = {"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(myDictionary)

"juntar una tupla con un diccionario"

mytupla = ["España", "Francia", "Reino Unido", "Alemania"]
myDictionary = {mytupla[0]:"Madrid", mytupla[1]:"Paris", mytupla[2]:"Londres", mytupla[3]:"Berlin"}
print(myDictionary)
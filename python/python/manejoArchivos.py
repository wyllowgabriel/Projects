from io import open

#archivo en modo escritura

archivoTexto = open("archivo.txt","w")

frase = "Estupendo día para estudiar python \n el miercules"

archivoTexto.write(frase)

archivoTexto.close()

#archivo en modo lectura
#Para poner en formato de lista seria
#(texto = archivoTexto.readlines())

archivoTexto = open("archivo.txt","r")

texto = archivoTexto.read()

archivoTexto.close()

print(texto)

#Archivo para agregar(anexar) información

from io import open
archivoTexto = open("archivo.txt", "a")

archivoTexto.write("\n siempre es una buena ocasión para estudiar python ")

archivoTexto.close()
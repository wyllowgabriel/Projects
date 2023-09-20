#import pickle

#listaNombres = ["Pedro", "Ana", "Maria", "Isabel"]

#ficheroBinario = open("listaNombres","wb")

#pickle.dump(listaNombres, ficheroBinario)

#ficheroBinario.close()

#del (ficheroBinario)


# Para leer la información

import pickle

fichero = open("listaNombres","rb")

lista = pickle.load(fichero)

print(lista)


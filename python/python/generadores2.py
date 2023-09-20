"Generador de numeros pares sin usar la función generador"
from ast import Num


def generator(limite):

    num=1
    miLista=[]
    while num<limite:
        miLista.append(num*2)

        num+=1
    return miLista

print(generator(10))

"Utilizando un generador"
def generarPares(Limite):
    num= 1
    while num<Limite:
        yield num * 2
        num+=1
devuelvePares = generarPares(10)

for i in devuelvePares:
    print(i)

"Caso quieta que me devuelva valor a valor"

def generarPares(Limite):
    num= 1
    while num<Limite:
        yield num * 2
        num+=1
devuelvePares = generarPares(10)

print(next(devuelvePares))
"Aqui prodria ir mas código"
print(next(devuelvePares)) 
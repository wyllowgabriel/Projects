def devuelveCiudades (*ciudades):
    for elemento in ciudades:
       #for subElemento in elemento:
            yield from elemento

ciudadeDevuelve = devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudadeDevuelve))
print(next(ciudadeDevuelve))
rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]

def optimizar_rutas(lista_rutas, limites):
    rutas_validas = []
    for ruta, limite in zip(lista_rutas, limites):
        if ruta[2] <= limite:
            rutas_validas.append(ruta)
    return rutas_validas

print(optimizar_rutas(rutas, distancias_max))
paquetes = [ ("Paris", 200, 5), ("Roma", 150, 4), ("Londres", 180, 3) ]

def calcular_precios(lista_paquetes):
    diccionario_paquetes = {destino: precio * duracion for destino, precio, duracion in lista_paquetes}
    return diccionario_paquetes

print(calcular_precios(paquetes))
inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

def actuaizacion_inventario(inventario, ventas):
    inv_actualizado = []
    for i in range(len(inventario)):
        nuevo_valor = inventario[i] - ventas[i]
        inv_actualizado.append(nuevo_valor)
    return inv_actualizado

print(actuaizacion_inventario(inventario, ventas))
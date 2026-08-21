precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

def simulacion(precios, operaciones):
    balance = 0
    for tipo, dia in operaciones:
        if tipo == "compra":
            balance -= precios[dia]
        elif tipo == "venta":
            balance += precios[dia]
    return balance

print(simulacion(precios_diarios, operaciones))
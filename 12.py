productos = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]

def producto_mas_caro(productos):
    mas_caro = productos[0][1]
    for precio in productos:
        if precio[1] > mas_caro:
            mas_caro = precio[1]
    return mas_caro

print(producto_mas_caro(productos))
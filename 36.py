inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}

def actualizar_inventario(dicc_inv, tienda, **kwargs):
    if tienda in dicc_inv:
        for producto, cantidad in kwargs.items():
            if producto in dicc_inv[tienda]:
                dicc_inv[tienda][producto] += cantidad
            else:
                dicc_inv[tienda][producto] = cantidad
    return dicc_inv

print(actualizar_inventario(inventario, tienda="Tienda A", producto_1=10, producto_2=-5))
ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

def analisis_ventas(ventas):
    total = sum(ventas)
    promedio = total / len(ventas)
    return total, promedio

print(analisis_ventas(ventas_diarias))
ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

def analisis_ventas(ventas):
    total = sum(ventas)
    promedio = total / len(ventas)
    mayor_mes = ventas.index(max(ventas)) +1
    return total, promedio, mayor_mes

print(analisis_ventas(ventas_mensuales))
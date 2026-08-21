def analizar_finanzas(**kwargs):
    return sum(kwargs.values())

balance = analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)
print(balance)

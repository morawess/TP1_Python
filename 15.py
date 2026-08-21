def calcular_promedio(*args):
    promedio= 0
    promedio = sum(args) / len(args)
    return promedio

print(calcular_promedio(10, 9, 7, 7))
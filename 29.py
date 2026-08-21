notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

def promedio_estudiante(listado):
    promedio = {nombre: sum(notas) / len(notas) for nombre, notas in listado}
    return promedio

print(promedio_estudiante(notas_estudiantes))
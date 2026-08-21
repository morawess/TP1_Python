estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}
def promedio_estudiante(registro, legajo):
    promedio = 0
    if legajo in registro:
        calificaciones = registro[legajo]["calificaciones"].values()
        proemdio = sum(calificaciones) / len(calificaciones)
        return proemdio

print(promedio_estudiante(estudiantes, 101))
estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

def ranking(registro):
    promedios = {}
    for estudiantes_id, materias in registro.items():
        total_notas = []
        for notas_materia in materias.values():
            total_notas.extend(notas_materia)

        promedio_gral = sum(total_notas) / len(total_notas)
        promedios[estudiantes_id] = promedio_gral

    return sorted(promedios.items(), key=lambda x: x[1], reverse=True)

print(ranking(estudiantes))
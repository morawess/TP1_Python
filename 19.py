resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

def calculo_goles(resultados):
    anotados = 0
    recibidos = 0
    for goles in resultados.values():
        anotados += goles[0]
        recibidos += goles[1]
    return anotados, recibidos

anotados, recibidos = calculo_goles(resultados)

print(f"goles anotados: {anotados}. goles recibidos: {recibidos}")
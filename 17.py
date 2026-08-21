empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

def filtrar_salario(registro_empleados, salario_minimo):
    empleados_filtrados = {}
    for id, info in registro_empleados.items():
        if info[2] > salario_minimo:
            empleados_filtrados[id] = info
    return empleados_filtrados

print(filtrar_salario(empleados, 2800))
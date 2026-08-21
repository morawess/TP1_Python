reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}


def hacer_reserva(diccionario_reservas, fecha, huesped, habitacion, precio):
    if fecha not in diccionario_reservas:
        diccionario_reservas[fecha] = []

    # Comprobar disponibilidad
    for reserva in diccionario_reservas[fecha]:
        if reserva[1] == habitacion:
            return f"La habitacion {habitacion} ya está reservada."

    diccionario_reservas[fecha].append((huesped, habitacion, precio))
    return "Reserva realizada con exito."


print(hacer_reserva(reservas, "2024-08-15", "Pedro", 103, 100))
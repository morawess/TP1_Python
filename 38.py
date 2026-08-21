suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

def actualizar_suscripcion(dicc_subs, usuario, suscripcion, **kwargs):
    if usuario not in dicc_subs:
        dicc_subs[usuario] = []

    if suscripcion not in dicc_subs[usuario]:
        dicc_subs[usuario].append(suscripcion)
    return dicc_subs


print(actualizar_suscripcion(suscripciones, usuario="Luis", suscripcion="mensual", auto_renovacion=True))
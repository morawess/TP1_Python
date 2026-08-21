def organizar_eventos(*args):
    for indice, evento in enumerate(args, 1):
        print(f"{indice}. {evento}")

organizar_eventos("Concierto", "Exposición de arte", "Conferencia")
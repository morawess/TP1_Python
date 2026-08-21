def publicar(usuario, texto, **kwargs):
    publicacion = {"usuario": usuario, "texto": texto}
    publicacion.update(kwargs)
    return publicacion

print(publicar("Juan", "Mi primer post!", etiquetas=["#hola", "#primerPost"], visibilidad="publica", likes=100))
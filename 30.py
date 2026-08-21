usuarios = ["Ana", "Luis", "María"]
def configurar_perfiles(lista_usuarios, **kwargs):
    array_config = list(kwargs.items())
    return {usuario: array_config for usuario in lista_usuarios}

print(configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False))

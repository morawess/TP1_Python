tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

def analizar_tendencias(lista_tendencias, limite_menciones):
    return [hashtag for hashtag, frec in lista_tendencias if frec > limite_menciones]

print(analizar_tendencias(tendencias, 100))
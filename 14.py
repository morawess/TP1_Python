temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def analisis_temperaturas(temperaturas):
    media = sum(temperaturas)/len(temperaturas)
    maxima = max(temperaturas)
    minima = min(temperaturas)
    return media, maxima, minima

print(analisis_temperaturas(temperaturas))
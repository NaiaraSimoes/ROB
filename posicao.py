import math

def posicao(alfa, cx, cy, d):
    x = cx + d * math.cos(alfa)
    y = cy + d * math.sin(alfa) * math.cos(alfa)
    z = 0

    # Formatando os valores com 2 casas decimais
    return {
        'x': f"{x:.2f}",
        'y': f"{y:.2f}",
        'z': f"{z:.2f}"
    }
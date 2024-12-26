import math

def velocidade(alfa, alfa_dot, d):
    vx = -d * math.sin(alfa) * alfa_dot
    vy = d * (math.cos(alfa)**2 - math.sin(alfa)**2) * alfa_dot
    vz = 0  # Constante

    return {
        'vx': f"{vx:.2f}",
        'vy': f"{vy:.2f}",
        'vz': f"{vz:.2f}"
    }

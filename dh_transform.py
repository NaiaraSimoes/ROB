import numpy as np
from sympy import cos, sin

def dh_transform(theta, d, a, alpha):
    """
    Retorna a matriz de transformação DH para os parâmetros fornecidos.
    """
    return np.array([
        [cos(theta), -sin(theta) * cos(alpha), sin(theta) * sin(alpha), a * cos(theta)],
        [sin(theta), cos(theta) * cos(alpha), -cos(theta) * sin(alpha), a * sin(theta)],
        [0, sin(alpha), cos(alpha), d],
        [0, 0, 0, 1]
    ])

import numpy as np
from sympy import sin, cos

def compute_jacobian(t1, d2, t3, Lg):

    return np.array([
        [-Lg * sin(t1 + t3) - d2 * sin(t1), cos(t1), -Lg * sin(t1 + t3)],
        [Lg * cos(t1 + t3) + d2 * cos(t1), sin(t1),  Lg * cos(t1 + t3)],
        [-1, 0, -1]
    ])

import numpy as np
from sympy import pi, simplify
from dh_transform import dh_transform

def forward_kinematics(t0, t1, d2, t3, Lg):
    """
    Calcula a matriz de cinemática direta (FK).
    """
    DH_table = [
        [t0,  0,  0,  pi/2],
        [t1,  0,  0,  pi/2],
        [0,  d2,  0, -pi/2],
        [t3,  0,  0,  pi/2],
        [0,  Lg,  0,  0]
    ]
    T = np.eye(4)
    for params in DH_table:
        T = T @ dh_transform(*params)
    return simplify(T)

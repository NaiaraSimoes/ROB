from sympy import cos, sin, atan2

def inverse_kinematics(r, Lg, alpha):
    """
    Calcula os ângulos articulares usando cinemática inversa.
    """
    tx = 40 + (r - Lg) * cos(alpha)
    ty = 0
    tz = 20 - (r - Lg) * sin(alpha)
    
    t0 = atan2(ty, tx)
    t1 = atan2(tz, cos(t0) * tx)
    d2 = cos(t1) * tx + sin(t1) * tz
    t3 = -alpha - t1
    
    return [t0, t1, d2, t3]

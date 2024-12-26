from forward_kinematics import forward_kinematics
from inverse_kinematics import inverse_kinematics
from jacobian import compute_jacobian
from sympy import pi

# Parâmetros iniciais
t0, t1, d2, t3 = 0, 0, 10, pi/4
Lg = 10
r = 10
alpha = pi / 4

# Cinemática Direta
T_ef = forward_kinematics(t0, t1, d2, t3, Lg)
print("Cinemática Direta (FK):")
print(T_ef)

# Cinemática Inversa
params = inverse_kinematics(r, Lg, alpha)
print("\nCinemática Inversa (IK):")
print("Parâmetros articulares:", params)

# Jacobiano
jacobian = compute_jacobian(params[1], params[2], params[3], Lg)
print("\nJacobiano:")
print(jacobian)

# Arquivo principal (main.py)

import time
import sys
sys.path.append('/workspaces/ROB/xarm')
from xarm.wrapper import XArmAPI
from simple_pid import PID
from posicao import posicao
from velocidade import velocidade
from pid_control import calcular_velocidades_pid
from forward_kinematics import forward_kinematics
from inverse_kinematics import inverse_kinematics
from jacobian import compute_jacobian
from sympy import pi

# Configuração inicial do braço
arm = XArmAPI('192.168.x.x')  # Substituir pelo IP correto
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)
time.sleep(1)

arm.move_gohome(wait=True)

# Configurar o modo de controlo de velocidade das juntas
arm.set_mode(4)
arm.set_state(0)
time.sleep(1)

# Parâmetros iniciais baseados na tabela DH fornecida
t0, t1, d2, t3 = 0, -90, -90  # Theta offset e deslocamento inicial
a1, a2, a3, a4, a5, a6 = 0, 200, 87, 0, 0, 0  # Valores de "a"
d1, d2, d3, d4, d5, d6 = 243.3, 0, 0, 227.6, 0, 61.5  # Valores de "d"
alpha1, alpha2, alpha3, alpha4, alpha5, alpha6 = -90, 180, 90, 90, -90, 0  # Valores de "alpha"


# Configuração da trajetória atribuída (trajetória 1)
cx, cy, d = 0.1, 0.1, 0.05  # Exemplos de parâmetros da tarefa
alpha_dot = 3.1415 / 2  # Velocidade angular (rad/s)

# Loop de controlo
start_time = time.time()
while time.time() - start_time < 20:  # Controla durante 20 segundos
    alpha = alpha_dot * (time.time() - start_time)
    pos = posicao(alpha, cx, cy, d)
    vel = velocidade(alpha, alpha_dot, d)

    # Mapear velocidades para o espaço articular (usando PID)
    joint_velocities = [
        float(vel['vx']),
        float(vel['vy']),
        float(vel['vz']),
        0, 0, 0
    ]

    adjusted_velocities = calcular_velocidades_pid(joint_velocities)

    # Enviar velocidades ajustadas para o robô
    arm.vc_set_joint_velocity(adjusted_velocities)
    time.sleep(0.05)  # Controla em ciclos de 50ms

    

# Parar o robô
arm.vc_set_joint_velocity([0, 0, 0, 0, 0, 0])
arm.disconnect()

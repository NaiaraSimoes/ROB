from simple_pid import PID

# Configurar os controladores PID para cada junta
pid_joint_1 = PID(1.0, 0.1, 0.05, setpoint=0)
pid_joint_2 = PID(1.0, 0.1, 0.05, setpoint=0)
pid_joint_3 = PID(1.0, 0.1, 0.05, setpoint=0)
pid_joint_4 = PID(1.0, 0.1, 0.05, setpoint=0)
pid_joint_5 = PID(1.0, 0.1, 0.05, setpoint=0)
pid_joint_6 = PID(1.0, 0.1, 0.05, setpoint=0)

def calcular_velocidades_pid(joint_velocities):
    return [
        pid_joint_1(joint_velocities[0]),
        pid_joint_2(joint_velocities[1]),
        pid_joint_3(joint_velocities[2]),
        pid_joint_4(joint_velocities[3]),
        pid_joint_5(joint_velocities[4]),
        pid_joint_6(joint_velocities[5])
    ]

import os
import sys
import time
import math
from math import pi
from xarm.wrapper import XArmAPI

# Initial configuration of the arm
cx = 0.1
cy = 0.1
d = 0.05
alfa_dot = pi / 2
alfa = 0.1
cte = 0.1
arm = XArmAPI('192.168.x.x')  # Add IP Correto
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

arm.move_gohome(wait=True)
# set joint velocity control mode
arm.set_mode(4)
arm.set_state(0)
time.sleep(1)
for t in range(0, 100):
    #Position
    px = cx + d * math.cos(alfa)
    py = cy + d * math.sin(alfa) * math.cos(alfa)
    pz = cte
    #Velocity
    vx = -d * math.sin(alfa) * alfa_dot
    vy = d * (math.cos(alfa)**2 - math.sin(alfa)**2) * alfa_dot
    vz = 0 
    #Extra data
    rollx = pi
    pitchy = 0
    yawz = 0
    #Set joint velocity
    arm.vc_set_joint_velocity([vx, vy, vz, rollx, pitchy, 0])
    #Set Tool position
    arm.set_tool_position(x=px, y=py, z=px, roll=0, pitch=pitchy, yaw=yawz, speed=pi/2, wait=True)
    alfa = alfa + alfa_dot * 0.01
    time.sleep(0.01)


arm.move_gohome(wait=True)
arm.disconnect()
import math
import numpy as np

from posicao import posicao
from velocidade import velocidade

def main():
    # Parâmetros do trajeto
    cx = 0.5    # Posição inicial no eixo x
    cy = 0.5    # Posição inicial no eixo y
    d = 0.2     # Raio da trajetória
    alfa_dot = np.pi / 2  # Velocidade angular (rad/s)

    # Loop para calcular posições e velocidades
    for alfa in np.linspace(0, 2 * np.pi, 100):  # 100 passos de 0 a 2π
        pos_atual = posicao(alfa, cx, cy, d)
        vel_atual = velocidade(alfa, alfa_dot, d)
        print(f"Posição: {pos_atual}, Velocidade: {vel_atual}")

if __name__ == "__main__":
    main()        
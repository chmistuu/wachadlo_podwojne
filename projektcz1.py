import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m1 = 1.0
m2 = 1.0
L1 = 1.0
L2 = 1.0
theta1 = 90
theta2 = 90
g=9.81
dt = 0.001
#okres czasu to ile razy dt, dt jest w sekundach
def liczenie_a(theta1, theta2, okres_czasu=10):
    theta1 = np.radians(theta1)  
    theta2 = np.radians(theta2)
    omega1, omega2 = 0.0, 0.0
    for i in range(okres_czasu):
        delta = theta2 - theta1
        denom1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta) ** 2
        denom2 = (L2 / L1) * denom1

        a1 = (m2 * L1 * omega1 ** 2 * np.sin(delta) * np.cos(delta) +
              m2 * g * np.sin(theta2) * np.cos(delta) +
              m2 * L2 * omega2 ** 2 * np.sin(delta) -
              (m1 + m2) * g * np.sin(theta1)) / denom1

        a2 = (-m2 * L2 * omega2 ** 2 * np.sin(delta) * np.cos(delta) +
              (m1 + m2) * g * np.sin(theta1) * np.cos(delta) -
              (m1 + m2) * L1 * omega1 ** 2 * np.sin(delta) -
              (m1 + m2) * g * np.sin(theta2)) / denom2
        omega1 += a1 * dt
        omega2 += a2 * dt
        theta1 += omega1 * dt
        theta2 += omega2 * dt

    return omega1, omega2, a1, a2

omega1, omega2, a1, a2 = liczenie_a(theta1, theta2)

print(f"omega1: {omega1}, a1: {a1}")
print(f"omega2: {omega2}, a2: {a2}")
#po czasie okres_czasu*10 wychodzi wynik


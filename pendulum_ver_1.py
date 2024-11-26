from multiprocessing.managers import Value

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def masakulek1():
    while True:
        try:
            wartosc = float(input("Podaj masę pierwszego wahadła (m1)[kg]: "))
            if wartosc > 0:
                return wartosc
            else:
                print("Podana wartość musi być liczba większą niż 0.")
        except ValueError:
            print("Proszę podać liczbę. Podana wartość musi być większa niż 0")
def masakulek2():
    while True:
        try:
            wartosc = float(input("Podaj masę pierwszego wahadła (m2)[kg]: "))
            if wartosc > 0:
                return wartosc
            else:
                print("Podana wartość musi być liczba większą niż 0.")
        except ValueError:
            print("Proszę podać liczbę. Podana wartość musi być większa niż 0")
def dlugoscpreta1():
    while True:
        try:
            wartosc = float(input("Podaj długość pierwszego wahadła (L1)[m]: "))
            if wartosc > 0:
                return wartosc
            else:
                print("Podana wartość musi być liczba większą niż 0.")
        except ValueError:
            print("Proszę podać liczbę. Podana wartość musi być większa niż 0")
def dlugoscpreta2():
    while True:
        try:
            wartosc = float(input("Podaj długość drugiego wahadła (L2)[m]: "))
            if wartosc > 0:
                return wartosc
            else:
                print("Podana wartość musi być liczba większą niż 0.")
        except ValueError:
            print("Proszę podać liczbę. Podana wartość musi być większa niż 0")
def katpocz1():
    while True:
        try:
            wartosc = float(input("Podaj początkowe wychylenie pierwszego wahadła (w stopniach): "))
            if wartosc >= 0:
                return wartosc
            else:
                print("Podana wartość musi być liczba większą niż 0.")
        except ValueError:
            print("Proszę podać liczbę. Podana wartość musi być większa lub równą niż 0")
def katpocz2():
    while True:
        try:
            wartosc = float(input("Podaj początkowe wychylenie drugiego wahadła (w stopniach): "))
            if wartosc >= 0:
                return wartosc
            else:
                print("Podana wartość musi być liczba większą niż 0.")
        except ValueError:
            print("Proszę podać liczbę. Podana wartość musi być większa lub równą niż 0")
def wybierzg():
    while True:
        try:
            wartosc = float(input("Podaj wartość przyśpieszenia grawitacyjnego[m/s^2]: "))
            if wartosc >= 0:
                return wartosc
            else:
                print("Podana wartość musi być liczba większą niż 0.")
        except ValueError:
            print("Proszę podać liczbę. Podana wartość musi być większa lub równą niż 0")
# Parametry od użytkownika
m1 = masakulek1()
m2 = masakulek2()
L1 = dlugoscpreta1()
L2 = dlugoscpreta2()
theta1 = katpocz1()
theta2 = katpocz2()
g = wybierzg()
# Funkcja symulująca ruch wahadła podwójnego
def simulate_double_pendulum(L1, L2, theta1, theta2, g=9.81, dt=0.01, steps=100000):
    # Inicjalizacja zmiennych
      # masy wahadeł
    theta1 = np.radians(theta1)  # konwersja kąta na radiany
    theta2 = np.radians(theta2)
    omega1, omega2 = 0.0, 0.0  # początkowe prędkości kątowe

    theta1_vals, theta2_vals = [theta1], [theta2]
    x1_vals, y1_vals, x2_vals, y2_vals = [], [], [], []

    for i in range(steps):
        # Równania ruchu
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

        # Aktualizacja zmiennych
        omega1 += a1 * dt
        omega2 += a2 * dt
        theta1 += omega1 * dt
        theta2 += omega2 * dt

        theta1_vals.append(theta1)
        theta2_vals.append(theta2)

        x1 = L1 * np.sin(theta1)
        y1 = -L1 * np.cos(theta1)
        x2 = x1 + L2 * np.sin(theta2)
        y2 = y1 - L2 * np.cos(theta2)

        x1_vals.append(x1)
        y1_vals.append(y1)
        x2_vals.append(x2)
        y2_vals.append(y2)

    return x1_vals, y1_vals, x2_vals, y2_vals,


# Symulacja
x1, y1, x2, y2 = simulate_double_pendulum(L1, L2, theta1, theta2, g)

# Animacja
fig, ax = plt.subplots()
ax.set_xlim(-L1 - L2 - 0.5, L1 + L2 + 0.5)
ax.set_ylim(-L1 - L2 - 0.5, L1 + L2 + 0.5)
line, = ax.plot([], [], 'o-', lw=2)
trail, = ax.plot([], [], 'r-', lw=0.5, alpha=0.5)

def init():
    line.set_data([], [])
    trail.set_data([], [])
    return line, trail

def update(frame):
    x = [0, x1[frame], x2[frame]]
    y = [0, y1[frame], y2[frame]]
    line.set_data(x, y)
    trail.set_data(x2[:frame], y2[:frame])
    return line, trail

ani = FuncAnimation(fig, update, frames=len(x1), init_func=init, blit=True, interval=1)

plt.show()
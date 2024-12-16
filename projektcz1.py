from multiprocessing.managers import Value
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class sprawdzanie:
    def masa1():
        while True:
            try:
                val = float(input("Podaj masę m1: "))
                if val>0:
                    return val
                else:
                    print("wartość musi być dodatnia")
            except ValueError:
                print("Wartość musi być liczbą. Podaj liczbę wiekszą od 0")

    def masa2():
        while True:
            try:
                val = float(input("Podaj masę m2: "))
                if val>0:
                    return val
                else:
                    print("wartość musi być dodatnia")
            except ValueError:
                print("Wartość musi być liczbą. Podaj liczbę wiekszą od 0")

    def dlugosc1():
        while True:
            try:
                val = float(input("Podaj długość L1: "))
                if val>0:
                    return val
                else:
                    print("wartość musi być dodatnia")
            except ValueError:
                print("Wartość musi być liczbą. Podaj liczbę wiekszą od 0")

    def dlugosc2():
        while True:
            try:
                val = float(input("Podaj długość L2: "))
                if val>0:
                    return val
                else:
                    print("wartość musi być dodatnia")
            except ValueError:
                print("Wartość musi być liczbą. Podaj liczbę wiekszą od 0")

    def kat1():
        while True:
            try:
                val = float(input("Podaj wychylenie pierwszego wahadła: "))
                return val
            except ValueError:
                print("Wartość musi być liczbą. Podaj liczbę wiekszą od 0")

    def kat2():
        while True:
            try:
                val = float(input("Podaj wychylenie drugiego wahadła: "))
                return val
            except ValueError:
                print("Wartość musi być liczbą. Podaj liczbę wiekszą od 0")

    def gravity():
        while True:
            try:
                val = float(input("Podaj siłę grawitacji: "))
                if val>0:
                    return val
                else:
                    print("wartość musi być dodatnia")
            except ValueError:
                print("Wartość musi być liczbą. Podaj liczbę wiekszą od 0")

m1 = sprawdzanie.masa1()
m2 = sprawdzanie.masa2()
L1 = sprawdzanie.dlugosc1()
L2 = sprawdzanie.dlugosc2()
theta1 = sprawdzanie.kat1()
theta2 = sprawdzanie.kat2()
g=sprawdzanie.gravity()
#okres czasu to ile razy dt, dt jest w sekundach
def liczenie_a(m1, m2, g, L1, L2, theta1, theta2, okres_czasu=100000, dt = 0.01):
    theta1 = np.radians(theta1)  
    theta2 = np.radians(theta2)
    omega1, omega2 = 0.0, 0.0
    theta1_wart, theta2_wart = [theta1], [theta2]
    x1_wart, x2_wart, y1_wart, y2_wart = [], [], [], []
    for i in range(okres_czasu):
        delta = theta2 - theta1
        mian1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta) ** 2
        mian2 = (L2 / L1) * mian1

        a1 = (m2 * L1 * omega1 ** 2 * np.sin(delta) * np.cos(delta) +
              m2 * g * np.sin(theta2) * np.cos(delta) +
              m2 * L2 * omega2 ** 2 * np.sin(delta) -
              (m1 + m2) * g * np.sin(theta1)) / mian1

        a2 = (-m2 * L2 * omega2 ** 2 * np.sin(delta) * np.cos(delta) +
              (m1 + m2) * g * np.sin(theta1) * np.cos(delta) -
              (m1 + m2) * L1 * omega1 ** 2 * np.sin(delta) -
              (m1 + m2) * g * np.sin(theta2)) / mian2
        omega1 += a1 * dt
        omega2 += a2 * dt
        theta1 += omega1 * dt
        theta2 += omega2 * dt
        x1 = L1*np.sin(theta1)
        y1 = -L1*np.cos(theta1)
        x2 = x1 + L2*np.sin(theta2)
        y2 = y1-L2*np.cos(theta2)
        
        x1_wart.append(x1)
        x2_wart.append(x2)
        y1_wart.append(y1)
        y2_wart.append(y2)
        
        theta1_wart.append(theta1)
        theta2_wart.append(theta2)

    return x1_wart, x2_wart, y1_wart, y2_wart

x1, x2, y1, y2 = liczenie_a(m1, m2, g, L1, L2, theta1, theta2)
fig, ax = plt.subplots()
ax.set_xlim(-L1-L2-1,L1+L2+1)
ax.set_ylim(-L1-L2-1,L1+L2+1)
linia, = ax.plot([], [], 'o-', lw=2)
trajektoria, = ax.plot([], [], 'r-', lw=0.5, alpha=0.5)

def init():
    linia.set_data([], [])
    trajektoria.set_data([], [])
    return linia, trajektoria

def update(frame):
    x = [0, x1[frame], x2[frame]]
    y = [0, y1[frame], y2[frame]]
    line.set_data(x, y)
    trajektoria.set_data(x2[:frame], y2[:frame])
    return linia, trajektoria

ani = FuncAnimation(fig, update, frames=len(x1), init_func=init, blit=True, interval=0.001)

plt.show()

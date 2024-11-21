import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.stats import linregress

#zad 1
#a>
def met_apd(n):
    kwadraty = []
    for liczby in range(n):
        kwadraty.append(liczby ** 2)
    return kwadraty

def list_comp(n):
    return[kwadrat**2 for kwadrat in range(n)]

def num_py(n):
    return np.arange(n)**2

n=10000

czas_start = time.time()
met_apd(n)
czas_stop = time.time()
print(f"Czas wykonania append: {czas_stop - czas_start:.6f} sekundy")

czas_start = time.time()
list_comp(n)
czas_stop = time.time()
print(f"Czas wykonania list comprehension: {czas_stop - czas_start:.6f} sekundy")

czas_start = time.time()
num_py(n)
czas_stop = time.time()
print(f"Czas wykonania numpy: {czas_stop - czas_start:.6f} sekundy")

#zad 2 
print(np.ones((4,4),bool))
#zad 3 
a = np.array(range(10))
b = np.ones(10)
a_macierz = a.reshape(2,5)
b_macierz = b.reshape(2,5)
polaczone = np.vstack((a_macierz, b_macierz))
print("\n\n macierz a \n", a_macierz)
print(" macierz b \n", b_macierz)
print("połączone a i b\n", polaczone)

#zad 4
wektor = np.random.rand(10)
filtrliczb = wektor[(wektor > 0.5) & (wektor < 0.9)]
print(filtrliczb)

#zad 5
plik = np.loadtxt('dih_sample.dat')
min = np.min(plik)
max = np.max(plik)
normplik = (plik - min)/(max - min)
np.savetxt('normdah_sample.dat', normplik)
#zad 6

g = 9.81  
v0 = 50   

def y_trajectory(x, alpha):
    alpha_rad = np.radians(alpha)
    return x * np.tan(alpha_rad) - (g * x**2) / (2 * (v0 * np.cos(alpha_rad))**2)

def calculate_range(alpha):
    alpha_rad = np.radians(alpha)
    return (v0**2 * np.sin(2 * alpha_rad)) / g

initial_alpha = 45

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)

x_max = calculate_range(initial_alpha)
x = np.linspace(0, x_max, 500)
y = y_trajectory(x, initial_alpha)

line, = ax.plot(x, y, label=f'Trajektoria gdy α = {initial_alpha}°')
ax.set_title('Ruch pocisku - rzut ukośny')
ax.set_xlabel('Zasięg na osi x')
ax.set_ylabel('Zasięg na osi y')
ax.grid(True)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.legend()

ax_alpha = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgrey')
alpha_slider = Slider(ax_alpha, 'Kąt α (°)', 10, 80, valinit=initial_alpha)

def update(val):
    alpha = alpha_slider.val
    x_max = calculate_range(alpha)
    x = np.linspace(0, x_max, 500)
    y = y_trajectory(x, alpha)
    line.set_xdata(x)
    line.set_ydata(y)
    line.set_label(f'Trajektoria gdy α = {alpha:.1f}°')
    ax.relim()
    ax.autoscale_view()
    ax.legend()
    fig.canvas.draw_idle()

alpha_slider.on_changed(update)

plt.show()

#zad 7
U = np.array([1, 5, 7, 9, 12])
I = np.array([0.25, 1.05, 1.37, 1.78, 2.45])

slope, intercept, r_value, p_value, std_err = linregress(U, I)

I_fit = slope * U + intercept

plt.figure(figsize=(8, 6))
plt.scatter(U, I, color='blue', label='Dane pomiarowe')
plt.plot(U, I_fit, color='red', label=f'Dopasowanie: I = {slope:.2f}U + {intercept:.2f}')
plt.title('Regresja liniowa')
plt.xlabel('Napięcie (U) [V]')
plt.ylabel('Natężenie prądu (I) [A]')
plt.legend()
plt.grid(True)
plt.show()


print(f'Wartość oporu (R): {1/slope:.2f} Ohm')
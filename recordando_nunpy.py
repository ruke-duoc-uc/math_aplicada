import matplotlib.pyplot as plt
import numpy as np

# 1. Definir el intervalo continuo para que las curvas se vean suaves
x = np.linspace(-2, 4, 400)
f = x**3
g = 2 * x + 3

# 2. Crear el gráfico base
plt.plot(x, f, label="f(x) = x**3", color="blue")
plt.plot(x, g, label="g(x) = 2x + 3", color="red")

# --- DESTACAR EXACTAMENTE CADA 1 UNIDAD ---
# Definimos los puntos enteros exactos donde sí queremos el punto (incluyendo el 1)
x_enteros = np.arange(-2, 5)  # Genera [-2, -1, 0, 1, 2, 3, 4]
y_enteros = x_enteros**3

plt.scatter(
    x_enteros,
    y_enteros,
    color="purple",
    s=60,
    zorder=5,
    label="Puntos exactos (intervalos de 1)",
)
# ------------------------------------------

# 3. Elementos visuales
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráfico con puntos enteros exactos destacados")
plt.grid(True)
plt.legend()

plt.show()
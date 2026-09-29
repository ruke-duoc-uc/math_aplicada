import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10, 2)
# Esta funcion nos permite ver los cambios
y = -0.5*x**2+3*x+20
# La variable independiente es el tiempo, ya que la temperatura es determinada por el mismo
plt.plot(x, y, color="purple", linewidth=2,label="Linea",linestyle="-.")
plt.plot(x,y,color="red",marker="o",label="Puntos",linestyle="")

plt.xlabel("Tiempo (Horas)")
plt.ylabel("Temperatura (C°)")
plt.title("Temperatura de servidor")
plt.grid(True)
plt.legend()

# 6. Mostrar el gráfico
plt.show()
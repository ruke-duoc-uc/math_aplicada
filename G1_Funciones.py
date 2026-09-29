import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1000, 10)
# Esta funcion nos permite ver los cambios
# 
y = (x / 200) * 100

plt.plot(x, y, color="purple", linewidth=2)

plt.xlim(200, 260)
plt.ylim(100, 140)

plt.xlabel("Energía utilizada (kWh)")
plt.ylabel("Incremento respecto a 200 (%)")
plt.title("Porcentaje de aumento tomando 200 como base (100%)")
plt.grid(True)
# 6. Mostrar el gráfico
plt.show()
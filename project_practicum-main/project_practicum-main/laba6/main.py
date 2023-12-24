import numpy as np
import matplotlib.pyplot as plt


def parametric_function(t):
    x = np.log(t) * np.sin(t)
    y = np.cos(t)
    return x, y


def polar_function(phi):
    rho = 2 * np.cos(phi / 3)
    return rho


t_values = np.linspace(0.1, 10, 1000)
phi_values = np.linspace(0, 2 * np.pi, 1000)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Параметрическая фукнция")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.plot(*parametric_function(t_values), label='$x = ln(t) * sin(t), y = cos(t)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')

plt.savefig('parametric_plot.svg', format='svg')
plt.close()


plt.figure(figsize=(5, 5), constrained_layout=True)
plt.subplot(polar=True)
plt.title("График в полярных координатах")
plt.grid(True)
plt.plot(phi_values, polar_function(phi_values), label='$\\rho = 2cos(\\frac{\\phi}{3})$')
plt.thetagrids(range(0, 360, 30), labels=[f'{i}°' for i in range(0, 360, 30)])
plt.rgrids(range(0, 4))
plt.legend(loc='lower center')

plt.fill_between(phi_values, 0, polar_function(phi_values), where=(phi_values >= 0) & (phi_values <= np.pi / 8) & (phi_values <= polar_function(phi_values)), alpha=0.3, color='blue', label='$0 \\leq \\phi \\leq \\frac{\pi}{8}, \\, 0 \\leq \\phi \\leq \\rho$')

plt.savefig('polar_plot.svg', format='svg')
plt.close()

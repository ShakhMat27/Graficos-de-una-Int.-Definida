import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 500)

def f(x):
    return 0.12 * (x - 5)**2 + 2

def g(x):
    return -0.12 * (x - 5)**2 + 5

a = 1.5
b = 8.5

y_at_a = f(a)
y_at_b = f(b)

fig, ax = plt.subplots(figsize=(8, 5))

for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_xticks([])
ax.set_yticks([])

ax.arrow(0, 0, 10.5, 0, head_width=0.3, head_length=0.3, fc='#1f77b4', ec='#1f77b4', lw=2, zorder=10)
ax.arrow(0, 0, 0, 6.5, head_width=0.15, head_length=0.6, fc='#1f77b4', ec='#1f77b4', lw=2, zorder=10)

ax.text(10.5, -0.5, 'x', fontsize=16, color='#1f77b4', fontweight='bold')
ax.text(-0.5, 6.3, 'y', fontsize=16, color='#1f77b4', fontweight='bold')

ax.plot(x, f(x), color='#ef3b2c', linewidth=2.5)
ax.plot(x, g(x), color='#4daf4a', linewidth=2.5)

x_fill = np.linspace(a, b, 100)
ax.fill_between(x_fill, f(x_fill), g(x_fill), color='#f9cca5', alpha=1)

ax.vlines(x=a, ymin=0, ymax=y_at_a, colors='gray', linestyles='--', linewidth=1.5)
ax.text(a, -0.5, 'a', ha='center', fontsize=16, color='gray', fontweight='bold')

ax.vlines(x=b, ymin=0, ymax=y_at_b, colors='gray', linestyles='--', linewidth=1.5)
ax.text(b, -0.5, 'b', ha='center', fontsize=16, color='gray', fontweight='bold')

ax.text(9, f(9) + 1.5, 'y = f(x)', color='#cc2529', fontsize=16, fontweight='normal')

ax.text(9, g(9) - 1.5, 'y = g(x)', color='#4daf4a', fontsize=16, fontweight='normal')

ax.set_xlim(-1, 11)
ax.set_ylim(-1, 7)
ax.set_aspect('equal')

plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.lines as mlines

x = np.linspace(1, 2, 100)
theta = np.linspace(0, 2 * np.pi, 100)

X_grid, Theta_grid = np.meshgrid(x, theta)

R = 1 / X_grid

X = X_grid
Y = R * np.cos(Theta_grid)
Z = R * np.sin(Theta_grid)

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap=cm.GnBu_r, alpha=0.8, 
                       rstride=4, cstride=4, 
                       edgecolor='teal', linewidth=0.3,shade=True)

cbar = fig.colorbar(surf, ax=ax, shrink=0.6, aspect=10, pad=0.1)
cbar.set_label('Variación del Radio (Valor Z local)', rotation=270, labelpad=15)

proxy_surf = mlines.Line2D([], [], color='teal', marker='s', markersize=10, 
                           markerfacecolor=cm.GnBu_r(0.5), alpha=0.8, linestyle='None',
                           label='Superficie de Revolución $f(x)=1/x$')

ax.legend(handles=[proxy_surf], loc='upper left', fontsize=12)


ax.set_xlabel('Eje X (Longitud)')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

ax.set_xlim(0.5, 2.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

ax.view_init(elev=25, azim=-60)

plt.title('Análisis del Volumen de Revolución entre x=1 y x=2', fontsize=16)
plt.tight_layout()
plt.show()

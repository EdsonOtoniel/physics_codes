import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Parâmetros
t = np.linspace(0, 2 * np.pi,70) # Menos pontos (20), maior espaçamento
E = np.sin(t)  # Campo Elétrico (Y)
B = np.sin(t)  # Campo Magnético (Z)

# Localização das frentes de onda (pontos de máxima amplitude)
frente_pos = [np.pi / 2, 3 * np.pi / 2]  # π/2 e 3π/2

# Plotagem
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Onda elétrica (E) no plano XY
ax.plot(t, E, np.zeros_like(t), color='r', label='Campo Elétrico (E)')

# Onda magnética (B) no plano XZ
ax.plot(t, np.zeros_like(t), B, color='b', label='Campo Magnético (B)')

# Vetores do campo elétrico (plano XY)
ax.quiver(t, np.zeros_like(t), np.zeros_like(t), 
          np.zeros_like(t), E, np.zeros_like(t), 
          color='r', length=1.0, normalize=False)

# Vetores do campo magnético (plano XZ)
ax.quiver(t, np.zeros_like(t), np.zeros_like(t), 
          np.zeros_like(t), np.zeros_like(t), B, 
          color='b', length=1.0, normalize=False)

# Adicionar duas frentes de onda
for pos in frente_pos:
    frente = [
        [pos, -1, -1],  # canto inferior esquerdo
        [pos, 1, -1],   # canto superior esquerdo
        [pos, 1, 1],    # canto superior direito
        [pos, -1, 1],   # canto inferior direito
    ]
    ax.add_collection3d(Poly3DCollection([frente], alpha=0.3, color='cyan'))

# Vetor de propagação (preto, perpendicular ao plano)
modulo = 8
direcao = np.array([1, 0, 0])
vetor = modulo * direcao

ax.quiver(0, 0, 0, vetor[0], vetor[1], vetor[2], 
          color='k', linewidth=3, arrow_length_ratio=0.05)

# Configurações do gráfico
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

# Remover caixa e grades
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_axis_off()

# Fundo transparente
fig.patch.set_alpha(0.0)
ax.set_facecolor((1, 1, 1, 0))

plt.show()

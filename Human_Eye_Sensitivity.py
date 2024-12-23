import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Dados da sensibilidade relativa do olho humano
# Comprimento de onda em nanômetros e sensibilidade relativa (normalizada)
wavelengths = np.linspace(380, 780, 400)

# Função aproximada para a sensibilidade relativa do olho humano (curva suavizada com uma Gaussiana)
def human_eye_sensitivity(wl):
    mean = 555  # Pico de sensibilidade em nm
    std_dev = 50  # Desvio padrão aproximado
    return np.exp(-0.5 * ((wl - mean) / std_dev) ** 2)

sensitivity = human_eye_sensitivity(wavelengths)

# Função para converter comprimento de onda em cor aproximada
# Fonte: Visão simplificada do espectro
from matplotlib.colors import hsv_to_rgb

def wavelength_to_rgb(wl):
    if wl < 380 or wl > 780:
        return (0, 0, 0)  # Preto para fora do espectro visível
    elif wl < 440:
        return (-(wl - 440) / (440 - 380), 0, 1)  # Azul
    elif wl < 490:
        return (0, (wl - 440) / (490 - 440), 1)  # Ciano
    elif wl < 510:
        return (0, 1, -(wl - 510) / (510 - 490))  # Verde
    elif wl < 580:
        return ((wl - 510) / (580 - 510), 1, 0)  # Amarelo
    elif wl < 645:
        return (1, -(wl - 645) / (645 - 580), 0)  # Laranja
    else:
        return (1, 0, 0)  # Vermelho

# Criação do gráfico
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_alpha(0)  # Fundo transparente

# Plot da sensibilidade relativa com mudança de cor
for i in range(len(wavelengths) - 1):
    wl_start = wavelengths[i]
    wl_end = wavelengths[i + 1]
    color = wavelength_to_rgb(wl_start)
    ax.plot(wavelengths[i:i+2], sensitivity[i:i+2], color=color, lw=2)

# Adicionando uma faixa colorida abaixo do gráfico
for i in range(len(wavelengths) - 1):
    wl_start = wavelengths[i]
    wl_end = wavelengths[i + 1]
    color = wavelength_to_rgb(wl_start)
    rect = Rectangle((wl_start, -0.05), wl_end - wl_start, 0.05, color=color)
    ax.add_patch(rect)

# Configurações do gráfico
ax.set_xlim(380, 780)
ax.set_ylim(-0.1, 1.1)
ax.set_xlabel('Comprimento de Onda (nm)')
ax.set_ylabel('Sensibilidade Relativa')
ax.set_title('Sensibilidade do Olho Humano ao Espectro Eletromagnético')
ax.grid(True)

# Salvar como PNG sem fundo
plt.savefig("sensibilidade_olho_humano.png", dpi=300, transparent=True)
plt.show()

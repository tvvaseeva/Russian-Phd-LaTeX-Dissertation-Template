from matplotlib.pyplot import figure, title, plot, show
import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack

f = 10    # Частота в циклах в секунду, или в герцах
f_s = 100 # Частота дискретизации, или количество замеров в секунду

t = np.linspace(0, 2, 2 * f_s, endpoint=False)
x = np.sin(f * 2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, x)
ax.set_xlabel('Время [с]')
ax.set_ylabel('Амплитуда сигнала')
plt.tight_layout()
plt.savefig('C:/Users/sun/Documents/ДИССЕРТАЦИЯ/МОЯ ДИССЕРТАЦИЯ/Russian-Phd-LaTeX-Dissertation-Template/Presentation/images/4_01.png', dpi=600)

from scipy import fftpack

X = fftpack.fft(x)
freqs = fftpack.fftfreq(len(x)) * f_s
fig, ax = plt.subplots()
ax.stem(freqs, np.abs(X))
ax.set_xlabel('Частота в герцах [Гц]')
ax.set_ylabel('Величина частотной (спектральной) области')
ax.set_xlim(-f_s / 2, f_s / 2)
ax.set_ylim(-5, 110)
plt.tight_layout()
plt.savefig('C:/Users/sun/Documents/ДИССЕРТАЦИЯ/МОЯ ДИССЕРТАЦИЯ/Russian-Phd-LaTeX-Dissertation-Template/Presentation/images/4_02.png', dpi=600)


### Оконное преобразование
x = np.zeros(500)
x[100:150] = 1

X = fftpack.fft(x)

f, (ax0, ax1) = plt.subplots(2, 1, sharex=True)

ax0.plot(x)
ax0.set_ylim(-0.1, 1.1)

ax1.plot(fftpack.fftshift(np.abs(X)))
ax1.set_ylim(-5, 55)
plt.tight_layout()
plt.savefig('C:/Users/sun/Documents/ДИССЕРТАЦИЯ/МОЯ ДИССЕРТАЦИЯ/Russian-Phd-LaTeX-Dissertation-Template/Presentation/images/4_3.png', dpi=600)

t = np.linspace(0, 1, 500)
x = np.sin(49 * np.pi * t)

X = fftpack.fft(x)

f, (ax0, ax1) = plt.subplots(2, 1)

ax0.plot(x)
ax0.set_ylim(-1.1, 1.1)

ax1.plot(fftpack.fftfreq(len(t)), np.abs(X))
ax1.set_ylim(0, 190)
plt.tight_layout()
plt.savefig('C:/Users/sun/Documents/ДИССЕРТАЦИЯ/МОЯ ДИССЕРТАЦИЯ/Russian-Phd-LaTeX-Dissertation-Template/Presentation/images/4_4.png', dpi=600)

### Окно Кайзера

f, ax = plt.subplots()

N = 10
beta_max = 5
colormap = plt.cm.plasma

norm = plt.Normalize(vmin=0, vmax=beta_max)

lines = [
    ax.plot(np.kaiser(100, beta), color=colormap(norm(beta)))
    for beta in np.linspace(0, beta_max, N)
    ]

sm = plt.cm.ScalarMappable(cmap=colormap, norm=norm)

sm._A = []

plt.colorbar(sm).set_label(r'Кайзер $\beta$')
plt.tight_layout()
plt.savefig('C:/Users/sun/Documents/ДИССЕРТАЦИЯ/МОЯ ДИССЕРТАЦИЯ/Russian-Phd-LaTeX-Dissertation-Template/Presentation/images/4_5.png', dpi=600)

f, ax = plt.subplots()

N = 10
beta_max = 5
colormap = plt.cm.plasma

norm = plt.Normalize(vmin=0, vmax=beta_max)

lines = [
    ax.plot(np.kaiser(100, beta), color=colormap(norm(beta)))
    for beta in np.linspace(0, beta_max, N)
    ]

sm = plt.cm.ScalarMappable(cmap=colormap, norm=norm)

sm._A = []

plt.colorbar(sm).set_label(r'Кайзер $\beta$')
plt.tight_layout()
plt.savefig('C:/Users/sun/Documents/ДИССЕРТАЦИЯ/МОЯ ДИССЕРТАЦИЯ/Russian-Phd-LaTeX-Dissertation-Template/Presentation/images/4_5.png', dpi=600)

win = np.kaiser(len(t), 5)
X_win = fftpack.fft(x * win)

plt.plot(fftpack.fftfreq(len(t)), np.abs(X_win))
plt.ylim(0, 190)
plt.tight_layout()
plt.savefig('C:/Users/sun/Documents/ДИССЕРТАЦИЯ/МОЯ ДИССЕРТАЦИЯ/Russian-Phd-LaTeX-Dissertation-Template/Presentation/images/4_6.png', dpi=600)




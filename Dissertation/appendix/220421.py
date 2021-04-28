from matplotlib.pyplot import figure, title, plot, show
from numpy import array, random, kaiser, zeros, cos
import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack



rectangular_kaiser_beta = 0 # Rectangular Window
m = 51


kaiser_beta = 15    # Kaiser window beta
n = 51              # Number of points in the window

# Оконное преобразование Rectangular Window
rectangular_window = np.kaiser(m, rectangular_kaiser_beta)
X = fftpack.fft(rectangular_window)


# Оконное преобразование Kaiser window
window = np.kaiser(n, kaiser_beta)
Y = fftpack.fft(window)

figure(1)
title("Влияние прямоугольного окна на спектр сигнала")
plot(fftpack.fftshift(np.abs(X)))

figure(2)
title("Прямоугольное окно")
plot(rectangular_window)

figure(3)
title("Окно Кайзера")
plot(window)

figure(4)
title("Влияние окна Кайзера на спектр сигнала")
plot(fftpack.fftshift(np.abs(Y)))
show()
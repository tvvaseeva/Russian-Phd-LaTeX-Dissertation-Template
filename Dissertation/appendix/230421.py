from matplotlib.pyplot import figure, title, plot, show
from numpy import array, random, kaiser, zeros, cos
import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack


# Rectangular Window
rectangular_kaiser_beta = 0
m = 49

# Kaiser window beta
kaiser_beta = 15
n = 49

### Оконное преобразование Rectangular Window
rectangular_window = kaiser(m+1, rectangular_kaiser_beta)
X = fftpack.fft(rectangular_window)

### Оконное преобразование Kaiser window
window = kaiser(n+1, kaiser_beta)
Y = fftpack.fft(window)

figure(1)
title("Влияние прямоугольного окна на спектр сигнала")
plot(fftpack.fftshift(np.abs(X)))

figure(2)
title("Прямоугольное окноw")
plot(rectangular_window)

figure(3)
title("Окно Кайзера")
plot(window)

figure(4)
title("Влияние окна Кайзера на спектр сигнала")
plot(fftpack.fftshift(np.abs(Y)))
show()
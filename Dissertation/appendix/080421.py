from matplotlib.pyplot import figure, title, plot, show
from numpy import array, random, kaiser, zeros, cos
import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack

### Оконное преобразование
x = np.zeros(500)
y = np.zeros(500)
x[100:150] = 1              # Rectangular Window

kaiser_beta = 15            # Kaiser window beta
n = 49
window = kaiser(n+1, kaiser_beta)   # create symmetric window
y[100:150] = window              # Rectangular Window

X = fftpack.fft(x)
Y = fftpack.fft(y)


figure(1)
title("Влияние прямоугольного окна на спектр сигнала")
plot(fftpack.fftshift(np.abs(X)))

figure(2)
title("Прямоугольное окно")
plot(x)

figure(3)
title("Окно Кайзера")
plot(y)

figure(4)
title("Влияние окна Кайзера на спектр сигнала")
plot(fftpack.fftshift(np.abs(Y)))
show()
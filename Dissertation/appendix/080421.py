from matplotlib.pyplot import figure, title, plot, show
from numpy import array, random, kaiser, zeros, cos
import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack

### Оконное преобразование
x = np.zeros(500)
x[100:150] = 1              # Rectangular Window
kaiser_beta = 15            # Kaiser window beta
n = 49

X = fftpack.fft(x)
window = kaiser(n+1, kaiser_beta)   # create symmetric window
Y = fftpack.fft(window)

figure(1)
title("Influence of the Rectangular Window on the Signal Spectrum")
plot(fftpack.fftshift(np.abs(X)))

figure(2)
title("Rectangular window")
plot(x)

figure(3)
title("Kaiser window")
plot(window)

figure(4)
title("Influence of the Kaiser window on the Signal Spectrum")
plot(fftpack.fftshift(np.abs(Y)))
show()
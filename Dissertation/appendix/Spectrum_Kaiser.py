from numpy import array, random, kaiser, zeros, cos
from numpy.core.umath import pi
from numpy.fft import fft
from matplotlib.pyplot import figure, title, plot, show

#
#       a test signal generation
#

# signal parameters
n = 2048
harmonics = array([3, 20.1, 35.3, 51.5, 66.9])
amplitudes = array([10, 3, 1, 1, 0.2])
phases = array([0, pi/2, pi/4, pi/6, pi/8])

# generation
signal = zeros(n)
noise = random.normal(0, 0.5, n)   # powerful noise
for i in range(n):
    for j in range(len(harmonics)):
        signal[i] = signal[i] + amplitudes[j] * cos(2 * pi * harmonics[j] * i / n + phases[j])
signal = signal+noise
spectrum = fft(signal)      # for test purpose

#
#       main part, analise of signal
#

#       algorithm parameters
# window parameters
kaiser_beta = 14            # Kaiser window beta
kaiser_beta2 = 0            # Rectangular window beta
exp_ratio = 2048            # expansion ratio
delta = 5                   # delta of window for peak detection
threshold_level = 0.01      # harmonic threshold
width_window = 10           # width of window
# peak finding parameters
peak_group_distance = 5     # to find candidate to peak
peak_area_distance = 100    # to find maximum of peak

#       window
# calculate window
window = kaiser(n+1, kaiser_beta)   # create symmetric window
window_factor = pi*sum(window)/n    # window factor
# apply window to reduce a number of peak
signal2 = signal * window[0:n]


window2 = kaiser(n+1, kaiser_beta2)   # create symmetric window
window_factor2 = pi*sum(window2)/n    # window factor
signal3 = signal * window2[0:n]

# plot parameters
fmax = 100
figure(1)
title("signal")
plot(signal)

figure(2)
title("spectrum")
plot(spectrum)

figure(3)
title("Kaiser window")
plot(window)

figure(4)
title("Spectrum with Kaiser Window")
plot(abs(signal2))

figure(5)
title("Rectangular window")
plot(window2)

figure(6)
title("Spectrum with Rectangular Window")
plot(abs(signal3))
show()





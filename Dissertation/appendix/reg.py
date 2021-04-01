from numpy import array, random, kaiser, zeros, cos, angle, absolute
from numpy.core.umath import pi
from numpy.fft import fft
from matplotlib.pyplot import figure, title, plot, xlim, show

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
kaiser_beta = 14            # kaiser window beta
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

#       on board calculation
# expand signal (add zeros)
signal3 = zeros(n * exp_ratio)
signal3[0:n] = signal2
# find spectrum of the expanded signal
# use SFFT (https://groups.csail.mit.edu/netmit/sFFT/index.html) for fast calculation
spectrum3 = 2 * pi * fft(signal3) / n

#       find peak in region of interest
sp = lambda x: abs(spectrum3[x])    # for brevity
# find peak candidate
peaks = []
for i in range(100 * exp_ratio):
    if (sp(i) < sp(i + delta))\
            & (sp(i + delta) < sp(i + 2 * delta)) \
            & (sp(i + 2 * delta) > sp(i + 3 * delta))\
            & (sp(i + 3 * delta) > sp(i + 4 * delta)):
        peaks.append(i + delta)
# find groups of peak
groups = []
i = 0
while i < len(peaks):
    s = set()
    groups.append(s)
    s.add(peaks[i])
    i += 1
    while peaks[i] - peaks[i - 1] < peak_group_distance:
        s.add(peaks[i])
        i += 1
        if i == len(peaks):
            break
# find true peak
true_peaks = []
for group in groups:
    middle = sum(group)//len(group)
    harm_range = range(middle - peak_area_distance // 2,
                       middle + peak_area_distance // 2)
    ind = 0
    max = 0
    for harm in harm_range:
        if sp(harm) > max:
            ind = harm
            max = sp(harm)
    true_peaks.append(ind)
# clear small peak
real_peaks = []
threshold = 0
for peak in true_peaks:
    if sp(peak) > threshold:
        threshold = sp(peak)
threshold = threshold * threshold_level
for peak in true_peaks:
    if sp(peak) > threshold:
        real_peaks.append(peak)
# find_harmonics
found_harmonics = zeros(len(real_peaks))
found_amplitudes = zeros(len(real_peaks))
fond_phase = zeros(len(real_peaks))
for i in range(len(real_peaks)):
    peak = real_peaks[i]
    found_harmonics[i] = (peak / exp_ratio)
    harmonic = spectrum3[peak]/window_factor
    found_amplitudes[i] = (absolute(harmonic))
    fond_phase[i] = (angle(harmonic, deg=True))

#
#       results and graphics
#

print(found_harmonics)
print(found_amplitudes)
print(fond_phase)

errors_harmonics = abs(found_harmonics-harmonics)
errors_amplitudes = 100*abs(found_amplitudes-amplitudes)/amplitudes
errors_phase = abs(fond_phase-180*phases/pi)
print("Harmonics error")
print(errors_harmonics)
print("Amplitudes error, % ")
print(errors_amplitudes)
print("Phase error, degree ")
print(errors_phase)
# plot parameters
fmax = 100

figure(1)
title("signal")
plot(signal)

figure(2)
title("spectrum of expanded signal")
plot(abs(spectrum3))
xlim(0, fmax * exp_ratio)

show()





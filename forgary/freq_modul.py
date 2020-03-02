import scipy.io.wavfile as wf
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import time

sample_rate = 44100
duration = 6.0
frequency_0 = 880.0
fm_0 = 73.3333

ramp_0 = np.logspace(0, 1, int(duration * sample_rate))

x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))

wave_data = np.sin(frequency_0 * x + ramp_0 * np.sin(fm_0 * x))
wave_data = wave_data * 0.2

plot_data = wave_data[:1000]

fig, ax = plt.subplots()
ax.plot(plot_data, linewidth=3)
plt.xlabel('Sample #')
plt.ylabel('Amplitude')
plt.title('Frequency Modulation')
plt.show()

sd.play(wave_data, sample_rate)
time.sleep(duration)
sd.stop()

wave_data

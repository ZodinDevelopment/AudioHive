import scipy.io.wavfile as wf
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import time


sample_rate = 44100
duration = 3.0
frequency = 440.0

x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))
sinewave_data = np.sin(frequency * x)

# attenuate it before playing
sinewave_data = sinewave_data * 0.3


sd.play(sinewave_data, sample_rate)
time.sleep(duration)
sd.stop()

# slicing 500 samples off wav 
plot_data = sinewave_data[:500]

figure, axis = plt.subplots()
axis.plot(plot_data, linewidth=3)
plt.xlabel('Sample Number')
plt.ylabel('Amplitude')
plt.title('Sine Wave')
plt.show()

write_data = np.int16(sinewave_data * 32767)
wf.write('440Hz.wav', sample_rate, write_data)



# Add waves together to make chords, here is an E4 major guitar chord
sinewave_data = np.sin(440.0 * x) + np.sin(329.6276 * x) + np.sin(659.2551 * x)

plot_data = sinewave_data[:500]

figure,axis = plt.subplots()
axis.plot(plot_data, linewidth=3)
plt.xlabel('')
plt.ylabel('')
plt.title('Chord')
plt.show()

sd.play(sinewave_data, sample_rate)
time.sleep(duration)
sd.stop()



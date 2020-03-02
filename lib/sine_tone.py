import numpy as np
import sounddevice as sd
import time 


sample_rate = 44100

def sine_wave(duration, frequency):

    x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))

    sinewave_data = np.sin(frequency * x)

    #attenuate audio before returning

    sinewave_data = sinewave_data * 0.3

    return sinewave_data




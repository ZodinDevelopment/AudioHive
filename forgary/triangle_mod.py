import numpy as np
import sounddevice as sd
import time


def sin_wave():
    return np.sin(fm_0 * x)

def wave_data():
    return 2 / np.pi * np.arcsin(
            np.sin(frequency_0 * x + ramp_0 * sin_wave())) * 0.2

sample_rate = 44100
duration = 8.0
frequency_0 = 440
fm_0 = 100


x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))
ramp_0 = np.logspace(0, 1, int(duration * sample_rate)) * 7


result = wave_data()

sd.play(result, sample_rate)

time.sleep(duration)
sd.stop()



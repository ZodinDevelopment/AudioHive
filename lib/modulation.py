import numpy as np
import sounddevice as sd
import time

sample_rate = 44100

def modulate(duration, frequency_0, fm_0, factor):

    x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))
    wave_data = np.sin(frequency_0 * x + (np.sin(fm_0 * x) * factor))

    #attenuate wav_data times that 
    wave_data = wave_data * 0.2


    return wave_data


def phase_modulate(duration, frequency_0, fm_0):

    ramp_0 = np.logspace(0, 1, int(duration * sample_rate))

    x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))

    wave_data = np.sin(frequency_0 * x + ramp_0 * np.sin(fm_0 * x))

    wave_data = wave_data * 0.2

    return wave_data




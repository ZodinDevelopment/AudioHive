import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wf


sample_rate = 44100

def wave_chord(frequencies, duration):
    sample_rate = 44100

    x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))
    wave_data = ''

    for f in frequencies:
        tone = np.sin(f * x)

        wave_data += tone

    return wave_data


def wave_triangle(duration, frequency):
    x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))

    wave_data = 2 / np.pi * np.arcsin(np.sin(frequency * x)) * 0.5



    return wave_data



def sin_wave(fm_0, x):
    return np.sin(fm_0 * x)



def gen_data(duration, frequency_0, x):

    ramp_0 = np.logspace(0, 1, int(duration * sample_rate)) * 7


    return 2 / np.pi * np.arcsin(
            np.sin(frequency_0 * x + ramp_0 * sin_wave())) * 0.2




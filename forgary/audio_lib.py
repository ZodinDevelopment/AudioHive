import numpy as np
import sounddevice as sd
import time
import random

SAMPLE_RATE = 44100


def sine(f, x):
    y = np.sin(f * x) * 0.2
    return y

def triangle(f, x, duration):
    freq2 = random.randint(200, 600)
    freq3 = random.randint(500, 1800)
    ramp_1 = np.logspace(1, 0, int(duration * SAMPLE_RATE)) * 5

    y = 2 / np.pi * np.arcsin(np.sin(freq3 * x + ramp_1 * sine(
                              freq2, x))) * 0.2
    return y


def sawtooth(f, x):
    return -2 / np.pi * np.arctan(
            np.tan(np.pi / 2 - (x * np.pi / (1 / f * 2 * np.pi))))

def square(f, x):
    a = np.sin(f * x) / 2 + 0.5
    d = np.round(a) - 0.5
    return d



def wave_gen(wave_type, duration, frequency):
    
    x = np.linspace(0, duration * 2 * np.pi, int(duration * SAMPLE_RATE))

    if wave_type == "Sine Wave":
        
        wave_data = sine(frequency, x)

    elif wave_type == "Triangle Wave":
        wave_data = triangle(frequency, x, duration)

    elif wave_type == "Sawtooth Wave":
        wave_data = sawtooth(frequency, x)

    elif wave_type == "Square Wave":

        wave_data = square(frequency, x)

    sd.play(wave_data, SAMPLE_RATE)
    time.sleep(duration)
    sd.stop()

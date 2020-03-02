import numpy as np
import sounddevice as sd
import time


sample_rate = 44100

def tremolo(duration, frequency_0, fm_0, tremolo_frequency=8.0, ramp_amount=2.1, factor=0.9):

    ramp_0 = np.logspace(0, 1, int(duration * sample_rate)) * ramp_amount
    x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))
    x_lfo = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))

    tremolo_osc = np.sin(tremolo_frequency * x)
    tremolo_osc = (tremolo_osc * factor / 2 + (1 - factor / 2))


    wave_data = np.sin(frequency_0 * x + ramp_0 * np.sin(
                       fm_0 * x)) * tremolo_osc


    wave_data = wave_data * 0.2

    return wave_data


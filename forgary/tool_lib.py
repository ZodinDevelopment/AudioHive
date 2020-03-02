import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import scipy.io.wavfile as wf


def plot_audio(audio_wave):
    if audio_wave is None:
        return False

    figure, axis = plt.subplots()
    axis.plot(audio_wave[:500], linewidth=3.0)

    plt.title('Waveform')
    plt.xlabel('Sample Number', fontsize=15)
    plt.ylabel('Amplitude', fontsize=15)
    plt.show()



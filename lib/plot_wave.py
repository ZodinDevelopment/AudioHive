import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import scipy.io.wavfile as wf


def plot_wave_slice(wave_data):

    #slice 500 samples off wave data 
    plot_data = wave_data[:500]

    fig, ax = plt.subplots()
    ax.plot(plot_data, linewidth=3)
    plt.xlabel('Sample Number')
    plt.ylabel('Amplitude')
    plt.title('Audio Wave')
    plt.show()

    
def write_to_wav(wave_data, outfile):
    sample_rate = 44100

    write_data = np.int16(wave_data * 32767)
    wf.write(outfile, sample_rate, write_data)





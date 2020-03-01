import numpy as np
import simpleaudio 

def main():
    frequency = 440 #hz
    fs = 44100
    seconds = 3
    #generate array with seconds*sample_rate steps ranging from 0 to duration
    array = np.linspace(0, seconds, seconds * fs, False)

    #generate a 440 Hz Sine wave
    note = np.sin(frequency * array * 2 * np.pi)

    #ensure highest value is in 16 bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))

    #convert to 16 bit
    audio = audio.astype(np.int16)

    playback = simpleaudio.play_buffer(audio, 1, 2, fs)

    playback.wait_done()

if __name__ == "__main__":
    main()


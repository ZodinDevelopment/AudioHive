import numpy as np
import sounddevice as sd
import wavio 
from math import pi, sin, floor
from fractions import gcd

SAMPLE_RATE = 44100
TOTAL_WHOLE_NOTES = 16
TOTAL_EIGHTH_NOTES = TOTAL_WHOLE_NOTES * 8

WHOLE_NOTE = 16
HALF_NOTE = 8
QUARTER_NOTE = 4
EIGHTH_NOTE = 2
TEENTH_NOTE = 1

stringFreqs = {6: 277.1826, 5: 415.3047, 4: 554.3653, 3: 739.9909, 2: 932.3275, 1: 1244.508}


#get duration of a single tick based on tempo 
def time_to_sample_count(time):
    return int(time / (1000.0/SAMPLE_RATE))

def get_tick_duration(tempo):
    eith = 30.0/tempo
    return eith * 0.5

def get_tick_freq(string, fret):
    frequency = stringFreqs[string]
    f = frequency * (2**(1.0 * fret / 12.0))
    return f

def parse_tabs(tabfile):
    parsed_tab = {}
    with open(tabfile, 'r') as f:
        tabs = f.read()

        strings = tabs.split('\n')
        
        for string, key in enumerate(strings):
            parsed_tab[key + 1] = string
            tablen = len(string)
    return parsed_tab, tablen

def sine_wave(freq, tick):
    x = np.linspace(0, tick * 2 * np.pi, int(tick * SAMPLE_RATE))

    y = np.sin(freq * x)
    return y * 0.2

def generate_tick(index):
    waves = []
    tick = get_tick_duration(tempo)
    for string in parsed_tab:
        
        freq = get_tick_freq(string, parsed_tab[string][index])
            
        
        wave = sine_wave(freq, tick)
        if parsed_tab[string][index] == '-':
            wave = wave * 0.0001

        waves.append(wave)

    wave_data = waves[0] + waves[1] + waves[2] + waves[3] + waves[4] + waves[5]

    return wave_data

def render_audio():
    tabfile = '/home/toasterkief/tabs.txt'

    parsed_tab, tablen = parse_tabs(tabfile)
    wave_data = sine_wave(440, get_tick_duration(tempo)) * 0.001
    
    for i in range(0, tablen):
        tick_data = generate_tick(i)
        wave_data += tick_data

    total_length = get_tick_duration(tempo) * tablen

    sd.play(wave_data)
    time.sleep(total_length)
    sd.stop()

if __name__ == "__main__":
    tempo = 60

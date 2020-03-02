import numpy as np
import sounddevice as sd
import time
import tkinter as tk


def play():
    play_button.config(text='Wait', state='disabled')
    play_button.update()
    duration = float(duration_scale.get())
    frequency_0 = float(frequency_0_scale.get())
    fm_0 = float(fm_0_scale.get())
    ramp_amount = float(ramp_amount_scale.get())

    ramp_0 = np.logspace(0, 1, int(duration * sample_rate)) * ramp_amount
    x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))
    wave_data = np.sin(frequency_0 * x + ramp_0 * np.sin(fm_0 * x))

    wave_data = wave_data * 0.25

    sd.play(wave_data, sample_rate)
    time.sleep(duration)
    sd.stop()

    play_button.update()
    play_button.config(text="Play", state='normal')


sample_rate = 44100

root = tk.Tk()
root.geometry("400x300")

duration_label = tk.Label(root, text='Duration')
frequency_0_label = tk.Label(root, text='Frequency')
fm_0_label = tk.Label(root, text='Fm')
ramp_amount_label = tk.Label(root, text='Rampt Amount')

duration_scale = tk.Scale(root, from_=1, to=20, resolution=1, orient=tk.HORIZONTAL)
frequency_0_scale = tk.Scale(root, from_=220, to=880, resolution=10, orient=tk.HORIZONTAL)
fm_0_scale = tk.Scale(root, from_=60, to=660, resolution=10, orient=tk.HORIZONTAL)
ramp_amount_scale = tk.Scale(root, from_=0.4, to=6.0, resolution=0.2, orient=tk.HORIZONTAL)
play_button = tk.Button(root, text='Play', command=play)

duration_label.grid(row=0, column=0)
frequency_0_label.grid(row=1, column=0)
fm_0_label.grid(row=2, column=0)
ramp_amount_label.grid(row=3, column=0)
duration_scale.grid(row=0, column=1)
frequency_0_scale.grid(row=1, column=1)
fm_0_scale.grid(row=2, column=1)
ramp_amount_scale.grid(row=3, column=1)
play_button.grid(row=0, column=2)

root.mainloop()



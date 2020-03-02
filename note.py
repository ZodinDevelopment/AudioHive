import numpy as np
from math import pi, sin, floor
from fractions import gcd
import wavio

from synth import SoundGenerator
from utilities import *

#Class for a note, generates sound for each note using tempo and an envelope

class Note:
    def __init__(self, noteValue = "C4", velocity=1.0, startLocation=0, noteLength=32, waveType="Sine"):
        self.noteValue = noteValue #actual note
        self.velocity = abs(limitAmplitude(velocity)) # loudness
        self.startLocation = startLocation # 8th note count of the note
        self.noteLength = noteLength # len in 8th notes
        self.octave = int(self.noteValue[-1]) # note octave
        self.noteChar = self.noteValue[0] if len(noteValue) == 2) else self.noteValue[:2]  # character
        self.noteFrequency = getNoteFrequency(self.noteChar, self.octave)
        self.waveType = waveType

    # return a pitch changed note based on number of half steps
    def pitchChange(self, halfSteps):
        newChar, newOctave = getPitchChangedData(self.noteChar, self.octave, halfSteps)
        noteValue = newChar + str(newOctave)
        return Note(noteValue, self.velocity, self.startLocation, self.noteLength, self.waveType)

    # generate note sound
    def getNoteSound(self, tempo, envelope, applyEnvelope):
        # the duratino of the smallest possible length of a note based on tempo in secs
        lengthOf8 = getDurationOf8thNote(tempo)

        # the duration of the actual note in seconds
        duration = self.noteLength * float(lengthOf8)

        # the duration of the initial silence before note starts
        initDuration = self.startLocation * float(lengthOf8)

        # duration of the silence after the note ends
        endDuration = max((TOTAL_EIGHTH_NOTES - (self.startLocation + self.noteLength)) * float(lengthOf8), 0)

        # generate initial silence
        initialSilence = SoundGenerator(waveType="Constant", frequency=5, amplitude=0.0, duration=initDuration)

        # generate sound of note
        soundPart = SoundGenerator(waveType=self.waveType, frequency=self.noteFrequency, amplitude=self.velocity, duration=duration)

        if applyEnvelope:
            adsrEnvelope = envelope.getADSREnvelope(soundPart)

            # apply envelope
            soundPart = adsrEnvelope ** soundPart

        # generate end silence if any
        endSilence = SoundGenerator(waveType="Constant", frequency=5, amplitude=0.0, duration=endDuration)

        # Join all 3 sounds together
        return initialSilence ^ soundPart ^ endSilence

    def __str__(self):
        return f'N: {self.noteValue} |V: {str(self.velocity)} |S: {str(self.startLocation)} |L: {str(self.noteLength)} |W: {self.waveType}'


if __name__ == "__main__":
    note1 = Note(noteValue="C4", velocity=1.0, startLocation=16, noteLength=1, waveType="Sine")
    note2 = note1.pitchChange(0)
    print(note1)
    print(note2)
    noteSound = note2.getNoteSound(100)

    waveio.write('notesound.wav', noteSound)


import numpy as np
import wavio
from math import pi, sin, floor
from fractions import gcd

SAMPLE_RATE = 11250
WHOLE_NOTES = 16
EIGHTH_NOTES = WHOLE_NOTES * 8

octaveNotes = ["C", "Db", 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'B']

octaveFrequencies = [32.70, 34.65, 36.71, 38.89, 41.20, 43.65, 46.25, 49.00, 51.91, 55.00, 58.27, 61.74]

octaveDict = dict(zip(octaveNotes, octaveFrequencies))

#note lengths
WHOLE_NOTE = 8
HALF_NOTE = 4
QUARTER_NOTE = 2
EIGHTH_NOTE = 1

#convert time in milliseconds to number of samples 
def convertTimeToSampleCount(time):
    return int(time / (1000.0/SAMPLE_RATE))

# get the duration of an 8th note
def getDurationOf8thNote(tempo):
    return 30.0/tempo

#return the frequency of a note
def getNoteFrequency(noteChar, octave):
    baseFrequency = octaveDict[noteChar]
    octaveBasedFrequency = baseFrequency * (2**(octave - 1))
    return octaveBasedFrequency


#take the note, octave, and # of half steps and return a pitch change
def getPitchChangedData(noteChar, octave, halfSteps):

    octaveChange = floor(float(halfSteps) / 12.0)
    noteTypeChange = halfsteps % 12

    newOctave = octave + octaveChange
    newChar = octaveNotes[octaveNotes.index(noteChar) + noteTypeChange]

    return (newChar, newOctave)

def limitAmplitude(amplitude):
    return max(min(float(amplitude), 1.0), -1.0)



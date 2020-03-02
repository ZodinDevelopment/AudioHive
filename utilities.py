import numpy as np
import wavio
import simpleaudio
from math import pi, sin, floor
from fractions import gcd

from SoundGenerator import *

SAMPLE_RATE = 11250
TOTAL_WHOLE_NOTES = 16 # MAXIMUM LENGTH OF SCORE
TOTAL_EIGHTH_NOTES = TOTAL_WHOLE_NOTES * 8 

#note characters
octave1Notes = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

octave1Frequencies = [32.70, 34.65, 36.71, 38.89, 41.20, 43.65, 46.25, 49.00, 51.91, 55.00, 58.27, 61.74]

octave1Dict = dict(zip(octave1Notes, octave1Frequencies))

#note lengths
WHOLE_NOTE = 8
HALF_NOTE = 4
QUARTER_NOTE = 2
EIGHTH_NOTE = 1

#convert time in ms to number of samples needed 
def convertTimeToSampleCount(time):
    return int(time / (1000.0/SAMPLE_RATE))

# get duration of an 8th note
def getDurationOf8thNote(tempo):
    return 30.0/tempo

#return the frequency of a note 
def getNoteFrequency(noteChar, octave):
    baseFrequency = octave1Dict[noteChar]
    octaveBasedFrequency = baseFrequency * ( 2**(octave - 1) )
    return octaveBasedFrequency

#takes note char, current octave, and # of halfsteps and return the pitch changed note data
def getPitchChangedData(noteChar, octave, halfSteps):

    octaveChange = floor(float(halfSteps) / 12.0)
    noteTypeChange = halfSteps % 12

    newOctave = octave + octaveChange
    newChar = octave1Notes[octave1Notes.index(noteChar) + noteTypeChange]

    return(newChar, newOctave)


def limitAmplitude(amplitude):
    return max(min(float(amplitude), 1.0), -1.0)



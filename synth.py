import numpy as np
import wavio
import simpleaudio
from math import pi, sin, floor
from fractions import gcd

from utilities import *

class SoundGenerator():

    #constants
    def __init__(self, waveType="Sine", frequency=500, amplitude=1.0, duration=5):
        #Initialize internal
        self.waveType = str(waveType)
        self.frequency = float(frequency)
        self.amplitude = limitAmplitude(amplitude)
        self.duration = float(duration)
        self.sampleCount = self.getSampleCount()
        self.sound = np.array([])
        self.limit = np.vectorize(limitAmplitude)

        #generate sound
        if (waveType == "Sine"):
            self.sound = self.generateSineWave()
        elif (waveType == "Square"):
            self.sound = self.generateSquareWave()
        elif (waveType == "Sawtooth"):
            self.sound = self.generateSawtoothWave()
        elif (waveType == "Constant"):
            self.sound = self.generateConstantWave()

        elif (waveType == "Noise"):
            self.sound = self.generateWhiteNoiseWave()

        elif (waveType == "Combination"):
            self.sound = self.sound

    def getSampleCount(self):
        return int(self.duration * SAMPLE_RATE)
        pass

    def getSinglePhaseArray(self):
        singleCycleLength = SAMPLE_RATE / float(self.frequency)
        omega = pi * 2 / singleCycleLength
        phaseArray = np.arrange(0, int(singleCycleLength)) * omega
        return phaseArray

    
    def generateSineWave(self):
        phaseArray = self.getSinglePhaseArray()

        singleCycle = self.amplitude * np.sin(phaseArray)

        return np.resize(singleCycle, (self.sampleCount,)).astype(np.float)

    def generateSquareWave(self):
        return self.amplitude * np.sign(self.generateSineWave())


    def generateSawtoothWave(self):
        phaseArray = self.getSinglePhaseArray()

        piInverse = 1/pi
        saw = np.vectorize(lambda x: 1 - piInverse*x)
        singleCycle = self.amplitude * saw(phaseArray)

        return np.resize(singleCycle, (self.sampleCount,)).astype(np.float)

    def generateConstantWave(self):
        phaseArray = self.getSinglePhaseArray()
        singleCycle = self.amplitude

        return np.resize(singleCycle, (self.sampleCount,)).astype(np.float)

    def generateWhiteNoiseWave(self):
        return np.random.uniform(-1, 1, self.getSampleCount())


    def combineSounds(self, soundObj, operator = "+"):
        if len(self.sound) < len(soundObj.getSound()):
            minSound = np.copy(self.getSound())
            maxSound = np.copy(soundObj.getSound())

        else:
            maxSound = np.copy(self.getSound())
            minSound = np.copy(soundObj.getSound())


        if operator == "+":
            maxSound[0:len(minSound)] = maxSound[0:len(minSound)] + minSound

        elif operator == "-":
            maxSound[0:len(minSound)] = maxSound[0:len(minSound)] - minSound

        elif operator == "*":
            maxSound[0:len(minSound)] = maxSound[0:len(minSound)] * minSound


        newSound = self.limit(maxSound)

        newFrequency = int(self.getFrequency()) * int(soundObj.getFrequency()) / gcd(int(self.getFrequency()), int(soundObj.getFrequency()))
        newDuration = float(len(newSound)) / SAMPLE_RATE
        newAmplitude = np.max(newSound)

        returnObj = SoundGenerator(waveType = "Combination", frequency = newFrequency, amplitude = newAmplitude, duration = newDuration)

        returnObj.setSound(newSound)
        return returnObj

    def __add__(self, soundObj):
        return self.combineSounds(soundObj, "+")

    def __sub__(self, soundObj):
        return self.combineSounds(soundObj, '-')

    def __mul__(self, soundObj):
        if isinstance(soundObj, int) or isinstance(soundObj, float):
            scaleFactor = limitAmplitude(soundObj)
            if (scaleFactor < 0):
                scaleFactor = 0.0

            returnObj = SoundGenerator(self.waveType, self.frequency, self.amplitude * scaleFactor, self.duration)
            sound = self.getSound()
            returnObj.setSound(sound * scaleFactor)
            return returnObj

        return self.combineSounds(soundObj, '*')

    def __xor__(self, soundObj):
        newSound = np.append(self.getSound(), soundObj.getSound())

        newFrequency = int(self.getFrequency()) * int (soundObj.getFrequency()) / gcd(int(self.getFrequency()), int(soundObj.getFrequency()))
        newDuration = self.getDuration() + soundObj.getDuration()
        newAmplitude = np.max(newSound)

        returnObj = SoundGenerator(waveType = "Join", frequency=newFrequency, amplitude=newAmplitude, duration=newDuration)

        returnObj.setSound(newSound)

        return returnObj

    def __pow__(self, soundObj):
        if len(self.sound) < len(soundObj.getSound()):
            minSound = np.copy(self.getSound())
            maxSound = np.copy(soundObj.getSound())

        else:
            maxSound = np.copy(self.getSound())
            minSound = np.copy(oundObj.getSound())

        minSound = np.resize(minSound, (len(maxSound),))

        newDuration = float(len(maxSound))/SAMPLE_RATE

        minSoundObj = SoundGenerator(waveType = "Temp", frequency = 100, amplitude=np.max(minSound), duration=newDuration)
        minSoundObj.setSound(minSound)

        maxSoundObj = SoundGenerator(waveType="Temp", frequency=100, amplitude=np.max(maxSound), duration=newDuration)
        maxSoundObj.setSound(maxSound)


    def __str__(self):
        return f"WT: {self.waveType} F: {str(self.frequency)} A: {str(self.amplitude)} D: {str(self.duration)}"

    def getSound(self):
        return self.sound

    def setSound(self, soundArray):
        self.sound = soundArray

    def getFrequency(self):
        return self.frequency

    def getDuration(self):
        return self.duration

    def shiftBy(self, numberOfSamples):
        sound = self.getSound()
        sound = np.roll(sound, numberOfSamples)
        sound = np.append(np.zeros(numberofSamples), sound[numberofSamples:])

        retSoundObj = SoundGenerator(self.waveType, self.frequency, self.amplitude, self.duration)
        retSoundObj.setSound(sound)

        return retSoundObj

def main():
    sin1 = SoundGenerator(waveType="Sine", duration=3.0)
    sqr1 = SoundGenerator(waveType="Square", frequency=400.0, amplitude=0.2, duration=3.0)
    sqr2 = SoundGenerator(waveType="Square", frequency=500.0, amplitude=0.2, duration=3.0)
    saw1 = SoundGenerator(waveType="Sawtooth", duration = 3)

    note1 = SoundGenerator(waveType="Square", frequency=400.0, amplitude=0.2, duration=5.0)
    note2 = SoundGenerator(waveType="Square", frequency=450.0, amplitude=0.2, duration=5.0)
    note3 = SoundGenerator(waveType="Square", frequency=600.0, amplitude=0.2, duration=5.0)
    note4 = SoundGenerator(waveType="Square", frequency=700.0, amplitude=0.1, duration=5.0)
    note5 = SoundGenerator(waveType="Square", frequency=800.0, amplitude=0.1, duration=5.0)




    chord1 = note1 + note2 + note3 + (note4 * 0.5) + note5

    join1 = sin1 ^  sqr1 ^ sqr2 ^ saw1 ^ chord1
    mod1 = SoundGenerator(waveType="Square", frequency=3.0, amplitude=1.0, duration=3.0)
    modjoin1 = mod1 ** join1

    wavio.write("output.wav", modjoin1, SAMPLE_RATE)

if __name__ == "__main__":
    main()



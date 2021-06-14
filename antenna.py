#!/usr/bin/python3

import numpy as np;

# we abuse the complex data type as a 2D vector to simplify things
# waveLength in metres
#
# This formula is valid at distances greater than twice the wavelength
#
def calcSignalVectorFromAntenna(antennaPos : np.csingle, myPos : np.csingle, waveLength : float) -> np.csingle : 

    distance = np.absolute(myPos - antennaPos)  # calculates the Euclidian norm i.e. the distance

    amplitude = 1.0/(distance*waveLength)
    wavelengths = distance / waveLength

    signal = amplitude * (np.cos(-2*np.pi*wavelengths) + 1j*np.sin(-2*np.pi*wavelengths))

    return signal

def printSignal(sig : np.csingle):
    print("  amplitude: ", np.absolute(sig))
    print("  angle    : ", np.angle(sig)/np.pi*180.0)

print("Signal at a distance of 20m from an antenna TXing on 40m")
printSignal(calcSignalVectorFromAntenna(0,20,40))

print("Combined signal from two 40m TX antennas at (-20,0) and (20,0) observed at (0,0)")
printSignal(calcSignalVectorFromAntenna(-20,0,40) + calcSignalVectorFromAntenna(20,0,40))


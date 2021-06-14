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

printSignal(calcSignalVectorFromAntenna(0,40,40))

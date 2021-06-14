#!/usr/bin/python3
# see: https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781849513265/6/ch06lvl1sec68/visualizing-a-2d-scalar-field

import numpy as np;
from matplotlib import pyplot as plt
import matplotlib.cm as cm 

# we abuse the complex data type as a 2D vector to simplify things
# waveLength in metres
# txphase is in degrees
#
# This formula is valid at distances greater than twice the wavelength
#
def calcSignalVectorFromAntenna(antennaPos : np.csingle, myPos : np.csingle, waveLength : float, txphase : float) -> np.csingle : 

    distance = np.absolute(myPos - antennaPos)  # calculates the Euclidian norm i.e. the distance

    amplitude = 1.0/(distance*waveLength)
    #amplitude = 1
    wavelengths = distance / waveLength + txphase / 360.

    signal = amplitude * (np.cos(-2*np.pi*wavelengths) + 1j*np.sin(-2*np.pi*wavelengths))

    return signal

def displayPattern():
    # fixed antenna locations
    ant1Location = -10.  # (-20, 0)
    ant2Location =  10.  # ( 20, 0)

    txphase = -45.

    viewWidth    = 800.  # 800 metre view on both sides

    n = 256 
    x = np.linspace(-viewWidth, viewWidth, n) 
    y = np.linspace(-viewWidth, viewWidth, n) 
    X, Y = np.meshgrid(x, y)

    amp = np.zeros((n,n))
    idx1 = 0
    for xx in x:
        idx2 = 0
        for yy in y:
            amplitude = np.absolute(calcSignalVectorFromAntenna(ant1Location, xx + 1.j*yy, 40, 0) + calcSignalVectorFromAntenna(ant2Location, xx + 1.j*yy, 40, txphase))
            amp[idx1, idx2] = 20.0*np.log10(amplitude)
            idx2 = idx2 + 1
        idx1 = idx1 + 1

    plt.figure(1)
    plt.pcolormesh(X, Y, amp, cmap = cm.gray) 

    # plot horizontal axis signal strength
    amp1 = np.zeros((n,1))
    amp2 = np.zeros((n,1))
    idx1 = 0
    for xx in x:
        amplitude1 = np.absolute(calcSignalVectorFromAntenna(ant1Location, 1j*xx, 40, 0) + calcSignalVectorFromAntenna(ant2Location, 1j*xx, 40, txphase))
        amp1[idx1] = 20.0*np.log10(amplitude1)
        amplitude2 = np.absolute(calcSignalVectorFromAntenna(ant1Location, xx, 40, 0) + calcSignalVectorFromAntenna(ant2Location, xx, 40, txphase))
        amp2[idx1] = 20.0*np.log10(amplitude2)
        idx1 = idx1 + 1
    
    plt.figure(2)
    plt.plot(x, amp1, x, amp2)
    plt.xlabel("distance (m)")
    plt.ylabel("amplitude (dB)")
    plt.show()

def printSignal(sig : np.csingle):
    print("  amplitude: ", np.absolute(sig))
    print("  angle    : ", np.angle(sig)/np.pi*180.0)

print("Signal at a distance of 20m from an antenna TXing on 40m")
printSignal(calcSignalVectorFromAntenna(0,20,40,0))

print("Combined signal from two 40m TX antennas at (-20,0) and (20,0) observed at (0,0)")
printSignal(calcSignalVectorFromAntenna(-20,0,40,0) + calcSignalVectorFromAntenna(20,0,40,0))

displayPattern()


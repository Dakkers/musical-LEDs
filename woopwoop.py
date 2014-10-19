from numpy import array, int16, reshape, append, zeros
from scipy.io.wavfile import read, write
from matplotlib.pyplot import plot
from numpy.fft import rfft

FILENAME = "C-Jam_Blues.wav"


# Read in .wav file and put in array called data.
def soundIn(f):
    inwav = read(f)             # Read in sound sample.
    samprate = inwav[0]         # Extract sample rate.
    data = inwav[1][:,0]        # Extract data list.
    return data, samprate

def binarify(arr):
    """performs fft, sort frequency into numbered LEDs, and converts to binary"""
    thresh = 1000
    freqs = [10,20,30,50,70,100,150,200,300,400,600,900,1200,2000,3000,5000]

    #perform descrete fourier transform
    fdata = rfft(arr).tolist()
    histo = zeros(len(freqs),1)
    AA, BB = 0, 0

    #form 16 element array
    freqOld = 0
    for i in xrange(len(freqs)):
        freqNew = freqs[i]
        histo[i] = sum(fdata[freqOld:freqNew])
        freqOld = freqNew

    #rearrange LED order now
    #create AA and BB in decimal using binary operations
    for i in range(8):
        if histo[i] > thresh:
            AA += 2**i
        if histo[i+8] > thresh:
            BB += 2**i

    return bin(AA), bin(BB)

#extract
try:
    wdata, samprate = soundIn(FILENAME)

    #delay in LED
    delay = samprate / 4

    #trimmed data for proper dimensions in 2D array
    w2data = append(wdata, zeros((delay - len(wdata)%delay), dtype=int16))
      
    #reshapes to 2D array
    w3data = reshape(w2data, (len(w2data)/delay, delay))

    #creates the array for Arduino
    arrLED = zeros(len(w3data), i)
    for i in xrange(len(w3data)):
        arrLED[i] = binarify(w3(data))

except IOError:
    raise IOError("File '%s' not found!" %FILENAME)
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

def binarify(mat):
    """performs fft, sort frequency into numbered LEDs, and converts to binary"""
    thresh = 1000
    freqs = [10,20,30,50,70,100,150,200,300,400,600,900,1200,2000,3000,5000]

    #perform descrete fourier transform
    fdata = rfft(mat)
    histo = zeros((len(fdata),len(freqs)))
    binaryData = zeros((len(histo), 2))

    for i in xrange(len(fdata)):
        row = fdata[i]
        freqOld = 0
        for j in xrange(len(freqs)):
            freqNew = freqs[j]
            histo[i,j] = sum(row[freqOld:freqNew])
            freqOld = freqNew

    #rearrange LED order now
    #create AA and BB in decimal using binary operations

    for i in xrange(len(histo)):
        for j in xrange(8):
            if histo[i,j] > thresh:
                binaryData[i,0] += 2**j
            if histo[i,j+8] > thresh:
                binaryData[i,1] += 2**j

    return [[str(bin(int(j)))[2:].zfill(8) for j in i] for i in binaryData]

#extract
try:
    #wdata is a 1D array of amplitudes
    wdata, samprate = soundIn(FILENAME)

    #delay in LED
    delay = samprate / 4

    #trimmed data for proper dimensions in 2D array
    w2data = append(wdata, zeros((delay - len(wdata)%delay), dtype=int16))
      
    #reshapes to 2D array
    w3data = reshape(w2data, (len(w2data)/delay, delay))

    #creates the array for Arduino
    print binarify(w3data)

except IOError:
    raise IOError("File '%s' not found!" %FILENAME)
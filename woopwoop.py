from numpy import array, int16, reshape, append, zeros
from scipy.io.wavfile import read, write
from matplotlib.pyplot import plot
from numpy.fft import rfft, irfft

thresh = 1000
freq = [10,20,30,50,70,100,150,200,300,400,600,900,1200,2000,3000,5000]

# Read in .wav file and put in array called data.
def soundIn(f):
    inwav = read(f)             # Read in sound sample.
    samprate = inwav[0]         # Extract sample rate.
    data = inwav[1][:,0]        # Extract data list.
    return data, samprate

# Normalize and output sound clip.
def soundOut(data, samprate):
    maxdata = 32767/max(abs(data))
    normdata = maxdata*data
    data2 = array([normdata,normdata],dtype=int16).T
    write("new.wav",samprate,data2)     # Save as .wav file.

#performs fft, sort frequency into LED, and converts to hex
def hexify(i):
    #perform descrete fourier transform
    fdata = rfft(i)
    fdata.tolist()
    histo = []
    AA, BB = 0, 0
    #form 16 element array
    j = 0
    for k in freq:
        histo.append(sum(fdata[j:k]))
        j=k
    #rearrange LED order now
    
    #create AA and BB in decimal using binary operations
    for m in range(8):
        if histo[m] > thresh:
            AA += 2**m
        if histo[m+8] > thresh:
            BB += 2**m
    #convert to hex
    return bin(AA), bin(BB)

#extract
wdata, samprate = soundIn("C-Jam_Blues.wav") 

#delay in LED
delay = samprate / 4

#trimmed data for proper dimensions in 2D array
w2data = append(wdata, zeros((delay - len(wdata)%delay), dtype=int16))
  
#reshapes to 2D array
w3data = reshape(w2data, (len(w2data)/delay, delay))

#creates the array for Arduino
arrLED = []
for i in w3data:
    arrLED.append(hexify(i))
    
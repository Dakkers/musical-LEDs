import serial, time
ser = serial.Serial('/dev/ttyACM0', 9600)
FILENAME = 'DATA.txt'

try:
	f = open(FILENAME)
	for line in f.readlines():
		ser.write(line.strip())
		time.sleep(0.250)

	ser.close()
	
except IOError:
	raise IOError("File '%s' not found!" %FILENAME)
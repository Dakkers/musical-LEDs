import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

# temp data.
ser.write('01101101,11111111,543')	

ser.close()
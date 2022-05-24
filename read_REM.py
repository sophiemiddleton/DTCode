# Read data coming from the REM 500 Neutron Survey Meter through a RS-232 serial cable

# Authors: Leo Borrel, Sophie Middleton
# Date: 2022-05-13


import serial
import binascii
from time import sleep

# Set up port
 ser = serial.Serial('/dev/tty.usbserial-AB0K01H7',9600,timeout=100) # Sophie's Macbook

ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE


# Create output text file
outputfile = open("raw_data.txt","w")
channelfile = open("channel_data.txt","w")

# Check if port is open
try:
    ser.isOpen()
    print("is open")
except:
    print("error: port is close")
    exit()

# Available commands to send
go = 'G'.encode('utf-8') # start the run
stop = 'S'.encode('utf-8') # stop the run
check = 'C'.encode('utf-8') # turn on and off the source in the detector
reset = 'R'.encode('utf-8') # reset data and timer
dump = 'DA'.encode('utf-8') # Dump the data for each channel
dump_read = 'D\r\n'.encode('utf-8')

# Read/Write
if(ser.isOpen()):
    serial_string = ""
    try:
        # Reset data and start the run
        ser.write(reset)
        ser.write(go)
        ser.write(check)

        # read data for the set runtime
        runtime = 10 # in seconds
        t = 0
        while(t <= runtime): # add X seconds to take into account the time to start
            serial_string = ser.readline()
            print(serial_string)
            outputfile.write(serial_string.decode('utf-8'))
            sleep(1)
            t = t + 1

        # stop the run and turn off the source
        ser.write(stop)
        ser.write(check)
        ser.write(dump)
        while (serial_string != dump_read):
            # read each line:
            serial_string = ser.readline()
            # print to screen:
            print(serial_string)
            # write and decode the output to readable format:
            outputfile.write(serial_string.decode('utf-8'))
        # read and combine channels:
        for i in range(256):
            # read line:
            serial_string = ser.readline()
            # print to screen:
            print(serial_string)
            # write channel output in readable format:
            channelfile.write(serial_string.decode('utf-8'))
        serial_string = ser.readline()
        print('remaining: ', serial_string)
        serial_string = ser.readline()
        print('remaining: ', serial_string)
    except Exception:
        print("Error: cannot read/write")
else:
    print("Error: cannont open port")

# close text file
outputfile.close()
channelfile.close()

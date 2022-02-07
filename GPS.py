import serial
#run de volgende line om een lijst met poorten te krijgen
#python -m serial.tools.list_ports
import pynmea2
import pandas as pd
import time
import io

def locatie():
    while 1:
        try:
            global ser
            ser = serial.Serial('COM4',4800, timeout=3)
            sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
            line = sio.readline()

            line = line.split(",")
            if str(line[0]) == str('$GPGGA'):
                Data = line
                Data = [float(line[1]), float(line[2])/100, float(line[4])]
                ser.close()
                return Data
            else:
                continue
        except serial.SerialException as e:
            ser.close()


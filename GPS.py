import serial
#run de volgende line om een lijst met poorten te krijgen
#python -m serial.tools.list_ports
import pynmea2
import pandas as pd
import time as t
import io

def locatie():
    while 1:
        try:
            global ser
            ser = serial.Serial('COM6',4800, timeout=3)
            sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
            line = sio.readline()

            match = line.split(",")
            if str(match[0]) == str('$GPGGA'):
                parsed = pynmea2.parse(line)
                Data = [float(parsed.lat)/100, float(parsed.lon)/100, str(parsed.timestamp)]
                ser.close()
                return Data
            else:
                continue
        except serial.SerialException as e:
            ser.close()


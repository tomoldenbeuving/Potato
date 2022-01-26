import serial
#run de volgende line om een lijst met poorten te krijgen
#python -m serial.tools.list_ports
import pynmea2
import pandas as pd
import time
import io
def locatie():
    global ser
    ser = serial.Serial('COM4',4800, timeout=3)
    sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
    i=0
    while i < 1:
        try:
            line = sio.readline()
            msg = pynmea2.parse(line)
            repr(msg)
            i += 1
            ser.close()
            print(
                msg.timestamp,",",msg.lat,",",msg.lon
            )
        except serial.SerialException as e:
            print('Device error: {}'.format(e))
            break
        except pynmea2.ParseError as e:
            print('Parse error: {}'.format(e))
            continue        



import serial
#run de volgende line om een lijst met poorten te krijgen
#python -m serial.tools.list_ports
import pynmea2
import pandas as pd
import time
import io


# import pynmea2
# msg = pynmea2.parse("$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D")
# msg


class loc:
    def lon():
        global ser
        ser = serial.Serial('COM4',4800, timeout=3)
        sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
        line = sio.readline()
        i=0
        while i < 1:
            try:
                msg = pynmea2.parse(line)
                repr(msg)
                i += 1
                return msg.lon
            except serial.SerialException as e:
                print('Device error: {}'.format(e))
                break
            except pynmea2.ParseError as e:
                print('Parse error: {}'.format(e))
                continue
    
    def lat():
        global ser
        ser = serial.Serial('COM4',4800, timeout=3)
        sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
        line = sio.readline()
        i=0
        while i < 1:
            try:
                msg = pynmea2.parse(line)
                repr(msg)
                i += 1
                return msg.lat
            except serial.SerialException as e:
                print('Device error: {}'.format(e))
                break
            except pynmea2.ParseError as e:
                print('Parse error: {}'.format(e))
                continue

    def time():
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
                print(msg.timestamp,msg.lat,msg.lon)
            except serial.SerialException as e:
                print('Device error: {}'.format(e))
                break
            except pynmea2.ParseError as e:
                print('Parse error: {}'.format(e))
                continue        



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
            print(msg.timestamp,msg.lat,msg.lon)
        except serial.SerialException as e:
            print('Device error: {}'.format(e))
            break
        except pynmea2.ParseError as e:
            print('Parse error: {}'.format(e))
            continue        

locatie()



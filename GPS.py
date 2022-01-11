import serial
import pandas as pd
#run de volgende line om een lijst met poorten te krijgen
#python -m serial.tools.list_ports

df = pd.read_csv('data.csv')

from pynmeagps import NMEAReader
stream = serial.Serial('COM4',4800, timeout=3)
nmr = NMEAReader(stream)
(raw_data, parsed_data) = nmr.read()
print(parsed_data.lat ,"," ,parsed_data.lon ,"," ,parsed_data.time)

stream.close()

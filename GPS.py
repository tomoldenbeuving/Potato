import serial
#run de volgende line om een lijst met poorten te krijgen
#python -m serial.tools.list_ports
from pynmeagps import NMEAReader
stream = serial.Serial('COM3', 9600, timeout=3)
nmr = NMEAReader(stream)
(raw_data, parsed_data) = nmr.read()
print(parsed_data)

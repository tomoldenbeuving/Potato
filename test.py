import time as tm

from pynmeagps import NMEAReader
msg = NMEAReader.parse('$GNGLL,5327.04319,S,00214.41396,E,223232.00,A,A*68\r\n')
print(msg.lat, msg.lon, msg.time)
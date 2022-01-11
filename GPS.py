import serial
#run de volgende line om een lijst met poorten te krijgen
#python -m serial.tools.list_ports
from pynmeagps import NMEAReader



class loc:
    stream = serial.Serial('COM4',4800, timeout=3)
    nmr = NMEAReader(stream)

    global parsed_data
    (raw_data, parsed_data) = nmr.read()
    
    
    def lon():
        return parsed_data.lon
    
    def lat():
        return parsed_data.lat

    def time():
        return parsed_data.time
    
    stream.close()



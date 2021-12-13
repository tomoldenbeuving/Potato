import gpsd
gpsd.connect(host="127.0.0.1", port=123456)
packet = gpsd.get_current()

def GPS():
    pass

GPS()

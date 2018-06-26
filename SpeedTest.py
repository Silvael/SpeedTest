# speedTest in Python 3.6
# Quelle unbekannt  - Basis im Internet gefunden war aber unvollständig
#before usage goto http://www.speedtestx.de and fill out the captcha to get download permission
# !/usr/bin/python
import urllib.request
import urllib.error
import urllib
import time
from datetime import datetime
import sys
import os


#52.428.800

# Geschwindigkeit messen findet in dieser Funktion statt
def measure(url="http://www.speedtestx.de/testfiles/data_50mb.test", buf=1024):
    tStart = datetime.now()
    amount = 0
    x = 0

    f = urllib.request.urlopen(url)
    # schleife liest in  buf  - beim letzten Mal ist len < buf
    while ((len(f.read(buf)) == buf) ):
        print("#")
        amount = amount + buf
        tEnd = datetime.now()

    dif = (tEnd - tStart).total_seconds()

    # wenn fertig berechne
    print (time.strftime("%H:%M:%S; "))
    print("Data loaded:  " + str(amount))
    speed = ((amount  / 10000.00) * 8) / 1024
    print (str(speed) + " Mbit/s")

#main
try:
    measure()
    #measure(buf=1024)
    #measure( url="http://www.speedtestx.de/testfiles/data_50mb.test", buf=102400)
except  KeyboardInterrupt:

    exit(0)

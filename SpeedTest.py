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


# Geschwindigkeit messen findet in dieser Funktion statt
def measure(url="http://www.speedtestx.de/testfiles/data_50mb.test", intervall=2, buf=10):
    tStart = datetime.now()
    amount = 0
    x = 0

    f = urllib.request.urlopen(url)
    # schleife liest in  buf
    while ((len(f.read(buf)) == buf) and (x <= 60)):
        print("#")
        amount = amount + buf
        tEnd = datetime.now()

    dif = (tEnd - tStart).total_seconds()

    # wenn fertig berechne   - unklar zu was der else Teil benötigt wird
    if (dif >= intervall):
        print (time.strftime("%H:%M:%S; "))
        speed = (((amount / intervall) / 1000.00) * 8) / 1024
        print (str(speed) + " Mbit/s")

        amount = 0
        tStart = datetime.now()
        x = x + 1

    else:
        print("whats this ?")
        amount = amount + buf


try:
    measure(buf=1024, intervall=1)
    #measure( url="http://www.speedtestx.de/testfiles/data_50mb.test", buf=102400, intervall=1)
except  KeyboardInterrupt:

    exit(0)

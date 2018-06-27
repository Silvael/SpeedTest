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
def measure(url="http://www.speedtestx.de/testfiles/data_100mb.test", buf=1024):
    try:
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
        print("Seconds total: " + str(dif))
        print("Data loaded:  " + str(amount) + " bytes  == " + str( (amount / 1024) /1024 ) + " Megabyte ")
        speed = amount * 8  / 1000000 / dif
        print ("Speed: " + str(speed) + " Mbit/s  (  calculated by formula:  data in bytes * 8  : 1.000.000 : seconds )" )
    except:
        print("open the URL http://www.speedtestx.de/  in Your browser and fill out the captcha")



#main
try:
    #measure()
    measure(buf=1024)
    #measure( url="http://www.speedtestx.de/testfiles/data_500mb.test", buf=102400)
except  KeyboardInterrupt:

    exit(0)

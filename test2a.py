import os
import sys
import random
import subprocess

btngray = ['http://stream.srg-ssr.ch/m/rsj/mp3_128?ref=L1St3N',
           'http://94.23.201.38:8020/stream',
           'http://89.16.185.174:8000/stream',
           'http://playerservices.streamtheworld.com/api/livestream-redirect/SUBLIME.mp3',
           'http://jazzradio.ice.infomaniak.ch/jazzradio-high.mp',
           'http://icecast.omroep.nl/radio6-bb-mp3',
           'http://stream.srg-ssr.ch/m/drs2/mp3_128',
           'http://edge-ads-02-gos1.sharp-stream.com/jazzfmmobile.mp3?ref=L1St3',
           'http://radiart.eu:10024/stream',
           'http://192.99.34.205:8399/stream',
           'http://east-mp3-128.streamthejazzgroove.com/',
           'http://west-mp3-128.streamthejazzgroove.com/?origine=1djfk']

btngray_choice = random.choice(btngray)

print ("Randomly selected item from list is ", btngray_choice)

#remove meta tag feed and added buffer to reduce pop
#subprocess.call(['mpg123', btngray_choice])
subprocess.call(['mpg123', '-q', btngray_choice, " --preload 1"])


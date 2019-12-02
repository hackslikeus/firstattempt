import os
import sys
import random
import subprocess

btn1234 = ['http://streams.bigfm.de/bigfm-deutschland-128-mp3?usid=0-0-H-M-V-08',
	   'http://radio.itconnect.se/rb3',
	   'http://stream.basefm.co.nz:8000/Base320MP3',
	   'http://192.99.39.108:7649/STREAM',
	   'http://fluxfm.hoerradar.de/flux-boomfm-mp3-hq',
	   'http://5.63.151.52:7082/stream',
	   'http://icy.unitedradio.it/101Hipster.mp3',
	   'http://air.radiorecord.ru:8102/yo_320',
	   'http://stream.secousse.org:8000/secousse-street',
	   'http://listen.thenumberz.fm:8000/stream',
	   'http://212.48.67.46:8000/']

btn1234_choice = random.choice(btn1234)

print ("Randomly selected item from list is ", btnpurp_choice)

subprocess.call(['mpg123', btn1234_choice])



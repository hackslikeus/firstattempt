import os
import sys
import random
import subprocess

btn1234 = ['http://stream.zeno.fm/nxwm3y6ma9quv',
	   'http://144.217.253.136:8433/stream',
	   'http://fluxfm.hoerradar.de/flux-event01-mp3-hq',
	   'http://streaming.shoutcast.com/Lozenets',
	   'http://192.227.116.104:8306/stream',
	   'http://192.99.34.205:8222/stream',
	   'http://188.138.198.247:8002/',
	   'http://manager1.creativradio.pro:2100/stream',
	   'http://listen.radioking.com/radio/117271/stream/159004',
	   'http://0n-chillout.radionetz.de/0n-chillout.mp3',
	   'http://1a-chillout.radionetz.de/1a-chillout.mp3']

btn1234_choice = random.choice(btn1234)

print ("Randomly selected item from list is ", btn1234_choice)

subprocess.call(['mpg123', btn1234_choice])



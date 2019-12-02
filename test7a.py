import os
import sys
import random
import subprocess

btnbrwn = ['http://radio.1jazz.ru:8280/radio',
	   'http://wms-13.streamsrus.com:16510',
	   'http://streaming.radionomy.com/BigBandMagic?AppName=vTuner',
	   'http://streams.calmradio.com/api/177/128/stream',
	   'http://classicempire-radio.stream.laut.fm/classicempire-radio?ref=vtuner',
	   'http://206.72.196.133:8000/stream',
	   'http://173.244.215.163:8430',
	   'http://agnes.torontocast.com:8151/stream',
	   'http://streams.radioriel.org:8040/stream',
	   'http://hanseswing.stream.laut.fm/hanseswing?ref=vtuner',
	   'http://relay.publicdomainproject.org:80/jazz_swing.mp3']

btnbrwn_choice = random.choice(btnbrwn)

print ("Magic 8 Ball radio has chosen ", btnbrwn_choice)

#subprocess.call(['mpg123', btnbrwn_choice])
subprocess.call(['mpg123', '-q', btnbrown_choice, " --preload 1"])

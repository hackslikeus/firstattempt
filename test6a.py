import os
import sys
import random
import subprocess

btnpurp = ['http://5.39.71.159:8942/stream',
	   'http://192.99.41.102:5304/stream',
	   'http://tachyon.shoutca.st:8306/stream',
	   'http://latino.ohmylatino.com/reggaeton.mp3',
	   'http://www.partyvibe.com:8000/',
	   'http://stream.secousse.org:8000/secousse-chill',
	   'http://38.107.243.220:8210/',
	   'http://us2.internet-radio.com:8114/live',
	   'http://go.gostreams.com:5195/',
	   'http://www.scratchradio.ca:8000/',
	   'http://192.99.34.205:8458/stream']

btnpurp_choice = random.choice(btnpurp)

print ("Yah Mahn! listening to ", btnpurp_choice)

#subprocess.call(['mpg123', btnpurp_choice])
subprocess.call(['mpg123', '-q', btnpurp_choice, " --preload 1"])


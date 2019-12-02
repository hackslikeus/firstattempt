import os
import sys
import random
import subprocess

btn1234 = ['http://tachyon.shoutca.st:8332/',
	   'http://91.121.165.41:9039/',
	   'http://stream.jammfm.nl:8221',
	   'http://icy.unitedradio.it/101Hipster.mp3',
	   'http://playerservices.streamtheworld.com/api/livestream-redirect/SP_R2591867_SC',
	   'http://198.27.83.198:5006/',
	   'http://www.texfm.ro:8000/rnbhiphop',
	   'http://philae.shoutca.st:8201/stream',
	   'http://streams.radio.co/sb1c077f89/listen',
	   'http://stream.radio.co/s7f7d62626/listen',
	   'http://195.201.129.237:8300/']

btn1234_choice = random.choice(btn1234)

print ("Randomly selected item from list is ", btnpurp_choice)

subprocess.call(['mpg123', btn1234_choice])



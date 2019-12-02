import os
import sys
import random
import subprocess

btn1234 = ['http://us1.internet-radio.com:8653/live',
	   'http://streams.abidingradio.org:7840/1',
	   'http://streams.calmradio.com/api/503/128/stream',
	   'http://streamplus14.leonex.de:15974',
	   'http://107.182.234.82:8060/',
	   'http://cp9.serverse.com:7362/live',
	   'http://199.195.194.140:8375/stream',
	   'http://46.17.5.73:8666/stream',
	   'http://69.162.125.2:8264/',
	   'http://server1.cityedv.at:8099/livestream',
	   'http://ceol.fm:8000/live']

btn1234_choice = random.choice(btn1234)

print ("Randomly selected item from list is ", btnpurp_choice)

subprocess.call(['mpg123', btn1234_choice])



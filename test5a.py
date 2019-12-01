import os
import sys
import random
import subprocess

btnpink = ['http://strm112.1.fm/baroque_mobile_mp3',
	   'http://94.23.201.38:8010/stream',
	   'http://mr-stream.mediaconnect.hu/4742/mr3hq.mp3',
	   'http://uk3.internet-radio.com:8060/stream',
	   'http://5.39.71.159:8978/stream',
	   'http://fluxfm.hoerradar.de/flux-neofm-mp3-hq',
	   'http://mediaserv30.live-streams.nl:8088/',
	   'http://89.16.185.174:8004/stream',
	   'http://atosradio.com:8001/stream/2//',
	   'http://play.organlive.com:7000/320',
	   'http://stream.iradio.fi:8000/klasupro-hi.mp3']

btnpink_choice = random.choice(btnpink)

print ("Randomly selected item from list is ", btnpink_choice)

subprocess.call(['mpg123', btnpink_choice])


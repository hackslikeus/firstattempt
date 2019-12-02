import os
import sys
import random
import subprocess

btnoran = ['http://centreforce.streamgb.com:8830/stream', 
           'http://ice4.somafm.com/bagel-128-mp3', 
           'http://ice4.somafm.com/poptron-128-mp3', 
           'http://sharprouter.sharp-stream.com:8000/nme1high.mp3', 
           'http://sharprouter.sharp-stream.com:8000/nme2high.mp3',
           'http://ice2.somafm.com/u80s-256-mp3', 
           'http://ice2.somafm.com/indiepop-128-mp3',  
           'http://149.56.195.94:8056/stream', 
           'http://media-ice.musicradio.com:80/RadioXLondonMP3']

btnoran_choice = random.choice(btnoran)

print ("And The Winner is:  ", btnoran_choice)

#subprocess.call(['mpg123', '-q', btnoran_choice])
subprocess.call(['mpg123', '-q', btnoran_choice, " --preload 1"])

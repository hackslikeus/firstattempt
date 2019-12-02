import os
import sys
import random
import subprocess

btn1234 = ['http://94.23.201.38:8040/stream',
	   'http://5.39.71.159:8990/stream',
	   'http://212.83.136.31:8000/_c',
	   'http://84.22.99.112:80/gl8media',
	   'http://sc2.1.fm:8030/',
	   'http://eu7.fastcast4u.com/proxy/fwhqdvyte',
	   'http://radioperfecto.net-radio.fr/perfectoblues.mp3',
	   'http://85.25.209.150/blues.mp3',
	   'http://217.116.9.142:9090/TheBluesCove',
	   'http://stream.fatmusicradio.com:8192/fatmusic',
	   'http://edge4.peta.live365.net/b77280_128mp3']

btn1234_choice = random.choice(btn1234)

print ("Randomly selected item from list is ", btnpurp_choice)

subprocess.call(['mpg123', btn1234_choice])



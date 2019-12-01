import os
import sys
import random
import subprocess

btn1234 = ['http://151.80.97.38:8189/stream',
	   'http://fr1.1mix.co.uk:8060/320h',
	   'http://fr1.1mix.co.uk:8060/320',
	   'http://streaming.103radio.fr/320',
	   'http://stream.24dubstep.pl/radio/8000/mp3_best',
	   'http://alles-radio2.stream.laut.fm/alles-radio2?ref=vtuner',
	   'http://195.154.191.116:80',
	   'http://77.168.22.74:8000/stream',
	   'http://HearMe.fm:8013/live',
	   'http://lb.zenfm.be/zenfm.mp3',
	   'http://katzenpuff.stream.laut.fm/katzenpuff?ref=vtuner']

btn1234_choice = random.choice(btn1234)

print ("Randomly selected item from list is ", btn1234_choice)

subprocess.call(['mpg123', btn1234_choice])



import os
import sys
import random
import subprocess

btnblue = ['http://icecast.vrtcdn.be/stubru-high.mp3?origine=1djfkg','http://pr320.pinguinradio.nl:80/','http://rmfstream1.interia.pl/rmf_depeche_mode','http://192.99.34.205:8201/stream']

btnblue_choice = random.choice(btnblue)

print ("Randomly selected item from list is ", btnblue_choice)

subprocess.call(['mpg123', btnblue_choice])


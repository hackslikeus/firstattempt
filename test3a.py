import os
import sys
import random
import subprocess

btnyelo = ['http://stream.srg-ssr.ch/m/rsj/mp3_128?ref=L1St3N','http://media-ice.musicradio.com/SmoothChillMP3','http://54.38.43.201:8006/stream-128kmp3-AbsoluteChillout?AppName=qLty','http://64.150.176.192:8064/','http://streaming.radionomy.com/100-CHILL?AppName=vTuner','http://stream.welleniederrhein.de/444ztgc','http://mediaserv33.live-streams.nl:8036/','http://lb.zenfm.be/zenfm.mp3','http://94.23.201.38:8030/stream','http://stream.absolutradio.de/relax/mp3-160/radioplayer/?AppName=l1vE','http://server1.chilltrax.com:9000/','http://94.23.201.38:8030/stream','http://sl256.hnux.com','http://streamer.hmx.hu/jazzy-groove.mp3']

#to: fix smooth chill url

btnyelo_choice = random.choice(btnyelo)

print ("Randomly selected item from list is ", btnyelo_choice)

subprocess.call(['mpg123', '-q', btnyelo_choice])


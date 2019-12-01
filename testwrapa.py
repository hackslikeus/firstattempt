import os 
import sys
import subprocess
import test1a
import test2a
import test3a
import test4a



#while True:
#        os.system('clear')
print ("")
print ("====================================================================")
print (")                          This is cool")
print ("====================================================================")
print ("")
print ("1 probably rock")
print ("2 jazz")
print ("3 ambient")
print ('4 i forget')
print ("")

nummer = input('what is you choice?: ' )
#       if number =="1":
#       os.system('sudo killall mpg123)
#       subprocess.call([test1a)
if nummer =="1":
        print ("you chose 1 - playing rock")  #os.system('sudo killall mpg123')
        #import test1a.py
	subprocess.call(['test1a.py'])
#subprocess.call([test1a.py])
if nummer =="2":
        os.system('sudo killall mpg123')
        subprocess.call(['test2a']) 
if nummer =="3":
        os.system('sudo killall mpg123')
        subprocess.call(['test3a']) 
if nummer =="4":
        os.system('sudo killall mpg123')
        subprocess.call(['test4a']) 


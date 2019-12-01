import os 
import sys
import subprocess
import time
import random

while True:
 os.system('clear')
 print ("")
 print ("====================================================================")
 print ("                  Magic 8-Ball Internet Radio Stations")
 print ("====================================================================")
 print ("")
 print ("       hit q to stop music - choose 0 to exit ")
 print ("") 
 print ("1 Alternative Rock")
 print ("")
 print ("2 Jazz")
 print ("")
 print ("3 Ambient")
 print ("")
 print ("4 i forget")
 print ("")
 print ("5 Classical")
 print ("")
 print ("6 Reggae")
 print ("")
 print ("7 Big Band")
 print ("")
 print ("8 TBD")
 print ("")
 nummer = input('What is you choice?: ')

 if nummer == 1:
  os.system("python test1a.py")
 if nummer == 2:
  os.system("python test2a.py")
 if nummer == 3:
  os.system("python test3a.py")
 if nummer == 4:
  os.system("python test4a.py")
 if nummer == 5:
  os.system("python test5a.py")
 if nummer == 6: 
  os.system("python test6a.py")
 if nummer == 7:
  os.system("python test7a.py")
 if nummer > 8:
  print ("select a number from above - choose again")
  time.sleep(2) 
 if nummer == 0:
  print ("Adios!")
  time.sleep(2)
  exit()



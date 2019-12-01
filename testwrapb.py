import os 
import sys
import subprocess
import test1a
import test2a
import test3a
import test4a

while True:
 os.system('clear')
 print ("")
 print ("====================================================================")
 print ("                          This is cool")
 print ("====================================================================")
 print ("")
 print ("1 probably rock")
 print ("")
 print ("2 classical")
 print ("")
 print ("3 ambient")
 print ("")
 print ("4 i forget")
 print ("")
 nummer = input('what is you choice: ' )

 if nummer == "1":
  print ("you chose 1 - playing rock")
  subprocess.call('python test1a.py')
 if nummer == "2":
  print ("you chose 2 -playing jazz")
 # os.system('python test2a.py')	  
  subprocess.call('python test2a.py')
 #python test2a.py #subprocess.call(['test2a.py']) 
 if nummer == "3":
  print ("you chose 3- playing ambient")
  #os.system('python test3a.py')
  subprocess.call('python tes3a.py')
 #python test3a.py #subprocess.call(['test3a.py']) 
 if nummer == "4":
  print ("you chose 4- playing something")
  #os.system('python test4a')
  subprocess.call('python test4a.py')
 #python test4a.py #subprocess.call(['test4a.py']) 


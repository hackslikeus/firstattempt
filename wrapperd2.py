import os 
import sys
import subprocess
import time
import random

while True:
 os.system('clear')
 print ("")
 print ("============================================================")
 print ("                 Set Alsamixer to 50%")
 print ("============================================================")
 print ("")
 print ("            hit q or f to stop music once playing ")
 print ("") 

 test = zip()

# print('Music Genre Selection : ', type(test))
 
 list1 = ['1 =_Alt rock', '2 =_Jazz    ', '3 =_Ambient ', '4 =_NotSure ']
 list2 = ['5 =_Classical', '6 =_Reggae   ', '7 =_Big Band ', '0 =_EXIT     ']

 test = zip(list1, list2)  # zip the values

 print('\nProvide a Number from the menu below')
 print("") 
 for values in test:
  print(values)  # print each tuples
 print("==============================================================")
 nummer = int(input('What is you choice?: '))
 if nummer > 8:
  print ("select a number from above - choose again")
  time.sleep(2) 
 elif nummer == 0:
  print ("Adios!")
  time.sleep(2)
  exit()
 elif 1 <= nummer <=8: 
  os.system("python test" + str(nummer) + "a.py")




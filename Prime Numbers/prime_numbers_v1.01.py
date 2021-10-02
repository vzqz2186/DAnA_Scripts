"""
      Program: prime_numbers_v1.00
       Author: Daniel Vazquez
         Date: 01/26/2018
 
    Assignment: (01/24/2018) Find Prime Numbers.
     Due Date: 01/30/2018
  
    Objective: 
 
  Execute via: python prime_numbers_v1.00 123
 
        To Do:
            
 
  ** Template based on Dr. Nichols program example. **
"""
  
#-----------------------------------------------------------------------------80

import time #Used to get current time and the timer for the program
import os
import math

def main():
    counter = 0
    n = int(input(""))

    for i in range(2, n + 1):
        pNum = True
        counter = counter + 1
        for y in range(2, i):
            if i % y == 0:
                pNum = False

        if (pNum == True):
            print(counter, i)
				
    print("Number of calculations: ", counter) 
    #disName()
    disDate()
    #disSysInfo()

# Source:
#    https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-
#    usage-in-python
#def disSysInfo():
    

# Source:
#    https://www.pythoncentral.io/how-to-display-the-date-and-time-using-python/
def disDate():
    print(time.strftime('%m/%d/%Y %H:%M:%S'))

#def disName():
#    print(os.path.splitext()[0])

#Call Main--------------------------------------------------------------------80
main()

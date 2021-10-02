#     Program: prime_numbers_v1.00.py
#      Author: Daniel Vazquez
#        Date: 01/26/2018
#
#   Assinment: (01/24/2018) Find Prime Numbers.
#    Due Date: 01/30/2018
# 
#   Objective: 
#
# Execute via: python prime_numbers_v1.00 123
#
#       To Do:
#           
#
# ** Template based on Dr. Nichols program example. **

#-----------------------------------------------------------------------------80

import time #Used to get current time and the timer for the program
import os
import math

def main():
    counter = 0
    n = int(input(""))
    pNum = 1
    
    if(n == 1):
        print("Not Prime")
    if(n == 2 or n == 3):
        print("Prime")
    if(n > 3):
        for y in range(2,n):
            counter = counter +1
            if n % y == 0:
                pNum = 0
                break
    if (pNum == 1):
        print("Prime \n")
    if (pNum == 0):
        print("Not Prime \n")



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

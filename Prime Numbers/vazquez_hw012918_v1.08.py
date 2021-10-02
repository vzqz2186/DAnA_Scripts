"""
	Program: vazquez_hw012918_v1.08.py
	Author: Daniel Vazquez
	Date: 01/29/2018
 
	Assignment: (01/24/2018) Find Prime Numbers.
	Due Date: 01/29/2018
	
	Objective: Print all prime numbers up to the user input number,n.
	
	Execute via: python prime_numbers_v1.00
	
	Output Sample:
	
		vazquez_hw012918_v1.03

		10
		---------------------------------
		|    i    |  Prime   | Counter  |
		|-------------------------------|
		|       1 |        2 |        9 |
		|       2 |        3 |        9 |
		|       3 |        5 |        9 |
		|       4 |        7 |        9 |
		---------------------------------
		Time:  0.0 ms
		01/29/2018 20:30:21
 
	* Time gets larger with larger n numbers.
	
	Specs of computer where code was programmed:
		CPU: Intel Core i5 6600k @ 3.80 gHz
		RAM: 16 GB
		OS:  Windows 10 Pro

  ** Template based on Dr. Nichols program example. **
"""
  
#----------------------------------------------------------------------------80
import time # Used to get current time and the timer for the program

def main():
	counter = 0
	primes = [] # List that stores all the primes gotten by the program
	numOps = [] # Stores the number of operation per prime
	
	print("\nvazquez_hw012918_v1.03 \n") # Name of the file
	
	n = int(input("")) #Primes are going to be computed up to this number
	i = counter
	
	# Header of the table in the output
	print("---------------------------------")
	print("|    i    |  Prime   | Counter  |")
	print("|-------------------------------|")
	
	start = time.time() # Starts the timer
	"""
	Source for the main loop: https://www.youtube.com/watch?v=r9mqm2dsFk4&t=17s
							  up until minute 6:26. I did not watch the rest of
							  the video.
	"""
	for x in range(2, n + 1):
		pNum = True #Is prime
		counter = counter + 1 # Counts the number of operations
		for y in range(2, x):
			if x % y == 0:
				pNum = False # If it's dividable, it's not prime
				break

#----------------------------------------------------------------------------80
		if (pNum == True):
			numOps.append(counter) # Sends the counter to the counters list
			primes.append(x) # sends the primes to the primes list
							 # source: https://swcarpentry.github.io/python-
							 # novice-inflammation/03-lists/
	end = time.time() # Ends the timer
	Timer = float((end - start) * 1000) # Calculates the time
						# Source:
						# https://programwhiz.wordpress.com/2016/03/10/how-to-
						# create-a-stopwatch-in-python/
						
	i = 0

	"""
	Source for alignment: https://stackoverflow.com/questions/8234445/python-
	format-output-string-right-alignment
	"""
	for row in primes:
		i = i + 1
		print("|{:>8} | {:>8} | {:>8} |" .format(i, row, counter))
	print("---------------------------------")
	"""
	Source for Sig Figs in Timer:
	https://docs.python.org/3/tutorial/floatingpoint.html
	"""
	print("Time: ", format(Timer, ".2f"), "ms")
	disDate()

""" Source:
    https://www.pythoncentral.io/how-to-display-the-date-and-time-using-python/
"""
def disDate():
	print(time.strftime('%m/%d/%Y %H:%M:%S'))

#Call Main--------------------------------------------------------------------80
main()
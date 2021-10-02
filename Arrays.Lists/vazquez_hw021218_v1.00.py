"""
		  Program: Arrays/List
		   Author: Daniel Vazquez
			 Date: 02/10/2018

	   Assignment: Create array/list with 20 possible elements. Fill with 10
				 random integers 1 <= n <= 100. Write a function to insert value
				 in middle of list.

		 Due Date:

		Objective: Write a function to insert value in middle of list.\
				   (WORKS: v1.00)

	  Execute via: >>python vazquez_hw021218_v1.00.py

	Sample output:  vazquez_hw021218_v1.00.py

					lista before insertion:
					 [4, 48, 31, 15, 94, 29, 89, 88, 21, 95]

					Type number to insert to lista: 54

					n = 54

					lista after insertion:
					 [4, 48, 31, 15, 94, '54', 29, 89, 88, 21, 95]

					02/10/2018 10:35

**				Template based on Dr. Nichols program example.				  **
"""
#-----------------------------------------------------------------------------80
import time # Used to get current time and the timer for the program.
import random # Used to fill the list with the 10 random numbers.

def main():
	print("vazquez_hw021218_v1.00.py\n")
	
	"""
	Source for creating the list:
	     https://www.youtube.com/watch?v=G_-ZR-B9STw up until minute 0:50
	 lista means list in Spanish
	"""
	 lista = random.sample(range(1, 100), 10)
	print("lista before insertion: \n",lista,"\n")
	
	n = input("Type number to insert to lista: ")
	print("\nn =",n, "\n")
	
	"""
	 This bit splices the list in two at the middle so n can be inserted into
	 the list without the need of using the .append() tool.
	 Source for splicing idea:
		https://stackoverflow.com/questions/42936941/insert-item-to-list-
		without-insert-or-append-python/42937056
	"""
	lista = lista[:5] + [n] + lista[5:]
	print("lista after insertion: \n", lista,"\n")
	
	disDate() # Prints date


#  Source:
#   https://www.pythoncentral.io/how-to-display-the-date-and-time-using-python/
def disDate():
	print(time.strftime('%m/%d/%Y %H:%M'))

#Call Main--------------------------------------------------------------------80
main()

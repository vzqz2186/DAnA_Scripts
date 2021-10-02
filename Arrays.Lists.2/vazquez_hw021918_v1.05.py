"""
		  Program: List Methods
		   Author: Daniel Vazquez
			 Date: 02/17/2018 (v1.00)
				   02/18/2017 (v1.01, v1.02, v1.03, v1.04, v1.05)

	   Assignment: Create array/list with 20 possible elements. Fill with 10
				   random integers 1 <= n <= 100. Write functions to replicate
				   the methods:
				   1. Length  (WORKS: v1.00)
				   2. Append  (WORKS: v1.00)
				   3. Pop	  (WORKS: v1.02)
				   4. Insert  (WORKS: v1.03)
				   5. Remove  (SOMEWHAT WORKS: v1.04)
				   6. Reverse (WORKS: v1.00)
				   7. Extend  (WORKS: v1.00)
				   8. Sort	  (WORKS: v1.01)

		 Due Date: 2/19/2018

		Objective: Write a function to insert value in middle of list.\
				   (WORKS: v1.00)

	  Execute via: >>python vazquez_hw021918_v1.05.py

	Sample output: 
O.G. List:
 [99, 83, 25, 19, 35, 56, 37, 91, 20, 55]

Length of the list: 10

Element to append:
 [4]
List after append:
 [99, 83, 25, 19, 35, 56, 37, 91, 20, 55, 4]

List after pop:
 [99, 83, 25, 19, 35, 56, 37, 91, 20, 55]

[14] will be inserted at the very middle of the list.
lista after insertion:
 [99, 83, 25, 19, 35, 14, 56, 37, 91, 20, 55]

Element to remove:
4th element in the list: 35
List after remove:
 [99, 83, 25, 19, 56, 37, 91, 20, 55]

List after reverse:
 [55, 20, 91, 37, 56, 19, 25, 83, 99]

List after extension:
 [99, 83, 25, 19, 56, 37, 91, 20, 55, 71, 96, 90, 28, 44, 66, 72, 30, 87, 16]

List after sort:
 [19, 20, 25, 37, 55, 56, 83, 91, 99]

02/18/2018 21:20

** List of methods to replicate: https://linuxconfig.org/python-list-methods **
**				Template based on Dr. Nichols program example.				 **
"""
#----------------------------------------------------------------------------80
import time # Used to get current time and the timer for the program.
import random # Used to fill the list with the 10 random numbers.

def main():
	print("vazquez_hw021918_v1.05.py\n")
	
	# Source for creating the list:
	#    https://www.youtube.com/watch?v=G_-ZR-B9STw up until minute 0:50
	# lista means list in Spanish
	lista = random.sample(range(1, 100), 10) # List is defined and filled with
											 # 10 random integers. 
	print("O.G. List:\n",lista,"\n") # Prints the original list
	
	largo(lista) # Calls the length function.
	adjuntar(lista) # Calls the append function.
	sacar(lista) # Calls the pop function.
	insertar(lista) # Calls the insert function.
	quitar(lista) # Calls the remove function.
	reversa(lista) # Calls the reverse function.
	extender(lista) # Calls the extend function.
	organiza(lista) # Calls the sort function.
	
	disDate() # Prints date

# Date/Time Function---------------------------------------------------------80
#  Source:
#   https://www.pythoncentral.io/how-to-display-the-date-and-time-using-python/
def disDate():
	print(time.strftime('%m/%d/%Y %H:%M'))

# Length function------------------------------------------------------------80
# I personally figured this one out.
def largo(lista):  # largo means "long". Length was too long.
	count = 0 # Count of elements is at 0 if list is empty.
	for x in lista:
		count += 1 # Count increases by 1 for every element in the list.
	print("Length of the list:",count,"\n") # Prints the length of the list.

# Append Function------------------------------------------------------------80
def adjuntar(lista): # adjuntar means "to append".
	n = random.sample(range(1, 100),1) # Number that will be appended.
	# Append just adds an element to the end of the list, so we can just add 
	# the element like this without using .append().
	print("Element to append:\n", n)
	lista += n # Adds the new random element to the list.
	print("List after append:\n",lista,"\n") # Prints new list.

# Pop Function---------------------------------------------------------------80
# Source for deleting the last element of the list:
# https://docs.python.org/3/tutorial/datastructures.html#the-del-statement
def sacar(lista):
	del(lista[-1]) # Eliminates the last element of the list.
	print("List after pop:\n",lista,"\n") # Prints new list.

# Insert Function------------------------------------------------------------80
# Source: Previous homework.
def insertar(lista): # insertar means "to insert".
	n = random.sample(range(1,100),1) # Number that will be inserted.
	print(n, "will be inserted at the very middle of the list.")
	lista = lista[:5] + n + lista[5:]
	print("lista after insertion: \n", lista,"\n")

# Remove Function------------------------------------------------------------80
def quitar(lista): # quitar means "to remove".
	print("Element to remove:\n4th element in the list:", lista[4])
	del(lista[4])
	print("List after remove:\n",lista,"\n") # Prints new list.

# Reverse Function-----------------------------------------------------------80
# Source for the reverse: hw_03_03_Vazquez_v1.00.py from Intro to
# Programming class.
def reversa(lista): # reversa means "reverse".
	lista2 = lista[::-1] # Reverses the elements in list.
	print("List after reverse:\n",lista2,"\n") # Prints new list.
	
# Extend Function------------------------------------------------------------80
# Wondered if the concept used in adjuntar(lista) would work here. It did.
def extender(lista): # extender means "to extend".
	lista2 = random.sample(range(1, 100), 10) # Creates a second list to add
											  # to the main one.
	lista = lista + lista2 # Adds elements of lista2 to lista.
	print("List after extension:\n",lista,"\n") # Prints the new list.

# Sort Function--------------------------------------------------------------80
# Source for function:
# https://stackoverflow.com/questions/11964450/python-order-a-list-of-numbers
# -without-built-in-sort-min-max-function
def organiza(lista): # Organiza means "to organize", which also means to sort.
	lista2 = [] # New copy of lista that will be sorted numerically.
	while lista: # Will loop as long as lista has elements.
		min = lista[0]  # Element that will be used to compare to the other
						# elements.
		for x in lista: # Every element, x, in lista is going to be compared
			if x < min: # with min. If x < min, then it becomes the new
				min = x # min.
				
		lista2.append(min) # min is appended to lista2. 
		lista.remove(min)  # min is removed from lista.

	print("List after sort:\n",lista2,"\n") # Prints new list.
	
# Call Main------------------------------------------------------------------80
main()
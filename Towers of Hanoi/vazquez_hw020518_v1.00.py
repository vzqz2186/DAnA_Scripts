"""
	Program: vazquez_hw020518_v1.00
	Editor: Daniel Vazquez
	Date: 2/4/2018
	Due Date: 2/5/2018

	Objective: Recursive Python function to solve Towers of Hanoi. The
			   purpose of the game is to move the disks from disk 1 to disk 3
			   without setting a larger disk on top of a smaller disk. (WORKS)

Sample Output:  Towers of Hanoi 

				Number of disks:  3 

				How to do it:
				Move disk 1 from rod A to rod C
				Move disk 2 from rod A to rod B
				Move disk 1 from rod C to rod B
				Move disk 3 from rod A to rod C
				Move disk 1 from rod B to rod A
				Move disk 2 from rod B to rod C
				Move disk 1 from rod A to rod C

		To do:  1) Add timer (WORKS: v1.02)
				2) Add counter

**                      Header based on Dr. Nichols's Template               **
**         Main body of the code based on Harshit Agrawal's code on:         **
**        https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/        **
"""
#----------------------------------------------------------------------------80
import time

def main():
	#counter = 0
	print("Towers of Hanoi \n") # Program's name
	n = int(input("")) # Amount of disks to work with.
	print("Number of disks: ",n, "\n\nHow to do it:")
	start = time.time() # Starts timer
	Hanoi(n, 'A', 'C', 'B') # Function call. Rods A, C, B
	end = time.time() # Ends timer
	tiempo = float((end - start) * 1000)
	print("Time: ", format(tiempo, ".2f"), "ms") # Prints timer
	
	
def Hanoi(n, from_rod, to_rod, aux_rod):
	if n == 1:
		print("Move disk 1 from rod",from_rod,"to rod",to_rod)
		print("Counter =", counter)
		# If only one disk, it gets moved from A to C
		return
	Hanoi(n-1, from_rod, aux_rod, to_rod) #
	print ("Move disk",n,"from rod",from_rod,"to rod",to_rod)
	Hanoi(n-1, aux_rod, to_rod, from_rod) #
	
main()
#----------------------------------------------------------------------------80
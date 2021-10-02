"""
          Program: vazquez_maze031918_v1.03.py
           Author: Daniel Vazquez
			 Date: 03/17/2018 (v1.00)
                   03/19/2018 (v1.01)
                   03/20/2018 (v1.02, v1.03)   

       Assignment: Initialize a rectangular maze.

         Due Date: 3/19/2018

        Objective: Create the grid for the maze. Create walls in the maze.
                   ()

      Execute via: >>python vazquez_maze031918_v1.00.py

    Sample output: 


** List of methods to replicate: https://linuxconfig.org/python-list-methods **
**				Template based on Dr. Nichols program example.				 **
"""
#----------------------------------------------------------------------------80
import time # Used to get current time and the timer for the program.

def main():
    og_m = [[0,0,0,1,1], # Original Maze.
            [1,1,0,1,1],
            [1,0,0,1,1],
            [1,0,0,0,0],
            [1,0,0,1,0]]

    r = 5 # Size of the original maze.
    c = 5

    new_m = [] # 2nd array that will be used to house the larger maze.
    new_maze(new_m, r, c) # Function creates the bigger 2D array.

    new_m[0][0] = 0 # Starting node has to be a 0.
    new_m[8][8] = 0 # Finishing node has to be a 0.
    
# Source on how to do the "every other __" for loop:
# https://stackoverflow.com/questions/34708370/replace-every-second-element-in
# -list-with-every-third-in-other-list
    for i in range(0, len(new_m), 2): # For every other list in the list...
        for y in range(len(og_m)):
            for j in range(0, len(new_m[i]), 2): # For every other element...
                for x in range(len(og_m[i])):
                    new_m[i][j] = og_m[y][x]

# Source on how to print the array:
# https://snakify.org/lessons/two_dimensional_lists_arrays/
    for i in range(len(new_m)):
        print(new_m[i]) # Prints the maze.

    disDate() # Prints current date

# Date/Time Function---------------------------------------------------------80
#  Source:
#  https://www.pythoncentral.io/how-to-display-the-date-and-time-using-python/
def disDate():
	print(time.strftime('%m/%d/%Y %H:%M'))

def new_maze(new_m, r, c): # Creates the larger 2D array.
    for x in range(2*r-1): # Fills the array with other arrays.
        new_m.append([])
        for y in range(2*c-1): # Fills the inside arrays with 2s.
            new_m[x].append(2)
    return new_m # Returns the new list to main.

main() # Runs main.
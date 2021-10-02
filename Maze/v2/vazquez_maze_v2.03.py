"""
          Program: vazquez_maze_v2.03.py
           Author: Daniel Vazquez
			 Date: 03/17/2018 (v1.00)
                   03/19/2018 (v1.01)
                   03/20/2018 (v1.02, v1.03)   

       Assignment: Create a rectangular maze.

         Due Date: 

        Objective: Create the grid for the maze. Create walls in the maze.
                   ()

      Execute via: >>python vazquez_maze_v2.03.py

    Algorithm:
        1) Create a rectangular grid where the maze will be generated.
		   a) Create a 2D array full of 2s to generate the grid. 
        2) Fill the grid with 1s and 0s. (1s will be walls and 0s will be open
           paths).
           a) Have a condition for the starting and finishing point to be 0.
           b) Have a condition for both the starting and finishing point to 
              have at least one 0 connected to it.
	       c) Randomly fill with 1s and 0s, making sure that the starting
              point and the finishing point are connected somehow.

    Sample output: 


** List of methods to replicate: https://linuxconfig.org/python-list-methods **
**				Template based on Dr. Nichols program example.				 **
"""
#----------------------------------------------------------------------------80
import time # Used to get current time and the timer for the program.
from random import randint

def main():

    ROW = 5 # Size of the maze maze.
    COL = 5

    maze = [] # 2nd array that will be used to house the maze.
    grid(maze, ROW, COL) # Function creates the array.

    maze[0][0] = 0 # Starting node has to be a 0.
    maze[ROW-1][COL-1] = 0 # Finishing node has to be a 0.

    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 2:
                maze[i][j] = randint(0,1)
#    maze[ROW-1][COL-2] = 3
#    maze[ROW-2][COL-1] = 3
    if(maze[ROW-1][COL-2] and maze[ROW-2][COL-1] == 1):
        maze[ROW-1][COL-2], maze[ROW-2][COL-1] == 0

# Source on how to print the array:
# https://snakify.org/lessons/two_dimensional_lists_arrays/
    for i in range(len(maze)):
        print(maze[i]) # Prints the maze.

    disDate() # Prints current date

# Date/Time Function---------------------------------------------------------80
#  Source:
#  https://www.pythoncentral.io/how-to-display-the-date-and-time-using-python/
def disDate():
	print(time.strftime('%m/%d/%Y %H:%M'))

def grid(maze, ROW, COL): # Creates the 2D array.
    for x in range(ROW): # Fills the array with other arrays.
        maze.append([])
        for y in range(COL): # Fills the inside arrays with 2s.
            maze[x].append(2)
    return maze # Returns the new list to main.

main() # Runs main.
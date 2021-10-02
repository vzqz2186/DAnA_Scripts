"""
          Program: vazquez_maze_v2.03.py
           Author: Daniel Vazquez
			 Date: 03/17/2018 (v1.00)
                   03/19/2018 (v1.01)
                   03/20/2018 (v1.02, v1.03)
                   03/22/2018 (v2.00, v2.01)
                   03/23/2018 (v2.02)
                   03/26/2018 (v2.03)
				   03/29/2018 (v2.04)

       Assignment: Create a rectangular maze.

         Due Date: 

        Objective: Create the grid for the maze. Create walls in the maze.
                   ()

      Execute via: >>python vazquez_maze_v2.03.py

    Algorithm:
        1) Maze Generation
            a) Create a rectangular grid where the maze will be generated.
                I) Initialize a 2D array full of spaces.
            b) Initialize the walls.
			    I) The positioning of the walls will be decided through
                   booleans. If there is a 1 between two vertexes, an 'M' will
                   be placed between the vertexes. If there is a 0, a space
                   will be placed in between instead.
            c) Define the borders as 'M's.
                I) Once walls and paths are initialized and ready, 2 lists
                   full of 'M's will be added to the 2D array. One at the 
                   beginning and one at the end. These will be upper and lower
                   borders.
               II) To 'M's will be added to every list in between those two
                   lists. One will be added at the front, another at the end.
                   These will be the side borders.
        2) Maze Traversing
            a) Start at the top left corner. The end is at the bottom right
               corner.
            b) Use 4 different keys (ex. U for up, D for down, R for right, and
               L for left) to traverse the maze.
                I) The players position will be marked by the plus sign (+).
               II) Once the player chooses moves to a different vertex in the
                   maze, a plus sign will be printed on the players new
                   position.
			  III) If there is already a + sign where the player chooses to go,
                   meaning that the player has already been in that vertex
                   before (i.e. player is moving back), the + sign at the
                   vertex where the player is moving from will be changed for
                   a 0.
			   IV) If there is an 'M' in a vertex, its content cannot be
                   changed for a + or a space. It is a wall.
        3) Displaying the maze
            a) If displayed in the command prompt, cmd screen will be refreshed
               every time the player makes a move to prevent the maze printing
			   again and again flooding the terminal.
			b) If displayed with fancy graphics... TBD.

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
    grid(maze, ROW+2, COL+2) # Function creates the array.

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

def grid(maze, ROW+2, COL+2): # Creates the 2D array.
    for x in range(ROW): # Fills the array with other arrays.
        maze.append([])
        for y in range(COL): # Fills the inside arrays with 2s.
            maze[x].append(' ')
    for y in range(maze[0]):
        maze[0][y] = 'M'
    return maze # Returns the new list to main.

main() # Runs main.
"""
          Program: vazquez_maze_v1.5.py
           Author: Daniel Vazquez
			 Date: 03/17/2018 (v1.00)
                   03/19/2018 (v1.01)
                   03/20/2018 (v1.02, v1.03)   
                   03/01/2018 (v1.05)

       Assignment: Initialize a rectangular maze.

        Objective: Create the grid for the maze. Create walls in the maze.
                   (WORKS v1.5)

      Execute via: >>python vazquez_maze_v1.5.py

        Algorithm:
            1) Maze Generation:
                a) Initial template of the maze is hard coded.
                b) Double the size of the maze to make room for walls and fake
                   paths (bigMaze). (WORKS v1.5)
                    I) 2s are inserted between every element in every list
                       inside maze.
                   II) New lists full with 2s are inserted between every list
                       in maze.
                c) Replace 2s for 1s and 0s (fillMaze). (WORKS v1.5)
                    I) In the lists that were originally in maze, if there is a
                       2 between two 0s, that 2 turns into a 0.
                   II) In the newly inserted lists in maze, if there is are 0s
                       above and below a 2, that 2 becomes a 0.
                  III) Every other 2 randomly becomes either a 0 or a 1.
                
    Sample output: [0, 0, 0, 0, 0, 0, 1, 0, 1]
                   [1, 0, 0, 1, 0, 0, 0, 0, 0]
                   [1, 0, 1, 1, 0, 1, 1, 0, 1]
                   [1, 1, 0, 1, 0, 1, 1, 0, 1]
                   [1, 1, 0, 0, 0, 0, 1, 1, 1]
                   [1, 1, 0, 0, 0, 1, 0, 0, 1]
                   [1, 0, 0, 0, 0, 0, 0, 0, 0]
                   [1, 1, 0, 0, 0, 0, 0, 1, 0]
                   [1, 1, 0, 0, 0, 1, 1, 0, 0]

**				Template based on Dr. Nichols program example.				 **
"""
#----------------------------------------------------------------------------80
import time # Used to get current time and the timer for the program.
from random import randint # Used to fill the grid with 1s and 0s.

def main():
    maze = [[0,0,0,1,1], # Original Maze. (A.1.a)
            [1,1,0,1,1],
            [1,0,0,1,1],
            [1,1,0,0,0],
            [1,0,0,1,0]]

    size = 5 # Size of the original maze.

    bigMaze(maze, size) # Function that will double the size of the maze. (1.b)

    fillMaze(maze) # Function that will fill the maze with 0s and 1s. (1.c)

    # Source on how to print the array:
    #   https://snakify.org/lessons/two_dimensional_lists_arrays/
    for i in range(len(maze)):
        print(maze[i]) # Prints the maze.
	
# Create bigger maze Function------------------------------------------------80
# Source on how to work with every other element:
#   https://stackoverflow.com/questions/31040525/insert-element-in-python-list-
#   after-every-nth-element
def bigMaze(maze, size):                # New lists are placed in between the
    for i in range(len(maze)):          # lists of original maze. (1.b.II)
        maze.insert(i+(i+1), [])
    del maze[-1]

    for i in range(0,len(maze),2):      # 2s are placed in between every
        for j in range(0,len(maze[i])): # element of every list inside maze.
            maze[i].insert(j+(j+1),2)   # (1.b.I)
        del maze[i][-1]
		
    for i in range(1, len(maze), 2):    # Newly placed lists inside maze are
        for j in range(2*size-1):       # filled with 2s. (1.b.II)
            maze[i].append(2)

    return maze
	
# Function to fill the maze with 0s and 1s-----------------------------------80
# Source for randint:
#   https://pythonspot.com/random-numbers/
def fillMaze(maze):
    for i in range(0, len(maze),2):       # 2s in between 0s in the original
        for j in range(1,len(maze[i]),2): # lists in maze are turned into 0s.
            if maze[i][j] == 2:           # (1.c.I)
                if(maze[i][j-1] == 0 and maze[i][j+1] == 0):
                    maze[i][j] = 0
                    
    for i in range(1,len(maze),2):     # 2s in new lists in maze with 0s above
        for j in range(len(maze[i])):  # and below are turned into 0s. (1.c.II)
            if(maze[i-1][j] == 0 and maze[i+1][j] == 0):
                maze[i][j] = 0
                #blockCheck(maze[i][j])

    for i in range(len(maze)):             # Every remaining 2 in maze gets
        for j in range(len(maze[i])):      # randomly turned into a 1 or a 0.
            if(maze[i][j] == 2):           # (1.c.III)
                maze[i][j] = randint(0,1)

    return maze

# Failed attempt to get rid off those blocks of 0s that sometimes form when
# filling up the maze.
"""
def blockCheck(maze):
    
    if(maze[i-1][j] == 0 and maze[i][j-1] == 0 and maze[i-1][j-1] == 0):
        maze[i][j] = 1
    elif(maze[i][j-1] == 0 and maze[i+1][j-1] == 0 and maze[i+1][j] == 0):
        maze[i][j] = 1
    elif(maze[i+1][j] == 0 and maze[i+1][j+1] == 0 and maze[i][j+1] == 0):
        maze[i][j] = 1
    elif(maze[i][j+1] == 0 and maze[i-1][j+1] == 0 and maze[i-1][j] == 0):
        maze[i][j] = 1
"""

# Runs main------------------------------------------------------------------80
main() 
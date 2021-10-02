"""
          Program: vazquez_maze_v3.01.py
           Author: Daniel Vazquez
			 Date: 03/17/2018 (v1.00: DOES NOT WORK)
                   03/19/2018 (v1.01: DOES NOT WORK)
                   03/20/2018 (v1.02, v1.03: DO NOT WORK)
                   03/22/2018 (v2.00, v2.01: DO NOT WORK)
                   03/23/2018 (v2.02: DOES NOT WORK)
                   03/26/2018 (v2.03: DOES NOT WORK)
				   03/29/2018 (v2.04: DOES NOT WORK)
				   04/01/2018 (v2.05: DOES NOT WORK)
                   04/01/2018 (v1.5: WORKS)
                   04/03/2018 (v3.00: WORKS SOMETIMES)
                   04/05/2018 (v3.01: WORKS)
                   04/15/2018 (v3.02: WORKS)

       Assignment: Create a rectangular maze.

        Objective: Create the grid for the maze. (WORKKS: V1.03)
                   Initialize a randomized path inside the grid. (WORKS: v3.01)
                   Create walls and dead ends. (WORKS: v3.02)
                   Allow a player to traverse through the maze. (COMING)
                   Display the maze with fancy graphics. (COMING)

      Execute via: >>python vazquez_maze_v3.02.py

        Algorithm: (latest: v3.02)
            1) Maze Generation
                a) Create a rectangular grid where the maze will be generated.
                b) Generate a randomized path from the starting node
                   (maze[0][0]) to the finishing node (maze[height-1][width-1])
                c) Generate dead ends and outer borders of the maze.
            2) Maze Traversing
                a) The player, represented by *, will start at the beginning
                   node (maze[1][1]) and will use U, D, R, L to move around.
                b) For every node that the player visits, it will get marked
                   with a *.
                c) When the player moves back in the route, the previous
                   location will get marked with a v.
                d) Maze is completed when player reaches
                   maze[height-2][width-2].
            3) Maze Graphics
                a) TBD

    Sample output of a 10 x 10 maze:
                          M M M M M M M M M M M M
                          M     M M             M
                          M       M M   M       M
                          M   M   M     M       M
                          M       M M M         M
                          M M M       M   M M M M
                          M M M   M   M   M M M M
                          M   M     M M M M M   M
                          M M M         M       M
                          M M M           M     M
                          M M     M             M
                          M M M M M M M M M M M M

**              Template based on Dr. Nichols program example.               **
"""
# ---------------------------------------------------------------------------80
# Used to generate the path of the maze.
# Source: 
#   https://docs.python.org/2/library/random.html
from random import randint

def main():

    # These define the size of the maze.
    height = 10
    width = 110

    # Array where the maze will be housed.
    maze = []

    # Creates the rectangular grid full of 2s. (A1.a)
    for i in range(height):
        maze.append([])
        for j in range(width):
            maze[i].append(2)

    # Generates the randomized path. (A1.b)
    generate_path(maze, i, j, height, width)
    # Generates the borders and walls for the maze. (A1.c)
    borders_and_walls(maze, i, j, height, width)
    # Allows a player to traverse the maze. (A2)
    #solving_maze(maze)

    # Source:
    #   Data Structures and Algoithms class (4/4/2018).
    for i in maze:
        for j in i:
            print(j, end = ' ')
        print(" ")

# ---------------------------------------------------------------------------80
# A random number (either 1 or 2) will be drawn in the for of the variable
# "direction". If "direction" is a 1, the loop will move to the node below and
# changing its value to 0. If "direction" is a 2, it will move to the node to
# the right, also changing its value to a 0. The loop will continue until the
# bottom, right node's value is 0.
def generate_path(maze, i, j, height, width):
    
    # Variables to make the loop work and counter initialization.
    x = 0       # Will represent "height".
    y = 0       # Will reppresent "width".
    counter = 0 # It's value will increment with every iteration of the loop.

    # The explanation of how the loop works can be found above the function.
    while(maze[height-1][width-1] != 0):
        maze[x][y] = 0
        direction = randint(1, 2)
        if(direction == 1 and x < height-1):
            if(x == height-1):
                y += 1
                counter += 1
            if(x != height-1):
                x += 1
                counter += 1
        if(direction == 2 and y < width-1):
            if(y == width-1):
                x += 1
                counter += 1
            if(y != width-1):
                y += 1
                counter +=1
        else:
            pass

    # Returns the new values of maze.
    return maze

# ---------------------------------------------------------------------------80
# Generates the borders and walls for the maze. (A1.c)
def borders_and_walls(maze, i, j, height, width):

    # Inserts new lists at the beggining and at the end of the 2D array.
    maze.insert(0, [])
    maze.append([])
    
    # Appends Ms the newly added lists.
    for i in range(width):
        maze[0].append(1)
        maze[-1].append(1)

    # Adds Ms to the beggining and the end of every list in the 2D array.
    for i in range(len(maze)):
        maze[i].insert(0, 1)
        maze[i].append(1)

    # Every remaining 2 in maze gets randomly turned into a 1 or a 0.
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if(maze[i][j] == 2):
                maze[i][j] = randint(0,1)
    
    # Turns 0s into paths (spaces) and 1s into walls (Ms).
    for i in range(len(maze)):             
        for j in range(len(maze[i])):
            if(maze[i][j] == 0):
                maze[i][j] = ' '
            if(maze[i][j] == 1):
                maze[i][j] = 'M'

# ---------------------------------------------------------------------------80
main()
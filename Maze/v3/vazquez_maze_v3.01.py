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

       Assignment: Create a rectangular maze.

        Objective: Create the grid for the maze. (WORKKS: V1.03)
                   Initialize a randomized path inside the grid. (WORKS: v3.01)
                   Allow a player to traverse through the maze. (COMING)
                   Display the maze with fancy graphics. (COMING)

      Execute via: >>python vazquez_maze_v3.01.py

        Algorithm: (latest: v3.01)
            1) Maze Generation
                a) Create a rectangular grid where the maze will be generated.
                b) Generate a randomized path from the starting node
                   (maze[0][0]) to the finishing node (maze[height-1][width-1])
                c) Generate dead ends and outer borders of the maze.
            2) Maze Traversing
                a) TBD
            3) Maze Graphics
                a) TBD

    Sample output: Output from a 10 x 10 maze:
                    M M M M M M M M M M M M M M M M M M M M
                            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
                    2       2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
                    2 2     2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
                    2 2         2 2 2 2 2 2 2 2 2 2 2 2 2 2
                    2 2             2 2 2 2 2 2 2 2 2 2 2 2
                    2 2 2 2     2     2 2 2 2 2 2 2 2 2 2 2
                    2 2 2 2 2     2             2 2 2 2 2 2
                    2 2 2 2 2 2           2 2   2 2 2 2 2 2
                    2 2 2 2 2 2 2 2 2 2   2 2   2 2 2 2 2 2
                    2 2 2 2 2 2 2 2 2 2   2 2     2 2 2 2 2
                    2 2 2 2 2 2 2 2 2 2   2 2 2   2 2 2 2 2
                    2 2 2 2 2 2 2 2 2 2   2 2 2     2 2 2 2
                    2 2 2 2 2 2 2 2 2 2     2 2 2
                    2 2 2 2 2 2 2 2 2 2 2     2 2 2 2 2 2
                    2 2 2 2 2 2 2 2 2 2 2 2   2 2 2 2 2 2
                    2 2 2 2 2 2 2 2 2 2 2 2   2 2 2 2 2 2
                    2 2 2 2 2 2 2 2 2 2 2 2         2 2 2
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2     2 2
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2   2 2
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
                    M M M M M M M M M M M M M M M M M M M M


**              Template based on Dr. Nichols program example.               **
"""
# ---------------------------------------------------------------------------80
# Used to generate the path of the maze.
# Source: 
#   https://docs.python.org/2/library/random.html
from random import randint

def main():

    # These define the size of the maze.
    height = 20
    width = 20

    # Array where the maze will be housed.
    maze = []

    # Creates the rectangular grid full of 2s. (A1.a)
    for i in range(height):
        maze.append([])
        for j in range(width):
            maze[i].append(2)

    # Generates the randomized path. (A1.b)
    generate_path(maze, i, j, height, width)
    # Generates a sacond possible path.
    generate_path_2(maze, i, j, height, width)
    # Generates outer borders.
    borders(maze, i, j, height, width)

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
    while(maze[height-1][width-1] != ' '):
        maze[x][y] = ' '
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
# Creates a second path that the player can follow. Does essencially the same
# as generate_path().
def generate_path_2(maze, i, j, height, width):
    
    # Variables to make the loop work and counter initialization.
    x = 0       # Will represent "height".
    y = 0       # Will reppresent "width".
    counter_2 = 0 # It's value will increment with every iteration of the loop.

    # The explanation of how the loop works can be found above the function.
    while True:
        maze[x][y] = ' '
        direction = randint(1, 2)
        if(direction == 1 and x < height-1):
            if(x == height-1):
                y += 1
                counter_2 += 1
            if(x != height-1):
                x += 1
                counter_2 += 1
            if(x == height-1 and y == width-1):
                break
        if(direction == 2 and y < width-1):
            if(y == width-1):
                x += 1
                counter_2 += 1
            if(y != width-1):
                y += 1
                counter_2 +=1
            if(x == height-1 and y == width-1):
                break
        else:
            pass

    # Returns the new values of maze.
    return maze

# ---------------------------------------------------------------------------80
# Generates the borders for the maze. (A1.d)
def borders(maze, i, j, height, width):

    # Inserts new lists at the beggining and at the end of the 2D array.
    maze.insert(0, [])
    maze.append([])
    
    # Appends Ms the newly added lists.
    for i in range(width):
        maze[0].append('M')
        maze[-1].append('M')

    # Adds Ms to the beggining and the end of every list in the 2D array.
    # (DOES NOT WORK v3.01)
    #for i in maze:
    #    maze[i].insert(0, 'M')
    #    maze[i].append('M')

main()
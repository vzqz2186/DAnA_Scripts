from random import randint

def main():

    height = 5
    width = 5

    grid = []

    for i in range(height):
        grid.append([])
        for j in range(width):
            grid[i].append(2)

    grid[0][0] = 0
    generate(grid, i, j, height, width)

    for i in range(len(grid)):
        print(grid[i])
        
def generate(grid, i, j, height, width):

    x = 0
    y = 0
    counter = 0

    current = grid[i][j]
    
    while(grid[height-1][width-1] != 0):
        grid[x][y] = 0
        direction = randint(1, 2)
        if(direction == 1 and x < height-1):
            if(x == height-1):
                y += 1
            if(x != height-1):
                x += 1
                #counter += 1
        if(direction == 2 and grid[x][y+1] < width-1):
            if(y == width-1):
                x += 1
            if(y != width-1):
                y += 1
            #counter +=1
        else:
            pass
    return grid
    

main()
'''
Mouse in the Maze problem: Giving Maze with the filled 1,0, where 1 - possbile
path to move, 0 - not possible move. Once it is solved it should leave only
path with 1 and rest mark as 0

Mouse can move: forward, down (foward means right from the board perspective)
'''
def printGrid(grid):
    for row in grid:
        print(*row)

def getMoves(row, col, valid_moves):
    for c in valid_moves:
        yield row + c[0], col + c[1]

def isValid(grid, *c):
    return not ((c[0] < 0 or c[0] >= len(grid)) or (c[1] < 0 or c[1] >= len(grid[0])) or not(grid[c[0]][c[1]] == 1))

def getLegalMOves(grid, row, col, valid_moves):
    for c in getMoves(row, col, valid_moves):
        if isValid(grid, *c):
            yield c

def adjustGrid(grid):
    for row in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[row][c] >=0: grid[row][c] = 0
            else: grid[row][c] = 1

def solveMaze(grid, row, col, valid_moves):
    if row == len(grid)-1 and col == len(grid[0])-1: return True

    for c in getLegalMOves(grid, row, col, valid_moves):
        grid[c[0]][c[1]] = -1
        if solveMaze(grid, *c, valid_moves): return True
        grid[c[0]][c[1]] = 0

    return False

# ------------TESTING--------------------
def createMaze(sizeX,sizeY ):
    from random import randint, choice
    moves, grid = [], [[0 for _ in range(sizeX)] for _ in range(sizeY)]

    for row in range(sizeY):
        for col in range(sizeX):
            cell_value = randint(0,1)
            grid[row][col] = cell_value
            if cell_value == 1: moves.append((row, col))
    return grid, choice(moves), choice(moves)

def solveMazeTest(grid, row, col, valid_moves, start, end):
    if start == end: return True
    if row == end[0] and col == end[1]: return True

    for c in getLegalMOves(grid, row, col, valid_moves):
        grid[c[0]][c[1]] = -1
        if solveMazeTest(grid, *c, valid_moves, start, end): return True
        grid[c[0]][c[1]] = 0

    return False

#-----------------END TESTING------------

if __name__=='__main__':
    # ------------MAZE SOLVING WITH RANDOM START, END POINTS AND AUTO MAZE CREATION--------------------
    grid, start, end = createMaze(8, 4)
    printGrid(grid)
    
    # valid_moves = [(1,0), (0,1)]
    valid_moves = [(1,0), (0,1), (-1,0), (0,-1)]

    print(f'start point: {start}, end point: {end}')
    grid[start[0]][start[1]] = -1
    print(f'{"":-^{len(grid) * 2}}')

    if solveMazeTest(grid, start[0], start[1], valid_moves, start, end):
        adjustGrid(grid)
        printGrid(grid)
    else: print('No path solve')

    #-----------------END TESTING----------------------------------------------

    #------------STATIC MAZE SOLVING WITH STARTING POINTS(0,0)-----------------
    # grid = [[1, 0, 0, 0],
    #         [1, 1, 0, 1],
    #         [1, 1, 0, 0],
    #         [0, 1, 1, 1]]
    # printGrid(grid)
    # valid_moves = [(1,0), (0,1)]
    # valid_moves = [(1,0), (0,1), (-1,0), (0,-1)]
    # grid[0][0] = -1
    # print(f'{"":-^{len(grid) * 2}}')
    #
    #
    # if solveMaze(grid, 0, 0, valid_moves):
    #     adjustGrid(grid)
    #     printGrid(grid)
    # else: print('No path solve')
    #-----------------END----------------------------------------------------------------------

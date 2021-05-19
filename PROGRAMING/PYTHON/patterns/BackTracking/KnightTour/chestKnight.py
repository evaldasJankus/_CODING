# https://bradfieldcs.com/algos/graphs/knights-tour/
# https://en.wikipedia.org/wiki/Knight%27s_tour#Warnsdorff.27s_rule
'''
Currently implemented with 'Warnsdorff's rule', which finds solution for board
31x31, when starting point is [0,0]. Bigger board (where n is 32) gives
RecursionError (maximum recursion depth exceeded in comparison)
'''

# Notes for implementation, testing:
# - Can be implemented with 'Neural network solutions'
# - Can be tried to go even depper testing of 'Warnsdorff's rule'
# - Can be implemented with 'Divide-and-conquer algorithms'

def printGrid(grid, n):
    num = len(str(n*n))+1
    for row in grid:
        for col in row:
            print(f'{col:{" "}^{num}}',end='')
        print()

def makeGrid(n):
    return [[-1 for x in range(n)] for _ in range(n)]

def goNext(row, col):
    move_offsets = [(1,2),(-1,2),(2,-1),(2,1),(-1,-2),(1,-2),(-2,1),(-2,-1)]
    for elem in move_offsets:
        yield (row + elem[0]),(col + elem[1])

def isValid(grid, row, col, n):
    return row >= 0 and col >= 0 and row < n and col < n and grid[row][col] == -1

# Rertun all valid moves, after a check if it is valid
def returnValidMoves(grid, row, col, n):
    for r,c in goNext(row, col):
        if isValid(grid, r, c, n):
            yield r,c
    # return [(r,c) for r,c in goNext(row, col) if isValid(grid, r, c, n)]


def returnNextValidMoves(grid, row, col, n):
    getNumOfNextMoves = [(len(list(returnValidMoves(grid, r, c, n))),r,c) for r,c in returnValidMoves(grid, row, col, n)]
    return [(r,c) for _,r,c in sorted(getNumOfNextMoves)]

def gridNotFinished(grid):
    # True if not finished yet
    for row in grid:
        if not (row.count(-1) == 0): return True
    return False

def solveChestTest(grid, row, col, n, counter):
    if counter == n*n: return True

    for c in returnNextValidMoves(grid, row, col, n):  # Warnsdorff’s Rule, grazina galimus ejimus didejo tvarka (Didejimo tvarka nustatoma sekanciu zingsniu skaicius t.y. ima glaima zingsni nuo to zingsnio ziuri kiek jis turi sekanciu zingsniu ir visus sekancius zingsnius is rikiuoja didejimo tvarka)
    # for c in returnValidMoves(grid, row, col, n): # Simple approach
        grid[c[0]][c[1]] = counter
        if solveChestTest(grid, *c, n, counter + 1): return True
        grid[c[0]][c[1]] = -1
    return False

if __name__=='__main__':
    n = 31 # Max 31
    grid = makeGrid(n)
    grid[0][0] = 0

    if solveChestTest(grid, 0, 0, n, 1): printGrid(grid, n)
    else: print('Not solvable')

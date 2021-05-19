#-----------------------DESCRIPTION---------------------------------------------
# The N Queen is the problem of placing N chess queens on an N×N chessboard
#so that no two queens attack each other.
#-------------------------------------------------------------------------------

def createGrid(n=4):
    return [[0 for _ in range(n)] for _ in range(n)]

def printGrid(arr):
    print(f' {"":-^{len(arr)*2-1}}')
    for x in arr: print('',*x)

def isUsedRow(arr, row):
    # Return True if Q already takes the row, False if row is safe
    return 'Q' in arr[row]

def isUsedCol(arr, col):
    # Return True if Q already takes the column, False if column is safe
    for x in arr:
        if x[col] == 'Q': return True
    return False

def isUsedLeftToRightUp(arr, row, col, n):
    # Return True if Q already exists in diagonal LeftToRightUp, False otherwise
    r,c = row+1, col-1
    while r < n and c >= 0:
        if arr[r][c] == 'Q': return True
        r += 1; c -= 1

    r,c = row-1, col+1
    while r >= 0 and c < n:
        if arr[r][c] == 'Q': return True
        r -= 1; c += 1
    return False

def isUsedLeftToRightDown(arr, row, col, n):
    # Return True if Q already exists in diagonal LeftToRightDown, False otherwise
    r,c = row+1, col+1
    while r < n and c < n:
        if arr[r][c] == 'Q': return True
        r += 1; c += 1

    r,c = row-1, col-1
    while r >= 0 and c >= 0:
        if arr[r][c] == 'Q': return True
        r -= 1; c -= 1
    return False

def isSafe(arr, row, col, n=4):
    # If cell is used return False, if cell is not used returns True
    return not (isUsedRow(arr, row) or isUsedCol(arr, col) or isUsedLeftToRightDown(arr, row, col, n) or isUsedLeftToRightUp(arr, row, col, n))

def nQueenSolver(arr, r=0,n=4, q=0):
    if q >= n-1: return True

    for r in range(r,n):
        for c in range(n):
            if isSafe(arr, r, c, n):
                arr[r][c] = 'Q'
                if nQueenSolver(arr, r+1,n, q+1): return True
                else:
                    arr[r][c] = 0

    return False

# Additional function to find all possible solutions,
def findAll(n):
    for x in range(n):
        grid = createGrid(n)
        grid[0][x] = 'Q'
        if nQueenSolver(grid, n=n): printGrid(grid)
        else:
            printGrid(grid)
            print('Problem not solvable')

if __name__=='__main__':
    n = 4
    findAll(n)
    ### TO find only first possible solution uncomment below and comment findeAll()
    # grid = createGrid(n)
    # # printGrid(grid)
    # if nQueenSolver(grid, n=n): printGrid(grid)
    # else: print('Problem not solvable')
    #     # printGrid(grid)

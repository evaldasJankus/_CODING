#--------------------------------SOME CODE STARTS-------------------------------
"""
Sudoku: Fill in full table of the size 9x9. N can be put in place if:
- N is not located in row
- N is not located in column
- N is not located in mini square
"""
def printGrid(board):
    for ind,x in enumerate(board):
        if ind % 3 == 0 and not ind == 0: print(f'{"":-^30}')
        for y in range(0,9,3):
            print('| ' if y == 0 else '', *x[y:y+3], ' | ', end="")
        else: print()

def findEmptySlot(board, row=9, col=9):
    # Returns first empty spot found in the grid
    for x in range(row):
        for y in range(col):
            if board[x][y] == 0: return x, y
    return False

def usedInRow(board, num, row):
    # Returns True if not used, and False if used
    return not num in board[row]

def usedInCol(board, num, col, n=9):
    # Returns True if not used, and False if used
    for x in range(n):
        if board[x][col] == num: return False
    return True

## Shorter Solution for Box checking:
# def used_in_box(arr, row, col, num):
#     for i in range(3):
#         for j in range(3):
#             if(arr[i + row][j + col] == num):
#                 return True
#     return False
# [+]: Where row, col of the box is calcualted: row - row % 3, col - col % 3.

def usedInBox(board, num, row, col, n=9):
    # If not used in Box, returns True, otherwise False
    row_start = 0 if row >=0 and row <= 2 else 3 if row >=3 and row <= 5 else 6
    row_end = 2 if row_start == 0 else 5 if row_start == 3 else 9
    col_start = 0 if col >=0 and col <= 2 else 3 if col >=3 and col <= 5 else 6
    col_end = 2 if col_start == 0 else 5 if col_start == 3 else 9

    temp = []
    for x in board[row_start:row_end+1]:
        temp.append(x[col_start:col_end+1])
    for x in temp:
        if num in x: return False
    return True

def isSafe(board, numb, row, col):
    return usedInBox(board, numb, row, col) and usedInCol(board, numb, col) and usedInRow(board, numb, row)

def solveSudoku(board):
    completed = findEmptySlot(board)
    if not completed: return True
    else:
        row, col = completed[0], completed[1]

    for num in range(1, 10):
        if isSafe(board, num, row, col):
            board[row][col] = num

            if solveSudoku(board): return True
            board[row][col] = 0

    return False

#--------------------------------SOME CODE ENDS---------------------------------

if __name__ == '__main__':
    #-------------------------TEST CASE, TEST CODE------------------------------
    grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0],
             [5, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 7, 0, 0, 0, 0, 3, 1],
             [0, 0, 3, 0, 1, 0, 0, 8, 0],
             [9, 0, 0, 8, 6, 3, 0, 0, 5],
             [0, 5, 0, 0, 9, 0, 6, 0, 0],
             [1, 3, 0, 0, 0, 0, 2, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 7, 4],
             [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

    ## UNSOLVABLE GRID BELOW
    # grid = [ [0, 0, 6, 5, 0, 8, 4, 0, 0],
    #          [5, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 8, 0, 0, 0, 0, 0, 5, 1],
    #          [0, 0, 3, 0, 1, 0, 0, 8, 0],
    #          [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #          [0, 5, 0, 0, 9, 0, 6, 0, 0],
    #          [1, 3, 0, 0, 0, 0, 2, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #          [0, 0, 5, 2, 0, 6, 3, 0, 0] ]
    import time

    star_time = time.time()
    if solveSudoku(grid): printGrid(grid)
    else: print('No Solution exists')
    print('Time took:', time.time() - star_time)

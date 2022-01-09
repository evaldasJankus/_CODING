def load_file(fname):
    with open(fname) as f:
        dots, fold_instructions = [],[]
        for line in f:
            line = line.rstrip()
            if not line: continue
            elif line.startswith('f'):
                line = line.split('=')
                fold_instructions.append((line[0][-1],int(line[1])))
            else:
                line = line.split(',')
                dots.append((int(line[0]),int(line[1])))
    return dots, fold_instructions

def get_max_x(x_dots):
    return max(x_dots)

def get_max_y(y_dots):
    return max(y_dots)

def create_grid(max_x, max_y):
    return [['.' for x in range(max_x+1)] for _ in range(max_y+1)]

def fill_grid(grid, dots):
    for x,y in dots:
        grid[y][x] = '#'

def fold_grid(grid, fold):
    temp_grid_top_left, temp_grid_bottom_right = [],[]
    if fold[0] == 'x':
        temp_grid_top_left = [[row[col] for col in range(fold[1])] for row in grid]
        temp_grid_bottom_right = [[row[col] for col in range(fold[1]+1, len(row))][::-1] for row in grid]
    else:
        temp_grid_top_left = [grid[row] for row in range(fold[1])]
        temp_grid_bottom_right = [grid[row] for row in range(fold[1]+1, len(grid))][::-1]

    for row in range(len(temp_grid_bottom_right)):
        for colum in range(len(temp_grid_bottom_right[0])):
            if temp_grid_top_left[row][colum] == '.' and temp_grid_bottom_right[row][colum] == '#':
                temp_grid_top_left[row][colum] = '#'

    grid = temp_grid_top_left
    return grid

def fold_all_instructions(grid, fold):
    for instruction in fold:
        grid = fold_grid(grid, instruction)
    return grid

def get_number_of_dots(grid):
    return sum([row.count('#') for row in grid])

def main():
    file = 'data'
    dots, fold_instructions = load_file(file)
    max_x, max_y = get_max_x([x[0] for x in dots]), get_max_y([y[1] for y in dots])

    grid = create_grid(max_x, max_y)
    fill_grid(grid, dots)
    # grid = fold_grid(grid, fold_instructions[0]) # To test only one fold
    grid = fold_all_instructions(grid, fold_instructions)
    # print(dots, '\n',fold_instructions) # Just for testing and additional data providing
    print(f'max_x= {max_x}'); print(f'max_y= {max_y}')
    for row in grid: print(row)

    print(f'Number of dots: {get_number_of_dots(grid)}')

if __name__ == '__main__':
    main()

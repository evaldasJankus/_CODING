def load_file(fname):
    with open(fname) as f:
        return [[int(number) for number in line.rstrip()] for line in f]

# --------------- FIRST PART -----------------
def get_valids(matrix, row, column, flashed_coordinates):
    top = (row-1, column)
    right = (row, column+1)
    bottom = (row+1, column)
    left = (row, column-1)
    # ----
    top_left = (row-1, column-1)
    top_right = (row-1, column+1)
    bottom_left = (row+1, column-1)
    bottom_right = (row+1, column+1)
    # ----
    # print(top,right,bottom,left, top_left,top_right,bottom_left,bottom_right)
    valids = [item for item in (top,right,bottom,left, top_left,top_right,bottom_left,bottom_right) if (item[0] >= 0 and item[0] <= len(matrix)-1) and (item[1] >= 0 and item[1] <= len(matrix[0])-1)
    and (not(item in flashed_coordinates))]
    # print(f'valids: {valids}')
    return valids

def is_flashing(matrix, row, column):
    return matrix[row][column] > 9

def update_coordinates(matrix, coordinates, not_valid):
    temp = []
    for coordinate in coordinates:
        if not (coordinate in not_valid):
            matrix[coordinate[0]][coordinate[1]] += 1
            if is_flashing(matrix, coordinate[0], coordinate[1]):
                not_valid.append(coordinate)
                matrix[coordinate[0]][coordinate[1]] = 0
                coordinates_to_update = get_valids(matrix, coordinate[0], coordinate[1], not_valid)
                temp.extend(coordinates_to_update)
    return temp

def get_flashes(matrix):

    flashed_coordinates = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if not ((row, column) in flashed_coordinates):
                matrix[row][column] += 1
                if is_flashing(matrix, row, column):
                    matrix[row][column] = 0
                    flashed_coordinates.append((row, column))
                    # print(flashed_coordinates)
                    coordinates_to_update = get_valids(matrix, row, column, flashed_coordinates)
                    coordinates_to_update = update_coordinates(matrix, coordinates_to_update, flashed_coordinates)
                    while coordinates_to_update:
                        coordinates_to_update = update_coordinates(matrix, coordinates_to_update, flashed_coordinates)
    return len(flashed_coordinates)


def main():
    file = 'data'
    matrix = load_file(file)
    number_repeat = 0
    flash_number = 100

    # -- Visual printing --
    for row in matrix: print(row)
    print('------------')
    #----------------------

    # for _ in range(number_repeat):
    #     flash_number += get_flashes(matrix)

    while not(get_flashes(matrix) == flash_number):
        number_repeat += 1

    # -- Visual printing --
    print('------------')
    for row in matrix: print(row)
    print(f'-------\nTotal flashes: {flash_number} after {number_repeat+1} steps')
    #----------------------


if __name__ == '__main__':
    # FIRST PART: *7*7
    # SECOND PART: *2*
    main()

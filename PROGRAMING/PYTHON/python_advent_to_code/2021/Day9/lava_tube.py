# Low point is when you are reaching the point where no higher number is in adjecendent positions
#
def load_data(fname):
    with open(fname) as f:
        return [[int(numb) for numb in numbers.rstrip()] for numbers in f]

def get_valids(matrix, row, column):
    top = (row-1, column)
    right = (row, column+1)
    bottom = (row+1, column)
    left = (row, column-1)
    valids = [item for item in (top,right,bottom,left) if (item[0] >= 0 and item[0] <= len(matrix)-1) and (item[1] >= 0 and item[1] <= len(matrix[0])-1)]
    # print(f'valids: {valids}')
    return valids

def is_low_point(matrix, row, column, valids):
    for item in valids:
        if matrix[row][column] >= matrix[item[0]][item[1]]: return False
    return True

# --------------- FIRST PART END ------------------------
def get_all_lows(matrix):
    temp, val = [], []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if is_low_point(matrix, row, column, get_valids(matrix, row, column)):
                temp.append(matrix[row][column])
                val.append([row, column])
    return temp, val

def final_answer(numbers):
    return sum([numb + 1 for numb in numbers])
# --------------- FIRST PART END ------------------------
# --------------- SECOND PART START ------------------------
def return_paths(matrix, row, column):
    # returns possible paths to go from given index
    to_go_list = []
    for coordinates in get_valids(matrix, row, column):
        if matrix[coordinates[0]][coordinates[1]] != 9: to_go_list.append(coordinates)
    return to_go_list

def get_bases(matrix, valid_coordinate):
    # searching all bases number from low point coordinate
    base_values = []
    base_values.append(tuple(valid_coordinate))
    search_path_list = return_paths(matrix, valid_coordinate[0], valid_coordinate[1]) # returns valid paths (from 4 possible)
    while len(search_path_list) != 0:
        for coord in search_path_list:
            if coord not in base_values: # if value already exists, that means that coordinate is already visited before
                base_values.append(coord) # not visited, adding to the list of all bases
                search_path_list.remove(coord) # removing from valid paths of search
                new_search_path_list = return_paths(matrix, coord[0], coord[1]) # creating inner search path list from given coordinate
                search_path_list.extend(new_search_path_list) # adding inner search values to a possible paths to go list
            else:
                search_path_list.remove(coord) # path is visited , removing from a list
    return base_values

def find_all_bases(matrix, valid_coordinates):
    return [set(get_bases(matrix, valid_cord)) for valid_cord in valid_coordinates]

def find_three_largest_bases(all_bases):
    return sorted(all_bases, key=len)[-3:]

def get_final_answer_of_three_max_multiplication(bases):
    return len(bases[0]) * len(bases[1]) * len(bases[2])

def print_all_bases(matrix, bases):
    for base in bases:
        print(f'{"":*^10}\nBase length: {len(base)}, coordinates: {base}')
        for cords in base: print(matrix[cords[0]][cords[0]], end=' ')
        print()
# --------------- SECOND PART END ------------------------



def main():
    file = 'data'
    matrix = load_data(file)
    low_points, valid_coordinates_of_low_points = get_all_lows(matrix)
    # print(f'Low points = {low_points}\nValues = {val}\nRisk level = {final_answer(low_points)}')
    all_bases = find_all_bases(matrix, valid_coordinates_of_low_points)
    print(f'Final answer: {get_final_answer_of_three_max_multiplication(find_three_largest_bases(all_bases))}')
    # print_all_bases(matrix, find_three_largest_bases(all_bases))




# 1679 - too big
# Part1 = 539
if __name__ == '__main__':
    main()

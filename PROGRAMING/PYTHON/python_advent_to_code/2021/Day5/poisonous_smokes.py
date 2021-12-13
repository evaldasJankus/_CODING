def load_file(fname):
    with open(fname) as f:
        for line in f:
            line = line.rstrip().split()
            yield tuple(line[0].split(',')), tuple(line[-1].split(','))

def filter_values(coordinates):
    temp_valid, temp_not_valid = [], []
    for item in coordinates:
        if item[0][0] == item[1][0] or item[0][1] == item[1][1]: temp_valid.append(item)
        else:
            temp_not_valid.append(item)
    return temp_valid, temp_not_valid

def make_diagram(coordinates):
    max_x = [(item[0][0], item[1][0]) for item in coordinates]
    max_x = max([val for item in max_x for val in item])
    max_y = [(item[0][1], item[1][1]) for item in coordinates]
    max_y = max([val for item in max_y for val in item])
    # print(max_x, max_y)
    return [[0 for x in range(int(max_x) + 1)] for y in range(int(max_y)+1)]

#----------------PART1----------------------
def fill_diagram(coordinates, diagram):

    for cord in coordinates:
        x1, x2, y1, y2 = int(cord[0][0]), int(cord[1][0]), int(cord[0][1]), int(cord[1][1])
        if x1 == x2:
            for y in range(min(y1,y2), min(y1,y2) + abs(y1-y2)+1):
                diagram[y][x1] += 1
        else:
            for x in range(min(x1,x2), min(x1,x2) + abs(x1-x2)+1):
                diagram[y1][x] += 1
    return diagram
#-------------END OF PART1----------------------
#-------------FILLING DIAGONAL COORDINATES PART2
def fill_diagram_part2(coordinates):
    dict_of_coordinates = {}
    for cord in coordinates:
        x1, x2, y1, y2 = int(cord[0][0]), int(cord[1][0]), int(cord[0][1]), int(cord[1][1])
        if x1 < x2:
            if y1 < y2:
                x = x1
                for y in range(y1, y2 +1):
                    dict_of_coordinates[f'{x1},{y1}:{x2},{y2}'] = dict_of_coordinates.get(f'{x1},{y1}:{x2},{y2}', []) + [[x,y]]
                    x += 1
            else:
                x = x1
                for y in range(y2, y1 +1)[::-1]:
                    dict_of_coordinates[f'{x1},{y1}:{x2},{y2}'] = dict_of_coordinates.get(f'{x1},{y1}:{x2},{y2}', []) + [[x,y]]
                    x += 1
        else:
            if y1 < y2:
                x = x1
                for y in range(y1, y2 +1):
                    dict_of_coordinates[f'{x1},{y1}:{x2},{y2}'] = dict_of_coordinates.get(f'{x1},{y1}:{x2},{y2}', []) + [[x,y]]
                    x -= 1
            else:
                x = x1
                for y in range(y2, y1 +1)[::-1]:
                    dict_of_coordinates[f'{x1},{y1}:{x2},{y2}'] = dict_of_coordinates.get(f'{x1},{y1}:{x2},{y2}', []) + [[x,y]]
                    x -= 1
    return dict_of_coordinates

def fill_diagram_with_diagonal(dict_list, diagram):
    for item in dict_list:
        for cord in dict_list[item]:
            diagram[cord[1]][cord[0]] += 1
    return diagram
#-------------FILLING DIAGONAL COORDINATES PART2

def overlaping_lines(diagram):
    return sum([1 for item in diagram for val in item if val >= 2])

def main():
    file = 'data'
    coordinates = list(load_file(file))
    # print(f'COORDINATES: {coordinates}')
    coordinates, not_valid_coordinates = filter_values(coordinates)
    # print(F'VALID COORDINATES: {coordinates}')
    diagram = make_diagram(coordinates)
    # print(diagram)
    diagram = fill_diagram(coordinates, diagram)
    print(F'NOT VALID COORDINATES: {not_valid_coordinates}')
    list_of_coordinates = fill_diagram_part2(not_valid_coordinates)
    diagram = fill_diagram_with_diagonal(list_of_coordinates, diagram)
    # for x in diagram: print(x)
    print(overlaping_lines(diagram))
    # print(list_of_coordinates)


if __name__ == '__main__':
    main()

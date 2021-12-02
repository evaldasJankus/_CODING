def load_file(fname):
    with open(fname) as f:
        for line in f: yield line.rstrip().split()

def get_data(fname):
    return tuple((key, int(val)) for key, val in load_file(fname))

#------PART1------------------
def get_final_score_part1(directions):
    horizontal_and_depth = {'horizontal':0, 'depth':0}
    for key, val in directions:
        if key == 'forward': horizontal_and_depth['horizontal'] += val
        elif key == 'down': horizontal_and_depth['depth'] += val
        else: horizontal_and_depth['depth'] -= val
    return horizontal_and_depth, horizontal_and_depth['horizontal'] * horizontal_and_depth['depth']

#------PART2------------------
def get_final_score_part2(directions):
    horizontal_and_depth = {'horizontal':0, 'depth':0, 'aim':0}
    for key, val in directions:
        if key == 'forward':
            horizontal_and_depth['horizontal'] += val
            horizontal_and_depth['depth'] += horizontal_and_depth['aim'] * val
        elif key == 'down': horizontal_and_depth['aim'] += val
        else: horizontal_and_depth['aim'] -= val
    return horizontal_and_depth, horizontal_and_depth['horizontal'] * horizontal_and_depth['depth']


def main():
    directions = get_data('data')
    print(get_final_score_part2(directions))

if __name__ == '__main__':
    main()

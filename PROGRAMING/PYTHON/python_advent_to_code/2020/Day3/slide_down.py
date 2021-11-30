def read_file(fname):
    with open(fname) as f:
        return [line.rstrip() for line in f]

def is_valid(entry, col):
    return True if entry[col] == '.' else False

def filter_data(fname):
    col_step = [1,3,5,7,1]
    row_step = [1,1,1,1,2]

    counter = 0
    col = 0

    for entry in read_file(fname)[::2]:
        if is_valid(entry * ((col // len(entry))+1), col):
            col += 1
        else:
            counter += 1
            col += 1
    return counter

def main():
    print('Number of trees encounter: ', filter_data('slide_data'))

if __name__ == '__main__':
    main()

# 61 (1,1)
# 257 (3,1)
# 64 (5,1)
# 47 (7,1)
# 37 (1,2)

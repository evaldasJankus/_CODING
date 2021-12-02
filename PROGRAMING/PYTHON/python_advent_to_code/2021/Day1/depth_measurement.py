# Part 1: Find some of adjacent numbers which are increased. Increased numbers are:
# - If current number is bigger than his adjacent(previous number/ one number higher) number
# 109 - First number not comparable
# 117 - Increased
# 118 - Increased
# - First number in data is never increased because it has no previous number
#
# Part 2: Find the number of sums of 3 adjacent numbers.
# - Sum consists of 3 numbers going one after another
# - First sum of 3 numbers, never increased because it does not have a sum of previous numbers
# 109 - a
# 117 - a b
# 118 - a b c d
# 98 - b c d e
# 102 - c e
# 94 -e
# 101 -
# 109 -
# 121 -

def load_file(fname):
    with open(fname) as f:
        for line in f: yield int(line.rstrip())

def find_increased(fname):
    depths = list(load_file(fname))
    # counter = 0
    # for x in range(1,len(depths)):
        # if depths[x] > depths[x-1]: counter += 1
    return sum([1 for x in range(1, len(depths)) if depths[x] > depths[x-1]])

def find_increased_of_sums(fname):
    def find_sums_of_groups(depths):
        return [depths[x] + depths[x+1] + depths[x+2] for x in range(len(depths)-2)]

    depths = find_sums_of_groups(list(load_file(fname)))
    return sum([1 for x in range(1, len(depths)) if depths[x] > depths[x-1]])


def main():
    print(find_increased_of_sums('data'))

# 1448 - First part of the question
# 1471 - Second part of the question

if __name__ == '__main__':
    main()

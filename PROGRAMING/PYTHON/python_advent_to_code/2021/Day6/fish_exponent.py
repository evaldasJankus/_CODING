def load_file(fname):
    with open(fname) as f:
        for fishes in f:
            for fish in fishes.rstrip().split(','):
                yield int(fish)

#---------------PART1-----------------
def fish_exponent_part1(fish_list, days):
    new_fish, old_fish = 8, 6
    for day in range(days):
        for item in range(len(fish_list)):
            if not fish_list[item]:
                fish_list[item] = old_fish
                fish_list.append(new_fish)
            else:
                fish_list[item] -= 1
    return len(fish_list), fish_list

#---------------END PART1-----------------
#---------------PART2---------------------
def load_file_part2(fname):
    with open(fname) as f:
        return f.readline().rstrip()

def fish_exponent_part2(fish_list, days):
    dict_fish = {k:0 for k in range(9)}
    for item in fish_list:
        dict_fish[item] = dict_fish.get(item, 0) + 1

    for x in range(days):
        temp = dict_fish[0]
        dict_fish[0] = dict_fish[1]
        dict_fish[1] = dict_fish[2]
        dict_fish[2] = dict_fish[3]
        dict_fish[3] = dict_fish[4]
        dict_fish[4] = dict_fish[5]
        dict_fish[5] = dict_fish[6]
        dict_fish[6] = dict_fish[7] + temp
        dict_fish[7] = dict_fish[8]
        dict_fish[8] = temp

    return dict_fish, sum([dict_fish[k] for k in dict_fish])

#---------------END PART2-----------------


def main():

    file, days = 'data', 256
    initial_fishes = list(load_file(file))
    print(f'Fishes after {days}: {fish_exponent_part2(initial_fishes, days)}')

if __name__ == '__main__':
    main()

def load_file(fname):
    with open(fname) as f:
        for line in f:
            yield line.rstrip()

def filter_data(fname):
    temp,filtered_list = '', []
    for line in load_file(fname):
        if not line:
            filtered_list.append((set(temp), len(set(temp))))
            temp = ''; continue
        temp += line
    else:
        filtered_list.append((set(temp), len(set(temp))))
    return filtered_list

def filter_data2(fname):
    temp, filtered_list = [],[]
    for line in load_file(fname):
        if not line:
            filtered_list.append(temp)
            temp = []; continue
        temp.append(set(line))
    else:
        filtered_list.append(temp)
    return filtered_list

def get_intersect_list(groups):
    groups_index = []
    for group in groups:
        if len(group) == 1:
            groups_index.append((group[0],len(group[0])))
            continue
        intersect = group[0].intersection(*group[1:])
        groups_index.append((intersect, len(intersect)))
    return groups_index

def sum_of_groups(groups):
    return sum([group[1] for group in groups])

def main():
    # print(sum_of_groups(filter_data('data')))
    # print(get_intersect_list(filter_data2('data')))
    # print(filter_data2('data'))
    print(sum_of_groups(get_intersect_list(filter_data2('data'))))

if __name__ == '__main__':
    main()

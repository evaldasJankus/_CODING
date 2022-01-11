from collections import Counter

def laod_file(fname):
    with open(fname) as f:
        polymer_template = f.readline().rstrip()
        f.readline()
        pair_insertion = {line.rstrip().split(' -> ')[0]:line.rstrip().split(' -> ')[1] for line in f}
        return polymer_template, pair_insertion

def get_pairs(template):
    # return {template[idx:idx+2] for idx in range(len(template)-1)}
    occur = {}
    for i in range(len(template)-1):
        s = template[i] + template[i+1]
        if s in occur:
            occur[s] += 1
        else:
            occur[s] = 1
    return occur

def get_new_template(pair_insertion, pairs):
    # s = ''
    # for idx in range(len(current_template)-1):
    #     s += current_template[idx] + pair_insertion[current_template[idx:idx+2]]
    # else:
    #     s += current_template[-1]
    # return ''.join([current_template[idx] + pair_insertion[current_template[idx:idx+2]] for idx in range(len(current_template)-1)]) + current_template[-1]
    #
    # FOr second part used this solved code[did nto understand the meaning of the task it self]: https://github.com/SaiMonYo/2021-Advent-Of-Code/blob/main/Day14.py
    temp = {}
    for key, value in pairs.items():
        # CH -> CB BC
        f = key[0] + pair_insertion[key]
        l = pair_insertion[key] + key[1]
        # adding to the temp dictionary
        if f in temp:
            temp[f] += value
        else:
            temp[f] = value
        if l in temp:
            temp[l] += value
        else:
            temp[l] = value

    return temp

def get_max_template(current_template):
    return max([current_template.count(ch) for ch in set(current_template)])

def get_min_template(current_template):
    return min([current_template.count(ch) for ch in set(current_template)])

def main():
    file = 'data'
    polymer_template, pair_insertion = laod_file(file)
    # print(polymer_template,'\n',pair_insertion)
    pairs = get_pairs(polymer_template)
    # print(f'Pairs for insertion: {pairs}')
    print(polymer_template)
    print('*',pairs)
    for _ in range(40):
        pairs = get_new_template(pair_insertion, pairs)
        # print(pairs)
    count = Counter()
    print(count)
    for key in pairs:
        count[key[0]] += pairs[key]
    count[polymer_template[-1]] += 1
    print(count)
    print(max(count.values())); print(min(count.values()))
    print(f'result {max(count.values()) - min(count.values())}')
    3849876073
    485345134

if __name__ == '__main__':
    main()

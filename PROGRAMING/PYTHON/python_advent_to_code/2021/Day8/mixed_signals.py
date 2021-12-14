def load_file_part1(fname):
    with open(fname) as f:
        for line in f:
            yield line.rstrip().split('|')[-1]

def get_unique_number_part1(data_list):
    numbers = {0:'acfgeb', 1:'cf', 2:'acdge', 3:'acdfg', 4:'cdfb', 5:'adfgb', 6:'adfgeb', 7:'acf', 8:'acdfgeb', 9:'acdfgb'}
    uniques_num = {1:'cf', 4:'cdfb', 7:'acf', 8:'acdfgeb'}
    counter = 0
    for val in data_list.split():
        for item in uniques_num:
            if len(val) == len(uniques_num[item]):
                counter += 1
                break
    return counter

def find_all_unique_numbers_part1(number_list):
    return sum([get_unique_number(numbers) for numbers in number_list])

#-----PART 2 ----
def load_file_part2(fname):
    with open(fname) as f:
        for line in f:
            yield line.rstrip().split('|')

# <- Left, right ->
# 1 = len(2), {right side top, right side bottom}
# 2 = len(5), {top, right side top, middle, left side bottom, bottom}
# 3 = len(5), {top, right side top, middle, right side bottom, bottom}
# 4 = len(4), {left side top, middle, right side top, right side bottom}
# 5 = len(5), {top, top side left, middle, right side bottom, bottom}
# 6 = len(6), {top, left side top, middle, right side bottom, bottom, left side bottom}
# 7 = len(3), {top, right side top, right side bottom}
# 8 = len(7), {top, right side top, right side bottom, bottom, left side bottom, middle, left side top}
# 9 = len(6), {top, right side top, middle, right side bottom, left side top}
# 0 = len(6), {top, right side top, right side bottom, bottom, left sdie bottom, left side top}
# ------
# 1 = len(2), 4 = len(4), 7 = len(3), 8 = len(7)
# 2 = len(5)(2 parts of 4), 3 = len(5)(if all 1 parts in), 5 = len(5)(else 5)
# 6 = len(6)(if all 5 number parts and one 1 number part), 9 = len(6)(all 5 parrts and all 1 parts), 0 = len(6)(else 0)

def find_pattern(data_list):
    dict_numbers = {}
    for number in data_list.split():
        if len(number) == 2: dict_numbers[1] = number
        elif len(number) == 4: dict_numbers[4] = number
        elif len(number) == 3: dict_numbers[7] = number
        elif len(number) == 7: dict_numbers[8] = number

    for number in data_list.split():
        if len(number) == 5:
            # print('number: ', number)
            if sum([number.count(letter) for letter in dict_numbers[1]]) == 2:
                dict_numbers[3] = number
            elif sum([number.count(letter) for letter in dict_numbers[4]]) == 2:
                dict_numbers[2] = number
            else:
                dict_numbers[5] = number

    for number in data_list.split():
        if len(number) == 6:
            if sum([number.count(letter) for letter in dict_numbers[5]]) == 5 and  sum([number.count(letter) for letter in dict_numbers[1]]) == 2:
                dict_numbers[9] = number
            elif sum([number.count(letter) for letter in dict_numbers[1]]) == 2 and sum([number.count(letter) for letter in dict_numbers[5]]) == 4:
                dict_numbers[0] = number
            else:
                dict_numbers[6] = number

    return dict_numbers

def get_signal_numbers(pattern, signal_numbers):
    temp = ''
    for number in signal_numbers:
        for k,v in pattern.items():
            if ''.join(sorted(number)) == ''.join(sorted(v)):
                temp += str(k)
                break
    return int(temp)


def main():
    file = 'data'
    numbers_list = list(load_file_part2(file))
    print(sum([get_signal_numbers(find_pattern(item[0]), item[-1].split()) for item in numbers_list]))

    # print(find_all_unique_numbers(numbers_list))

if __name__ == '__main__':
    main()

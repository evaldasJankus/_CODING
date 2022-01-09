def load_file(fname):
    with open(fname) as f:
        for line in f:
            yield line.rstrip()

# PART1
def filter_results_part1(fname):
    # Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers
    # The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001
    gamma_rate, epsilon_rate = '',''
    data_loaded = list(load_file(fname))
    for x in range(len(data_loaded[0])):
        temp = [item[x] for item in data_loaded]
        gamma_rate += '1' if temp.count('1') > temp.count('0') else '0'
    else:
        epsilon_rate = ''.join(['0' if int(item) else '1' for item in gamma_rate])
    print(f'gamma_rate: {gamma_rate} - epsilon_rate: {epsilon_rate}')
    print(f'gamma_rate: {int(gamma_rate, base=2)} - epsilon_rate: {int(epsilon_rate, base=2)}')
    print(f'Power consumption: {int(gamma_rate, base=2) * int(epsilon_rate, base=2)}')

# PART2
def filter_results_part2(fname):
    # Find life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.
    # life_support_rating = 0
    data_loaded = list(load_file(fname))
    oxygen_generator_rating, co2_scrubber_rating = data_loaded[:], data_loaded[:]

    for x in range(len(data_loaded[0])):

        # print(temp)
        if len(oxygen_generator_rating) > 1:
            temp = [item[x] for item in oxygen_generator_rating]
            oxygen_generator_rating = [item for item in oxygen_generator_rating if int(item[x])] if temp.count('1') >= temp.count('0') else [item for item in oxygen_generator_rating if not int(item[x])]
            # print(temp.count('1'),',', temp.count('0'), '=>', oxygen_generator_rating)
        if len(co2_scrubber_rating) > 1:
            temp = [item[x] for item in co2_scrubber_rating]
            co2_scrubber_rating = [item for item in co2_scrubber_rating if int(item[x])] if temp.count('1') < temp.count('0') else [item for item in co2_scrubber_rating if not int(item[x])]
            # print(temp.count('1'),',', temp.count('0'), '=>', co2_scrubber_rating)

    life_support_rating = int(oxygen_generator_rating[0], base=2) * int(co2_scrubber_rating[0], base=2)
    print(f'oxygen_generator_rating: {oxygen_generator_rating}, co2_scrubber_rating: {co2_scrubber_rating}')
    print(f'oxygen_generator_rating: {int(oxygen_generator_rating[0], base=2)}, co2_scrubber_rating: {int(co2_scrubber_rating[0], base=2)}')
    print(f'life_support_rating = {life_support_rating}')

def main():
    file = 'data_example'
    # filter_results_part1(file)
    filter_results_part2(file)


if __name__ == '__main__':
    main()

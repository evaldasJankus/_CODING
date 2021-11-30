def read_file(fname):
    with open(fname) as f:
        for line in f:
            yield line.split()

def if_valid(entry):
    # one star
    occurrence = entry[-1].count(entry[1].replace(':',''))
    nrange = entry[0].split('-')
    return occurrence >= int(nrange[0]) and occurrence <= int(nrange[1])

def if_valid_two_stars(entry):
    # two star
    password = ' ' + entry[-1]
    nrange = entry[0].split('-')
    low, high = int(nrange[0]),int(nrange[1])
    letter = entry[1].replace(':','')
    return password[low] == letter and password[high] != letter or password[low] != letter and password[high] == letter

def filter_data(fname):
    count = 0
    for entry in read_file(fname):
        if if_valid_two_stars(entry): count += 1
        else: print(entry, False)
        # break
    return count

def main():
    # data = read_file('passwords_policy')
    print(filter_data('passwords_policy'))
    # print(data)

if __name__ == '__main__':
    main()
    # ''.replace()

def read_from_file(fname):
    with open(fname) as f:
        return [int(line) for line in f]

def find_second_pair(n, n_list):
    for num in n_list:
        req_num = n - num
        if req_num in n_list:
            # print(num, req_num)
            return num, req_num
    return 0,0


def find_pair(num_list):
    for k, num in enumerate(num_list):
        req_num = 2020 - num
        pair = find_second_pair(req_num, num_list[k+1:])
        if isinstance(get_results(pair), int): return num, pair[0] * pair[1]
        # if req_num in num_list: return num, req_num
    return 0,0
    # return pairs

def get_results(pair):
    if pair[0] or pair[1]: return pair[0] * pair[1]
    return 'No results'

def main():
    number_list = read_from_file('input_data')
    print(type(number_list))
    print(number_list)
    pairs = find_pair(number_list)
    print(pairs, end='\n*****\n')
    print(get_results(pairs))

if __name__=="__main__":
    main()

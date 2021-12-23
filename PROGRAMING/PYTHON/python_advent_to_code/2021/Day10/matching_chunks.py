def load_file(fname):
    with open(fname) as f:
        for line in f:
            yield line.rstrip()

def is_chunk_corrupted(chunk):
    left_side, right_side = '({[<', ')}]>'
    dict_points = {')':3, ']': 57, '}':1197, '>': 25137}
    temp_chunks = []
    counter = 0
    # while True:
    for index in range(len(chunk)):
        if chunk[index] in left_side:
            temp_chunks.append(chunk[index])
            # counter +=1
        else:
            if right_side.find(chunk[index]) == left_side.find(temp_chunks[-1]):
                temp_chunks.pop()
            else:
                return False, dict_points[chunk[index]]
                # return f'False, expected {temp_chunks[-1]}, but got {chunk[index]}: {chunk}'
    return True, None
    # return 'Line is good'

def return_falty_lines_of_chunk(chunks):
    suma = 0
    for chunk in chunks:
        is_corrupted, symbol = is_chunk_corrupted(chunk)
        if not is_corrupted: suma += symbol
    return suma
# ------------- FIRST PART END ------------
# ------------- SECOND PART START ---------
def is_chunk_corrupted_part2(chunk):
    left_side, right_side = '({[<', ')}]>'
    dict_endings = {'(':')', '[': ']', '{': '}', '<': '>'}
    temp_chunks = []
    counter = 0
    for index in range(len(chunk)):
        if chunk[index] in left_side:
            temp_chunks.append(chunk[index])
        else:
            if right_side.find(chunk[index]) == left_side.find(temp_chunks[-1]):
                temp_chunks.pop()
            else:
                return False, None # False means that it is corrupted
    # print(f'Is not corrupted, left to close: {temp_chunks}')
    return True, ''.join([dict_endings[ch] for ch in temp_chunks[::-1]]) # True means that it is not corrupted

def return_not_falty_lines_of_chunk(chunks):
    chunk_endings = []
    for chunk in chunks:
        is_corrupted, endings = is_chunk_corrupted_part2(chunk)
        if is_corrupted:
            chunk_endings.append(endings)
            # print(f'{chunk}: needs to finish "{endings}"')
    return chunk_endings

def get_total_scores_of_lines(chunk_endings):
    dict_points = {')':1, ']': 2, '}':3, '>': 4}
    total_scores_list = []
    for chunk in chunk_endings:
        suma  = 0
        for ch in chunk:
            suma = suma * 5 + dict_points[ch]
        else:
            total_scores_list.append(suma)
            # print(f'Suma: {suma}')
    # print(sorted(total_scores_list), len(total_scores_list) // 2)
    return sorted(total_scores_list)

def find_middle_score(total_scores):
    return total_scores[(len(total_scores) // 2)]
# ------------- SECOND PART START ---------


def main():
    file_name = 'data'
    all_chunks = list(load_file(file_name))
    print(find_middle_score(get_total_scores_of_lines(return_not_falty_lines_of_chunk(all_chunks))))
    # print(f'Total syntax error score: {return_falty_lines_of_chunk(all_chunks)}')
    # for chunk in all_chunks: print(is_chunk_corrupted(chunk))

if __name__ == '__main__':
    main()

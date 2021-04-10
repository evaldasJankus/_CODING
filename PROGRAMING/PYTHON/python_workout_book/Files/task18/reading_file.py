"""
NOTE: there is a solution: StringIO (http://mng.bz/PAOP). StringIO objects are
what Python calls “file-like objects.” They implement the same API as file objects,
allowing us to read from them and write to them just like files. Unlike files, though,
StringIO objects never actually touch the filesystem.
"""

def read_file_last_line(filename='data_text'):
    """
    * Task to print last line of the file
    """
    # Method 1 (Seeking end file is the way to go, faster solution)
    with open(filename,'rb+') as f:
        f.seek(-2,2)
        s = f.read(1)
        ch = s
        while True:
            f.seek(-2,1)
            ch = f.read(1)
            if ch == b'\n': break
            s += ch
        print(str(s[::-1],'utf-8'))

    # Method 2 (readlines()[-1]) return last element of readline, but with ling files it is goign to be slow
    # Method (offered in the book, simply iterate through lines and print the last one)

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Iterate over the lines of a text file. Find all of the words (i.e., non-whitespace
surrounded by whitespace) that contain only integers, and sum them.
"""
def find_all_numbers(filename='data_text'):
    with open(filename) as f:
        numb = 0
        for line in f:
            numb += sum([int(word) for word in line.split() if word.isdigit()])
    return numb

"""
 Create a text file (using an editor, not necessarily Python) containing two tabseparated columns, with each column containing a number. Then use Python
to read through the file you’ve created. For each line, multiply each first number by the second, and then sum the results
"""
def sum_numbers_from_file(filename='number_table'):
    total = 0
    with open(filename) as f:
        for line in f:
            line = line.replace('\n','').split(',')
            if len(line) < 2: continue
            if all(map(str.isdigit, line[:2])):
                print(f'{line[0]} * {line[1]} => { (int(line[0])*int(line[1])) }')
                total += int(line[0]) * int(line[1])
    print(f'TOTAL: {total}')

"""
 Read through a text file, line by line. Use a dict to keep track of how many times
each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation.
"""
def vowel_counter(filename='data_text'):
    # Method 1
    from collections import Counter
    vowels_dict = {'a': 0, 'e':0, 'i':0, 'o':0, 'u':0}
    with open(filename) as f:
        for line in f:
            c = Counter(line)
            for key in vowels_dict:
                vowels_dict[key] += c.get(key,0)
    return vowels_dict

    # Method 2: simply iterate through each caracter and check if it meets a, if ye add to dict
    # vowels_dict = {'a': 0, 'e':0, 'i':0, 'o':0, 'u':0}
    # with open(filename) as f:
    #     ch = ' '
    #     while ch :
    #         ch =  f.read(1)
    #         if not (ch in vowels_dict): continue
    #         vowels_dict[ch] += 1
    # return vowels_dict

if __name__ == '__main__':
    # read_file_last_line()
    # print(find_all_numbers())
    # sum_numbers_from_file()
    print(vowel_counter())

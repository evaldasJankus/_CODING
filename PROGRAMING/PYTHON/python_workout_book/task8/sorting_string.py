def str_sort(word):
    return ''.join(sorted(word))

    # word_list = [ch for ch in word]
    # for x in range(len(word_list)-1):
    #     for y in range(x,len(word_list)):
    #         if word_list[y] < word_list[x]:
    #             word_list[y], word_list[x] = word_list[x], word_list[y]
    # return ''.join(word_list)

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Which is the longest word in a text file?
"""
def longest_word_file(filename):
    longest_word = ''
    with open(filename,'r') as f:
        for line in f:
            temp = ''
            for ch in line:
                if ch.isalnum() or ch ==' ': temp += ch
            longest = sorted(temp.split(), key=len)[-1]
            print(longest, len(longest), end=' ')
            if len(longest_word) <  len(longest): longest_word = longest
    print()
    return longest_word, len(longest_word)

"""
 Which is the last word, alphabetically, in a text file?
"""
def last_word_file(filename):
    last_word = ''
    with open(filename,'r') as f:
        for line in f:
            temp = ''
            for ch in line:
                if ch.isalnum() or ch ==' ': temp += ch
            last = sorted(temp.split())[-1]
            if last_word <  last: last_word = last
    return last_word

"""
Given the string “Tom Dick Harry,” break it into individual words, and then sort
those words alphabetically. Once they’re sorted, print them with commas (,)
between the names
"""
def str_list_sort(word_list):
    return ','.join(sorted(word_list.split()))


if __name__=='__main__':
    print(last_word_file('data'))
    print(longest_word_file('data'))
    # st = 'baca'
    # print(st,'=>',str_sort(st))
    # word_list = 'evaldas Evaldas mindaugas Aiste aiste labas'
    # print(word_list + '\n' + str_list_sort(word_list))

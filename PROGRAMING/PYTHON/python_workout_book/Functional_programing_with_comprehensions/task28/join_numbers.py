
#-------------------------MAIN TASK--------------------------------------------
"""
For this exercise, write a function (join_numbers) that takes a range of integers.
The function should return those numbers as a string, with commas between the
numbers. That is, given range(15) as input, the function should return this string:
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
"""
def join_numbers(numb):
    # List comprehention
    # return ','.join([str(n) for n in range(numb)])

    # Generator
    return ','.join(str(n) for n in range(numb))

#-------------------------BEYOND THE TASK--------------------------------------
"""
 As in the exercise, take a list of integers and turn them into strings. However,
you’ll only want to produce strings for integers between 0 and 10. Doing this
will require understanding the if statement in list comprehensions as well.
"""
def integers_to_strings(*args):
    return [str(x) if x >= 0 and x <= 10 else x for x in args]

"""
 Given a list of strings containing hexadecimal numbers, sum the numbers
together.
"""
def hex_to_base_10_sum(hex_list):
    return sum(int(n, base=16) for n in hex_list)

"""
Use a list comprehension to reverse the word order of lines in a text file. That
is, if the first line is abc def and the second line is ghi jkl, then you should
return the list ['def abc', 'jkl ghi'].
"""
def reverse_lines(filename='data'):
    result = []
    with open(filename) as f:
        result = [' '.join(line.rstrip().split()[::-1]) for line in f]
    return result


if __name__ == '__main__':
    print(reverse_lines())
    # print(hex_to_base_10_sum([hex(2),hex(10), hex(-1), hex(15)]))
    # print(integers_to_strings(*[47,1,2,10,15,7,888]))
    # print(join_numbers(7))

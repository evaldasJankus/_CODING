'''
For this exercise, you need to write a function (hex_output) that takes a hex
number and returns the decimal equivalent.
'''
def any_base_to_decimal(num, base):
    hexnum = str(num)
    decimal = 0
    if hexnum == '0': return 0

    while  hexnum:
        digit = hexnum[0]
        hexnum = hexnum[1:]
        if digit.isalpha():
            decimal += ((ord(digit) - ord('a')) * base**len(hexnum))+10
        else:
            decimal += int(digit) * base**len(hexnum)

    return decimal

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Write a program that asks the user for their name and then produces a “name
triangle”: the first letter of their name, then the first two letters, then the first
three, and so forth, until the entire name is written on the final line. 
"""
def print_triangle(name):
    for x in range(1,len(name)):
        print(f'{name[:x]:^{len(name)*2}}')

if __name__ == '__main__':
    # print(any_base_to_decimal('101', 2))
    print_triangle('evaldas')

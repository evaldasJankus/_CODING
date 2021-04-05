import operator, functools
#-------------------------MAIN TASK--------------------------------------------
"""
Create a fucntion named calc, which expects single input in string in tha math
expression prefix '+ 2 3'. Shoudl support 6 operations '+/*-%**'. Should not use
if statement. 6 Different functions. and oprator module
"""
# operator +
def suma(a,b): return a + b
# operator -
def minus(a,b): return a - b
# operator **
def raisem(a,b): return a ** b
# operator /
def devide(a,b): return a / b
# operator %
def modnum(a,b): return a % b
# operator *
def multiple(a,b): return a * b
def calc(prefix_string):
    operator_dict = {'+':operator.add , '-':operator.sub, '**':operator.pow,
                     '/':operator.truediv, '%': operator.mod, '*':operator.mul}
    op, num1,num2 = prefix_string.split()
    return operator_dict[op](int(num1),int(num2))

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Expand the program you wrote, such that the user’s input can contain any
number of numbers, not just two. The program will thus handle + 3 5 7 or / 100
5 5, and will apply the operator from left to right—giving the answers 15 and 4,
respectively.
"""
def calc_extend(prefix_string):
    operator_dict = {'+':operator.add , '-':operator.sub, '**':operator.pow,
                     '/':operator.truediv, '%': operator.mod, '*':operator.mul}
    op, *nums = prefix_string.split()
    nums = [int(n) for n in nums]

    # Use of built-in function
    # return functools.reduce(operator_dict[op],nums)

    # Custom reduce fucntion to handle no input for numbers
    def myreduce(func, numbers):
        if not numbers: return 0
        elif len(numbers) == 1: return numbers[0]
        else:
            it = iter(numbers)
            result = next(it) #func(numbers[0],numbers[1])
            for elem in it:
                result = func(result,elem)
        return result
    return myreduce(operator_dict[op],nums)

"""
 Write a function, apply_to_each, that takes two arguments: a function that takes
a single argument, and an iterable. Return a list whose values are the result of
applying the function to each element in the iterable. (If this sounds familiar, it
might be—this is an implementation of the classic map function, still available in
Python. You can find a description of map in chapter 7.)
"""
def apply_to_each(func, m_iterable):
    return [func(elem) for elem in m_iterable]

"""
 Write a function, transform_lines, that takes three arguments: a function that
takes a single argument, the name of an input file, and the name of an output
file. Calling the function will run the function on each line of the input file,
with the results written to the output file. (Hint: the previous exercise and this
one are closely related.)
"""
def transform_lines(func, filein, fileout):
    with open(filein) as f_reader, open(fileout,'w') as f_writer:
        for line in f_reader: f_writer.write(func(line))


if __name__ == '__main__':
    # print(calc('** 1 2'))
    # print(calc_extend('/ 100 5 5'))
    # print(apply_to_each(lambda x: x*2,[1,2,3,4,5]))
    transform_lines(lambda x: x.replace('m','1'), 'data', 'result_output')

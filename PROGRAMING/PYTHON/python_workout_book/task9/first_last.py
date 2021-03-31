def max_element(object):
    return max(object)

def numbers_square(numb):
    return numb**2

def first_last(object):
    return object[:1] + object[-1:]

def max_word(streamo):
    if isinstance(streamo,io.StringIO):
        content = streamo.getvalue()

    else:
        content = streamo.read()

    return max(content.replace('\n',' ').split())
    
#-------------------------BEYOND THE TASK--------------------------------------
"""
* Write a function that takes a list or tuple of numbers. Return a two-element list,
containing (respectively) the sum of the even-indexed numbers and the sum of
the odd-indexed numbers. So calling the function as even_odd_sums([10, 20,
30, 40, 50, 60]), you’ll get back [90, 120].
"""
def even_odd(iter):
    return [sum(iter[::2]), sum(iter[1::2])]

"""
* Write a function that takes a list or tuple of numbers. Return the result of
alternately adding and subtracting numbers from each other. So calling the function
as plus_minus([10, 20, 30, 40, 50, 60]), you’ll get back the result of
10+20-30+40-50+60, or 50.
"""
def plus_minus(iter):
    string_result = f'{iter[0]}'
    number_sum = iter[0]
    for indx in range(1,len(iter)):
        if not (indx % 2):
            string_result += f'-{iter[indx]}'
            number_sum -= iter[indx]
        else:
            string_result += f'+{iter[indx]}'
            number_sum += iter[indx]
    return string_result, number_sum

"""
* Write a function that partly emulates the built-in zip function (http://mng.bz/
Jyzv), taking any number of iterables and returning a list of tuples. Each tuple
will contain one element from each of the iterables passed to the function.
Thus, if I call myzip([10, 20,30], 'abc'), the result will be [(10, 'a'), (20,
'b'), (30, 'c')]. You can return a list (not an iterator) and can assume that all
of the iterables are of the same length.
"""
def myzip(iterable):
    #Method 1
    new_iter = [[(elem[x]) for elem in iterable] for x in range(len(iterable[0]))]
    return [tuple(elem) for elem in new_iter]

if __name__=='__main__':
    print(f'{"Main exercise":-^40}')
    print(first_last([1,2,'a','b']))
    print(first_last('abcd'))
    print(first_last((2,3,6,-5)))
    print(f'{"Extra first exercise":-^40}')
    print('2 =>',numbers_square(2))
    print('2.2 =>',numbers_square(2.2))
    print(f'{"Extra second exercise":-^40}')
    print(max_element([1,2,3,5,4]))
    print(max_element('abcd'))
    print(max_element((2,3,6,-5)))
    print(f'{"Extra third exercise":-^40}')
    import io
    output = io.StringIO()
    output.write('first line of the first input\n')
    output.write('second line xof the second input\n')
    print('IO =>', max_word(output))
    print('file[data] =>',max_word(open('data','r')))
    print(f'{"Extra slicing First exercise":-^40}')
    print('[sum_EVENS, sum_ODDS] =>',even_odd([1,2,3,4,5,6,7,8,9,10]))
    print(f'{"Extra slicing Second exercise":-^40}')
    print('[string_RESULT, number_RESULT] =>',plus_minus([1,2,3,4,5,6,7,8,9,10]))
    print(f'{"Extra slicing Third exercise":-^40}')
    print('MY_ZIP =>',myzip([[1,2,3],'abc']))

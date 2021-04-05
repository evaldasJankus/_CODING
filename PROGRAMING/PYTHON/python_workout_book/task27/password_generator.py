import random, string, operator

#-------------------------MAIN TASK--------------------------------------------
def create_password_generator(options):
    def generate_password(length_of_password):
        return ''.join([random.choice(options) for _ in range(length_of_password)])
    return generate_password

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Now that you’ve written a function to create passwords, write create_password_checker,
which checks that a given password meets the IT staff’s acceptability criteria. In other
words, create a function with four parameters: min_uppercase, min_lowercase,
min_punctuation, and min_digits. These represent the minimum number of uppercase letters,
lowercase letters, punctuations, and digits for an acceptable password. The output from
create_password_checker is a function that takes a potential password (string) as its
input and returns a Boolean value indicating whether the string is an acceptable password.
"""
def create_password_checker(min_uppercase=0, min_lowercase=0, min_punctuation=0, min_digits=0):
    def is_valid(password_string):
        valid_dict = {'min_up':0,'min_low':0, 'min_dig':0, 'min_pun':0}

        for ch in password_string:
            if ch.isalpha() and ch.islower(): valid_dict['min_low'] += 1
            elif ch.isalpha() and ch.isupper(): valid_dict['min_up'] += 1
            elif ch.isdigit(): valid_dict['min_dig'] += 1
            elif ch in string.punctuation: valid_dict['min_pun'] += 1
        return valid_dict['min_low'] >= min_lowercase and valid_dict['min_up'] >= min_uppercase and valid_dict['min_dig'] >= min_digits and valid_dict['min_pun'] >= min_punctuation
    return is_valid

"""
 Write a function, getitem, that takes a single argument and returns a function
f. The returned f can then be invoked on any data structure whose elements
can be selected via square brackets, and then returns that item. So if I invoke
f = getitem('a'), and if I have a dict d = {'a':1, 'b':2}, then f(d) will return
1. (This is very similar to operator.itemgetter, a very useful function in many
circumstances.)
"""
def get_item(item):
    def funct(iter): return iter[item]  #operator.itemgetter(item)(iter)
    return funct

"""
 Write a function, doboth, that takes two functions as arguments (f1 and f2) and
returns a single function, g. Invoking g(x) should return the same result as
invoking f2(f1(x)).
"""
def func_do_both(func1, func2):
    def func_g(x): return func2(func1(x))
    return func_g


if __name__ == '__main__':
    # BEYOND TASK3
    f1 = lambda x: x.rstrip('\nabc'); f2 = lambda x: x.lstrip(' 156')
    strip_string_from_sides = func_do_both(f1,f2)
    print(strip_string_from_sides(' 15555.My String.\nccbba'))
    print(f2(f1(' 15555.My String.\nccbba')))

    #BEYOND TASK 2
    # f = get_item(1)
    # print(f('asd'))

    # BEYOND TASK 1
    # pass_requirements1 = create_password_checker()
    # pass_requirements2 = create_password_checker(2,4,1,2)
    # pass_requirements3 = create_password_checker(min_lowercase=4,min_punctuation=1,min_digits=3)
    #
    # print(pass_requirements1('123456ab')); print(pass_requirements2('a.s1u234D56Gl'))
    # print(pass_requirements3('as1@23hj456'))
    # MAIN TASK -----------------------
    # alpha_password = create_password_generator('asdfghhj')
    # symbol_password = create_password_generator('/*?.><@#')
    # print(alpha_password(12))
    # print(symbol_password(5))

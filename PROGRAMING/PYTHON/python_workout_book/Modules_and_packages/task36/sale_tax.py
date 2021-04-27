## IMPORTS
from decimal import Decimal
## GLOBALS
HOURS = [n for n in range(24)]
PROVINCE = {'Chico':50,'Groucho':70,'Harpo':50,'Zeppo':40}

#-------------------------MAIN TASK--------------------------------------------
"""
Fucntion takes 3 arguments: pa - purchase amount, p - province, h - hour(0-24).
To calculcate taxes: Chico: 50%, Groucho: 70%, Harpo: 50%, Zeppo: 40%
Taxes applied accoridng the time. The tax percentage is always multiplied by the
hour at which the purchase was made.
Example: 0 - no taxes, 12-13 only 50%(12/24), 23-24 95.8%(23/24)
"""
class HoursError(Exception): pass
class HourToolowError(HoursError): pass
class HourTooHighError(HoursError): pass


def time_percentage(p,h): return ((PROVINCE[p]*(h/24))/100)

def calculate_tax(pm, p, h):
    try:
        if h < 0: raise HourToolowError(f'Hour can not be below 0, you entered {h}')
        if h > 24: raise HourTooHighError(f'Hour can not be higher than 24, you entered {h}')
    except HoursError as e:
        print(e)
    else:
        return round(pm + pm*time_percentage(p,h),2)

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Income tax in many countries is not a flat percentage, but rather the combination
of different “brackets.” So a country might not tax you on your first $1,000
of income, and then 10% on the next $10,000, and then 20% on the next
$10,000, and then 50% on anything above that. Write a function that takes
someone’s income and returns the amount of tax they will have to pay, totaling
the percentages from various brackets.
"""
class IncomeTooLow(Exception): pass

INCOME = [Decimal('0.0'),Decimal('0.1'),Decimal('0.2'),Decimal('0.5')]
def calculate_income(i):
    # i - income
    # try:
    if i < 0: raise IncomeTooLow('Income can not be negative')
    # except IncomeTooLow as e:
    #     print(e, end=' ')
    # else:
    index = 0 if i <= 1000 else 1 if i <= 10000 else 2 if i <= 20000 else 3
    return float(i*INCOME[index])

"""
 Write a module providing a function that, given a string, returns a dict indicating
how many characters provide a True result to each of the following functions:
str.isdigit, str.isalpha, and str.isspace. The keys should be isdigit,
isalpha, and isspace.
"""
def calculcate_char(s):
    string_list = [str.isdigit, str.isalpha, str.isspace]
    string_dict = {'isdigit':([],0),'isalpha':([],0),'isspace':([],0)}
    # for ch in s:
    for f in string_list:
        string_dict[f.__name__] = (list(filter(f,s)),string_dict[f.__name__][1]+list(map(f,s)).count(True))
    return string_dict

"""
 The dict.fromkeys method (http://mng.bz/1zrV) makes it easy to create a
new dict. For example, dict.fromkeys('abc') will create the dict {'a':None,
'b':None, 'c':None}. You can also pass a value that will be assigned to each
key, as in dict.fromkeys('abc', 5), resulting in the dict {'a':5, 'b':5,
'c':5}. Implement a function that does the same thing as dict.keys but whose
second argument is a function. The value associated with the key will be the
result of invoking f(key).
"""
def create_dict(keys, f):
    return {k:f(k) for k in keys}


if __name__ == '__main__':
    # print(calculcate_char('Mano12.3 sd'))
    print(create_dict('abs', lambda x: ord(x)))

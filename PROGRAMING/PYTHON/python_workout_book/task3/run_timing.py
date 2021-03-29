"""
Write a function (run_timing) that asks how long it took for you to run 10 km.
The function continues to ask how long (in minutes) it took for additional runs, until
the user presses Enter. At that point, the function exits—but only after calculating and
displaying the average time that the 10 km runs took.
"""
def run_timing():
    avg, counter = 0, 0
    choice = 1
    while choice:
        choice = input('Enter 10km running time in minutes: ')
        if choice == '': continue
        avg += float(choice)
        counter += 1
    else:
        print(f'Average of {(avg/counter):.2f}, over {counter} runs.')
#-------------------------BEYOND THE TASK--------------------------------------
"""
 Write a function that takes a float and two integers (before and after). The
function should return a float consisting of before digits before the decimal
point and after digits after. Thus, if we call the function with 1234.5678, 2 and
3, the return value should be 34.567.
"""
def beforeAfter(flo, before, after):
    # Takes float number and two numbers: before - number of digits before dot from right to left
    # after - number after dot, left to right
    numstring = str(flo).split('.')
    numstring = numstring[0][-before:] + '.' + numstring[1][:after]
    return float(numstring)

"""
 Explore the Decimal class (http://mng.bz/oPVr), which has an alternative
floating-point representation that’s as accurate as any decimal number can be.
Write a function that takes two strings from the user, turns them into decimal
instances, and then prints the floating-point sum of the user’s two inputs. In
other words, make it possible for the user to enter 0.1 and 0.2, and for us to get
0.3 back.
"""
def sum_decimal():
    # Decimal module is used to get more precise results.
    import decimal

    decimal.getcontext().prec = 2
    num1 = decimal.Decimal(input('Enter first number: '))
    num2 = decimal.Decimal(input('Enter second number: '))

    print(num1 + num2)
    print(0.1 + 0.2)


if __name__=='__main__':
    # run_timing()
    # print(beforeAfter(123456.12345,2,3))
    sum_decimal()

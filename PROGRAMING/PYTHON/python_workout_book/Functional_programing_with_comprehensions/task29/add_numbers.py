
#-------------------------MAIN TASK--------------------------------------------
"""
Function takes input from user and returns all valid digits sum. INput seperate
with space
"""
def sum_numbers():
    numbers = input('Enter list of numbers: ').rstrip().split()
    return sum(int(n) for n in numbers if n.isdigit())


#-------------------------BEYOND THE TASK--------------------------------------
"""
 Show the lines of a text file that contain at least one vowel and contain more
than 20 characters
"""
def show_lines(filename='data'):
    results = []
    with open(filename) as fr:
        filtered_lines = filter(lambda x: len(x) > 20,(line for line in fr))
        # results = [for line in filter_lines]
        for line in filtered_lines:
            for ch in line:
                if ch.lower() in 'aeiuo':
                    print(line.rstrip())
                    break

"""
Change area code if middle number begins with digits 0-5. format of number
XXX-YYY-ZZZZ. Use List comprehention
"""
def change_area(areas):
    areas = [area.split('-') for area in areas]
    new_areas = ['-'.join([str(int(area[n])+1) if not n else area[n] for n in range(len(area))]) if area[1][0] in '012345' else '-'.join(area) for area in areas]
    return new_areas

"""
Define a list of five dicts. Each dict will have two key-value pairs, name and age,
containing a person’s name and age (in years). Use a list comprehension to
produce a list of dicts in which each dict contains three key-value pairs: the original name, the original age, and a third age_in_months key, containing the person’s age in months. However, the output should exclude any of the input dicts
representing people over 20 years of age.
"""
def person_age(person_list):
    new_list = [{**d,**{'age_in_months':d['age']*12}} for d in person_list]
    return list(filter(lambda x: x["age"]>20 , new_list))


if __name__ == '__main__':

    print(person_age([{'name':'al','age':12},{'name':'le','age':22},{'name':'ev','age':32},{'name':'ais','age':30},{'name':'rg','age':17}]))
    # print(change_area(['123-456-7890', '123-333-4444', '123-777-8888']))
    # show_lines()

    # print(sum_numbers())

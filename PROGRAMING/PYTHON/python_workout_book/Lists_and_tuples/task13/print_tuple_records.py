PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

MOVIES = [('Movie1', 120,'Some Author'),
          ('Novie1', 139,'Fome Author'),
          ('Xovie1', 111,'Vome Author'),
          ('Xyvie1', 111,'Some Author'),
            ]

def format_sort_record(iter):
    # import operator
    # sorted(iter, key=operator.itemgetter(1,0))
    s = ''
    for elem in sorted(iter, key=lambda x: (x[1],x[0])):
        s += f'{elem[1]:<10} {elem[0]:<10} {elem[-1]:>5.2f}\n'
    return s
    # alternatively can be one liner
    # return '\n'.join([f'{elem[1]:<10} {elem[0]:<10} {elem[-1]:>5.2f}' for elem in iter])

#-------------------------BEYOND THE TASK--------------------------------------
def format_sort_record_using_namedtuple(iter):
    """
     If you find tuples annoying because they use numeric indexes, you’re not alone!
    Reimplement this exercise using namedtuple objects (http://mng.bz/gyWl),
    defined in the collections module. Many people like to use named tuples
    because they give the right balance between readability and efficiency"""
    import collections
    s = ''
    person = collections.namedtuple('person',('firstname','lastname','hours'))
    persons = [person(p[0],p[1],p[-1]) for p in iter]
    for elem in sorted(persons, key=lambda x: (x.lastname,x.firstname)):
        s += f'{elem.lastname:<10} {elem.firstname:<10} {elem.hours:>5.2f}\n'
    return s

def list_of_movies_oscar(iter):
    """
     Define a list of tuples, in which each tuple contains the name, length (in minutes), and director of the movies nominated for best picture Oscar awards last
    year. Ask the user whether they want to sort the list by title, length, or director’s
    name, and then present the list sorted by the user’s choice of axis.
     Extend this exercise by allowing the user to sort by two or three of these fields,
    not just one of them. The user can specify the fields by entering them separated
    by commas; you can use str.split to turn them into a list."""

    import collections
    options = ('title','length','director')
    movie = collections.namedtuple('movie',options)
    movies = [movie(m[0],m[1],m[-1]) for m in iter]
    print(movies)
    choice = input(f'Please chose by which column to sort: {options}: ').split(',')
    if all(map(lambda x: x.lower() in options,choice)):
        from operator import itemgetter
        s = ''
        # print(options.index(choice.lower()))
        for elem in sorted(movies, key=itemgetter(*[options.index(x.lower()) for x in choice])): # lambda x: x[options.index(choice.lower())]
            # print(elem)
            s += f'{elem.title:<10} {elem.length:>5} {elem.director:^10}\n'
        return s
    return 'WRONG CHOICE'

if __name__ == '__main__':
    # print(format_sort_record(PEOPLE))
    # print(format_sort_record_using_namedtuple(PEOPLE))
    print(list_of_movies_oscar(MOVIES))

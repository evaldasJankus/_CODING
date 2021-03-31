def password_to_dict(filename='data_file'):
    """
    From etc/password extract users and user unique ID. (users are in 0 columns),
    unique ID is in 3 columns  (column 2). Ignore lines which are not valid
    """
    users_dict = {}
    with open(filename) as file:
        for line in file:
            if line.startswith(('#', '_','\n')): continue
            line = line.replace('\n','').split(':')
            users_dict[line[0]] = line[2]
    return users_dict

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Read through /etc/passwd, creating a dict in which user login shells (the final
field on each line) are the keys. Each value will be a list of the users for whom
that shell is defined as their login shell.
"""
def users_shels(filename='data_file'):
    users_shels_dict = {}
    with open(filename) as file:
        for line in file:
            if line.startswith(('#', '\n')): continue
            line = line.replace('\n','').split(':')
            users_shels_dict[line[-1]] = list(users_shels_dict.get(line[-1], [])) + [line[0]]
    for shel,users in users_shels_dict.items(): print(shel,':',users)


"""
 Ask the user to enter integers, separated by spaces. From this input, create a
dict whose keys are the factors for each number, and the values are lists containing those of the users’ integers that are multiples of those factors.
"""
def read_numbers_input():
    numbers = input('Eenter integer numbers separated by spaces: ').split()
    numbers = [int(number) for number in numbers if number.isdigit()]
    def get_factors_of_number(numb):
        return {x for x in range(1,numb+1) if not numb % x}
    dict_keys = list(map(get_factors_of_number, numbers))
    set_keys = set()
    for num in dict_keys: set_keys.update(num)
    dict_keys = {key:[ key*val for val in numbers] for key in set_keys}
    print(dict_keys)

"""
 From /etc/passwd, create a dict in which the keys are the usernames (as in the
main exercise) and the values are themselves dicts with keys (and appropriate
values) for user ID, home directory, and shell.
"""
def passwd_dict(filename='data_file'):
    new_dict, inner_dict = {}, {}
    with open(filename) as file:
        for line in file:
            if line.startswith(('#','_','\n')): continue
            line = line.replace('\n','').split(':')
            # print(line)
            new_dict[line[0]] = {'User ID':line[2],'home directory':line[8], 'shell':line[-1]}
    return new_dict


if __name__ == '__main__':
    # print(password_to_dict())
    # users_shels()
    # read_numbers_input()
    print(passwd_dict())

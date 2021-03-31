MENU = {'barsciai':1.8,'kepti kiausiniai':2,'virti kiausiniai':1.2,'salotos':3.90,'pica':4.90,'kebabas':4}
USERS = {'user1':'password1','user2':'password2', 'user3':'password3'}


def restaurant():
    total = 0
    choice = '-1'
    while choice:
        choice = input(f'Choose from menu ({"|".join(MENU.keys())}):').lower().strip()
        if not choice: continue
        item = MENU.get(choice, 0)
        if item:
            total += item
            print(f'{choice.capitalize()} cost {item}, total amount is {total}')
        else:
            print(f'{choice.upper()} is not in the MENU. Try again')
    else:
        print(f'Total ammount is {total}')
        
#-------------------------BEYOND THE TASK--------------------------------------
"""
 Create a dict in which the keys are usernames and the values are passwords,
both represented as strings. Create a tiny login system, in which the user must
enter a username and password. If there is a match, then indicate that the user
has successfully logged in. If not, then refuse them entry. (Note: This is a nice
little exercise, but please never store unencrypted passwords. It’s a major security risk.)
"""
def login_check():
    choice = 1
    while choice:
        username = input('Enter your login: ')
        if not username.strip():
            choice = 0
            continue
        password = input('Enter your password: ')
        item = USERS.get(username, 0)
        if item == password:
            print('Welcome aboard!')
            choice = 0
            continue
        else:
            print('Entered username and/or password is in correct! Trye again.')


"""
 Define a dict whose keys are dates (represented by strings) from the most recent
week and whose values are temperatures. Ask the user to enter a date, and display the temperature on that date, as well as the previous and subsequent dates,
if available.
"""
def dates_temp():
    DATES = {'07/03':'1', '08/03':'2', '09/03':'-1', '10/03':'10', '11/03':'-5','12/03':'1','13/03':'0'}
    choice = input('Enter date to see the weather in format "dd/mm": ')
    if choice in DATES:
        dict_keys = list(DATES.keys())
        prevd = dict_keys[dict_keys.index(choice) -1] if (dict_keys.index(choice) -1) >=0 else ''
        nextd = dict_keys[dict_keys.index(choice) + 1] if (dict_keys.index(choice) + 1) < len(dict_keys) else ''

        # print(str(dict_keys[prevd:prevd+1]),str(dict_keys[nextd:nextd+1]))
        print(f'Temperature of previouse day, chosen day, next day: {DATES.get(prevd, "NOT AVAILABLE")},{DATES.get(choice)},{DATES.get(nextd,"NOT AVAILABLE")}')
    else:
        print('Either entered wrong format or such date does not exists in previouse week.')

"""
 Define a dict whose keys are names of people in your family, and whose values
are their birth dates, as represented by Python date objects (http://mng.bz/
jggr). Ask the user to enter the name of someone in your family, and have the
program calculate how many days old that person is.
"""
def birthday():
    from datetime import date
    BIRTHDAYS = {'evaldas':date(1989,7,9),'aiste':date(1987,8,13), 'laima':date(1963,7,12),'albinas':date(1964,7,19)}
    name = input(f"Enter name {list(BIRTHDAYS.keys())}: ")
    print((date.today()-BIRTHDAYS[name]).days // 365.25 if name in BIRTHDAYS else 'Name does not exists')

if __name__ == '__main__':
    birthday()

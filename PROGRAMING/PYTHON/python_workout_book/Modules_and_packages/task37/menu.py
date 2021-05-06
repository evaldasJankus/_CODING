## IMPORTS

#-------------------------MAIN TASK--------------------------------------------
"""
Specifically, write a new module called “menu” (in the file menu.py). The module
should define a function, also called menu. The function takes any number of keyvalue pairs as arguments. Each value should be a callable, a fancy name for a function
or class in Python.
 When the function is invoked, the user is asked to enter some input. If the user
enters a string that matches one of the keyword arguments, the function associated
with that keyword will be invoked, and its return value will be returned to menu’s caller.
If the user enters a string that’s not one of the keyword arguments, they’ll be given an
error message and asked to try again.
"""
def menu(**kwargs):
    if not kwargs: return 'Menu has no options'
    menu_options = '/'.join(kwargs)
    while 1:
        choice = input(f"Enter an option from a menu [{menu_options.upper()}]: ")
        if choice in kwargs: return kwargs[choice]()
        print(f'Your choice <{choice}> is not valid!')


#-------------------------BEYOND THE TASK--------------------------------------

if __name__ == '__main__':
    import pytest
    def start_o(): return 'START'
    def edit_o(): return 'EDIT'
    def about_o(): return 'ABOUT'
    def exit_o(): return 'EXIT'
    # TESTS
    return_value = menu(start=start_o, edit=edit_o, about=about_o, exit=exit_o)
    print(return_value)

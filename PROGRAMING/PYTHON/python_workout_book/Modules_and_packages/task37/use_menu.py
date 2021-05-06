## IMPORTS
from menu import menu

def start_o(): return 'You have choisen menu option START'
def edit_o(): return 'You have choisen menu option EDIT'
def about_o(): return 'You have choisen menu option ABOUT'
def exit_o(): return 'You have choisen menu option EXIT'

if __name__=='__main__':
    return_value = menu(start=start_o, edit=edit_o, about=about_o, exit=exit_o)
    print(f'Result is: {return_value}')

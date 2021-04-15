##CAPSTONE PROJECT##
# Write a menu driven program called project_base_file.py that will allow the user to enter
# commands and process these commands until the quit command is entered.
# The program will store and maintain personal profile information (using a List of Profile objects). Personal
# profile information will be stored in a text file that will be read in when the program commences.
# Once the initial profile data has been read in from the file, the program should allow the user to
# interactively query and manipulate the profile information.
####################
# Your solutions MUST NOT use:
#  Built-in functions (other than the int(), input(), print(), range(), open(),
# close(), len() and str() functions).
#  Slice expressions to select a range of elements from a string or list. i.e. name[start:end].
#  String or list methods (i.e. other than those mentioned in the 'MAY make use' of section above.
#  Global variables as described in week 8 lecture.
#  The use break, return or continue statements (or any other technique to break out of
# loops) in your solution – doing so will result in a significant mark deduction.

## IMPORTS ##
import profile
import list_function

## VARIABLES ##
profile_list = []                 # List of profile instances
filename = 'profiles.txt'         # Input file - reading information from
output_file = 'new_profiles.txt'  # Output file - writting information to(results)

## FUNCTIONS ##
# Reads input data from a file 'filename' and save all profiles to 'profile_list'
# Requirements: 1) You may use String and/or List methods in this function only
def read_file(filename, profile_list):
    with open(filename) as f:
        for line in f:
            friends = [] # friends list of each profile read from a file
            person = line.split()
            status = f.readline().strip('\n')
            friend_num = int(f.readline())
            for _ in range(friend_num):
                friends.append(f.readline().strip('\n'))
            profile_ = profile.Profile(person[0], person[1], person[2], person[3], status)
            profile_.set_friends_list(friends)
            profile_list.append(profile_)
    return profile_list

# Saves results to 'output_file' on terminating a program
# Requirements: 1) You must use a loop in your solution
def write_to_file(filename, profile_list):
    with open(filename, 'w') as f:
        for profile_ in profile_list:
            f.write(profile_.__str__())

# Checks if email exists in profile list. Returns index_num if it does, -1 if it doesn't
# Requirements: 1) You must use a loop in your solution. 2) You must not use list methods in your solution.
def find_profile(profile_list, email):
    index_counter = 0
    for profile_ in profile_list:
        if profile_.get_email() == email:
            return index_counter
        index_counter += 1
    else:
        return -1

# Adds no profile if email does not exists in profile list, shows an error message if it does.
# Requirements: 1) Must use function 'find_profile' 2) May use list.append()
def add_profile(profile_list):
    email = input('Please enter email address: ')
    if find_profile(profile_list, email) > -1:
        print(f'<{email}> already exists in profiles.')
    else:
        g_name = input('Please enter given name: ')
        f_name = input('Please enter family name: ')
        gender = input('Please enter gender: ')
        status = input('Please enter current status: ')
        profile_ = profile.Profile(g_name, f_name, email, gender, status)
        profile_list.append(profile_)
        print(f'Successfully added <{email}> to profiles.')
    return profile_list

# Prints full summary of all profiles in a format provided 'PARTB - Sample Output'
# Requirements: 1) You must use a loop in your solution.
def display_summary(profile_list):
    l = 80  # Static length of styling simbols '-', '=', can be made dynamicly if needed
    print(f'{"":=^{l}}')
    print('Profile Summary')
    print(f'{"":=^{l}}')
    print(f'{"":-^{l}}')
    for profile_ in profile_list:
        print_profile(profile_)  # Prints single profile summary
        print(f'{"":-^{l}}')
    else:
        print(f'{"":=^{l}}')

# Search profile in profiles list. Shows single profile summary if found, otherwise
# shows an error message
def search_profile(profile_list):
    email = input('Please enter an email address: ')
    index_num = find_profile(profile_list, email)
    if index_num == -1:
        print(f'<{email}> is NOT found in profiles')
    else:
        profile_ = profile_list[index_num]
        print_profile(profile_)

# Prints provided profile summary. Created to avoid code repeating
# in display_summary() and search_profile().
def print_profile(profile_):
    print(f'{profile_.get_given_name()} {profile_.get_family_name()} ({profile_.get_gender()} | {profile_.get_email()})')
    print(f'- {profile_.get_status()}')
    if profile_.get_number_friends() == 0:
        print('- No Friends yet ...')
    else:
        print(f'- Friends ({profile_.get_number_friends()}):')
        for friend in profile_.get_friends_list():
            index_num = find_profile(profile_list, friend)
            print(f'\t{profile_list[index_num].get_given_name()} {profile_list[index_num].get_family_name()}')

# Removes profile from a profile list, if not found return an error message
# Requirements: 1) You may use list.append() 2) You must use 'find_profile' method
def remove_profile(profile_list):
    email = input('Please enter email address: ')
    index_num = find_profile(profile_list, email)
    if index_num == -1:
        print(f'<{email}> is NOT found in profiles.')
    else:
        profile_list = list_function.remove_value(profile_list, index_num)
        for profile_ in profile_list:
            profile_.remove_friend(email)
        print(f'Successfully removed <{email}> from profiles.')
    return profile_list

# Provides 3 option to choose: status, add_friend, remove_friend. Updates profile
# accordingly, if profile not found shows an error message and returns to main menu.
def update_profile(profile_list):
    email = input('Please enter email address: ')
    index_num = find_profile(profile_list, email)
    if index_num == -1:
        print(f'<{email}> is NOT found in profiles')
    else:
        choices = ['status', 'add_friend','remove_friend']
        s_choices = list_function.to_string(choices,sep='|')
        choice = input(f'Update {profile_list[index_num].get_given_name()} {profile_list[index_num].get_family_name()} ({s_choices}): ')
        if choice not in choices:  # Requirement of documentation in PDF output scenarios 'Sample output 5'
            print(f'<{choice}> is NOT a valid command - returning to main menu.')
        else:
            if choice == choices[0]:
                status = input(f'Please enter {choice} to udpate: ')
                profile_list[index_num].set_status(status)
                print(f'Profile successfully updated, status for {profile_list[index_num].get_given_name()} changed. Updated profile below:')
                print_profile(profile_list[index_num])
            elif choice == choices[1]:
                email = input('Please enter email address of friend to add: ')
                if find_profile(profile_list, email) == -1:
                    print(f'<{email}> is NOT found in profiles')
                else:
                    if profile_list[index_num].is_friend(email):
                        print(f'{profile_list[find_profile(profile_list, email)].get_given_name()}<{email}> is already a friend of {profile_list[index_num].get_given_name()}. Duplicate entries are not allowed.')
                    else:
                        profile_list[index_num].add_friend(email)
                        print(f'Profile successfully updated, {profile_list[find_profile(profile_list, email)].get_given_name()}<{email}> added to friends list. Updated profile below:')
                        print_profile(profile_list[index_num])
            else:
                email = input('Please enter email address of friend to remove: ')
                if not profile_list[index_num].is_friend(email):
                    print(f'<{email}> is NOT in friends list of {profile_list[index_num].get_given_name()}.')
                else:
                    profile_list[index_num].remove_friend(email)
                    print(f'Profile successfully updated, {profile_list[find_profile(profile_list, email)].get_given_name()}<{email}> removed from friends list. Updated profile below:')
                    print_profile(profile_list[index_num])

# Main menu, provides action list for profiles: summary, add, remove, search, update, quit
# quit - terminates the program, all other actions described above in methods
def main_menu(profile_list):
    choices = ['summary', 'add','remove','search','update','quit']
    s_choices = list_function.to_string(choices,sep='|')
    choice = None
    while not choice == choices[-1]:
        choice = input(f'\nPlease enter choice ({s_choices}): ')
        print() # To leave empty space as in PDF
        if choice not in choices:
            print(f'<{choice}> is NOT a valid command. Please try again.')
        else:
            if choice == choices[0]:
                display_summary(profile_list)
            elif choice == choices[1]:
                profile_list = add_profile(profile_list)
            elif choice == choices[2]:
                profile_list = remove_profile(profile_list)
            elif choice == choices[3]:
                search_profile(profile_list)
            elif choice == choices[4]:
                update_profile(profile_list)
    write_to_file(output_file, profile_list)          # Saving updated 'profile_list' to 'output_file'

if __name__ == '__main__':                            # If file is run directly (not an import), runs code below
    profile_list = read_file(filename, profile_list)  # Storing profiles into list
    main_menu(profile_list)                           # Main interactive mode
    print("\n\n-- Program terminating --\n")          # Program endinf with final print message

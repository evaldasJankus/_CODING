# PROJECT: Multi-clipboard (https://www.youtube.com/watch?v=Oz3W-LKfafE)
import sys
import clipboard
import json

data_file = 'clipboard.json'
allowed_commands = ['save', 'copy', 'show', 'show-all']

def save_to_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file)

def load_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except OSError:
        return {}

def main():
    len_of_arguments = len(sys.argv)
    data = load_from_file(data_file)

    if len_of_arguments == 2:
        command = sys.argv[1]
        if command in allowed_commands:
            print(f'Processing command <{command}> ...\n{"-"*12}')
            if command == allowed_commands[0]: # command {save}
                key = input('Enter key: ')
                if key in data.keys():
                    if input(f'KEY <{key}> already existing. Do you want to overide Y/N?').lower() == 'y':
                        data[key] = clipboard.paste()
                        save_to_file(data_file, data)
                    else:
                        print(f'<{command}> terminated...')
                else:
                    data[key] = clipboard.paste()
                    save_to_file(data_file, data)
            elif command == allowed_commands[1]: # command {copy}
                key = input('Enter key: ')
                if key in data.keys():
                    clipboard.copy(data[key])
                else:
                    print(f'Key <{key}> doen not exist')
            elif command == allowed_commands[2]: # command {show}
                key = input('Enter key: ')
                if key in data.keys():
                    print(f'Clipboard by key: <{key}>\nHas input: <{data[key]}>')
                else:
                    print(f'Key <{key}> doen not exist')
            else: # command {show-all}
                print('Full clipboard:')
                for k,v in data.items(): print(f'{k} => {v}')
        else:
            print(f'NOT ALLOWED command <{command}>. Allowed commands: <{" | ".join(allowed_commands)}>')
    else: print(f'Should be exactly one command! Provided: {len_of_arguments-1} commands')


if __name__ == '__main__':
    main()

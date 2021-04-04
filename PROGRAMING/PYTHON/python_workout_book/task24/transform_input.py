
#-------------------------MAIN TASK--------------------------------------------
"""
Transform any read line into reverse order by line, lines them selves remains in same order
"""
def transform_input_output(filein='data.txt', fileout='results.txt'):
    with open(filein) as f_reader, open(fileout,'w') as f_writer:
        for line in f_reader:
            f_writer.write(line[::-1].lstrip('\n')+'\n')

#-------------------------BEYOND THE TASK--------------------------------------
"""
 “Encrypt” a text file by turning all of its characters into their numeric equivalents
(with the built-in ord function) and writing that file to disk. Now “decrypt”
the file (using the built-in chr function), turning the numbers back into their
original characters.
"""
def encrypt_decrypt_files(filein='data_file',file_encrypt='encrypt_file',file_decrypt='decrypt_file'):
    with open(filein) as f_reader, open(file_encrypt,'w') as f_encrypt:
        for line in f_reader:
            for cha in line: f_encrypt.write(f'{ord(cha)} ') if ord(cha) != 10 else f_encrypt.write(f'{ord(cha)}\n')

    with open(file_encrypt,'r') as f_encrypt, open(file_decrypt,'w') as f_decrypt:
        for line in f_encrypt:
            for cha in line.rstrip('\n').split():
                f_decrypt.write(chr(int(cha)))

"""
 Given an existing text file, create two new text files. The new files will each
contain the same number of lines as the input file. In one output file, you’ll write
all of the vowels (a, e, i, o, and u) from the input file. In the other, you’ll write
all of the consonants. (You can ignore punctuation and whitespace.)
"""
def encrypt_decrypt_files(filein='data_file',file_v='vowels.txt',file_c='consonants.txt'):
    vowels = 'aeiou'
    with open(filein) as f_reader, open(file_v,'w') as f_vowels, open(file_c, 'w') as f_consonants:
        for line in f_reader:
            for cha in line:
                if cha in vowels: f_vowels.write(cha)
                elif cha.isalpha() and not(cha in vowels): f_consonants.write(cha)
            else:
                f_vowels.write('\n');f_consonants.write('\n')

"""
 The final field in /etc/passwd is the shell, the Unix command interpreter that’s
invoked when a user logs in. Create a file, containing one line per shell, in
which the shell’s name is written, followed by all of the usernames that use the
shell; for example
"""
def password_file(filein='passwd.txt',fileout='result_shels'):
    shell_users = {}
    with open(filein) as f_reader, open(fileout,'w') as f_writer:
        for line in f_reader:
            if not line.startswith('#'):
                line = line.rstrip().split(':')
                shell_users[line[-1]] = shell_users.get(line[-1],[]) + [line[0]]
        for key in shell_users:
            f_writer.write(f'{key}: {",".join(shell_users[key])}\n')


if __name__ == '__main__':
    # transform_input_output()
    # encrypt_decrypt_files()
    # encrypt_decrypt_files()
    password_file()

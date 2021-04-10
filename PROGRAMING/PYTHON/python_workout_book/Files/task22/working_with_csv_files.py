import csv

#-------------------------MAIN TASK--------------------------------------------
# Test before executing main task
# Made this fucntion a generator, becaues we have already mae some tesing fucntion
# and why not to use it in our solution for also practixing generator
def simple_test_reader(filename='data_file.csv'):
    with open(filename) as csvfile:
        file_reader = csv.reader(csvfile, delimiter=':')
        for line in file_reader:
            yield line

def simple_test_writer(filein='data_file.csv',fileout='date_output_test.csv'):
    with open(fileout,'w') as csv_writer:
        file_writer = csv.writer(csv_writer, delimiter=' ')
        # file_writer.writerows(list(simple_test_reader(filein)))
        for line in simple_test_reader(filein):
            file_writer.writerow(line)

# Test END == before executing main task
"""
For this exercise, create a function, passwd_to_csv, that takes two filenames as
arguments: the first is a passwd-style file to read from, and the second is the name of a
file in which to write the output.
 The new file’s contents are the username (index 0) and the user ID (index 2).
Note that a record may contain a comment, in which case it will not have anything at
index 2; you should take that into consideration when writing the file. The output file
should use TAB characters to separate the elements.
"""
def passwd_to_csv(filein='password_log', fileout='password_out.csv'):
    # GOOD NOTE: with content manager can take any number of objects, example:
    # "with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:"
    with open(fileout,'w') as csv_writer:
        writer = csv.writer(csv_writer, delimiter='\t')
        for line in simple_test_reader(filein):
            if len(line) > 1: writer.writerow([line[0],line[2]])

#-------------------------BEYOND THE TASK--------------------------------------
"""
* Extend this exercise by asking the user to enter a space-separated list of integers,
indicating which fields should be written to the output CSV file. Also ask
the user which character should be used as a delimiter in the output file. Then
read from /etc/passwd, writing the user’s chosen fields, separated by the user’s
chosen delimiter.
"""
# In this case just wanted to add some logic to avoid some invalid data, and
# also practice def usage in the another def
def find_lengh_of_row(filein):
    with open(filein) as f:
        reader = csv.reader(f,delimiter=':')
        for line in reader:
            if len(line) > 2: return len(line)
        return 0

def passwd_to_csv_user_fields(filein='passwd.txt', fileout='password_out.csv'):
    with open(filein) as csv_reader, open(fileout,'w') as csv_writer:
        row_length = find_lengh_of_row(filein)

        field = input('Enter column numbers which should be parsed out to csv file: ')
        delim = input('Enter separation delimiter: ')
        field = list(filter(lambda x: x < row_length,[abs(int(x)) for x in field.split()]))

        writer = csv.writer(csv_writer, delimiter=delim)
        writer.writerow([f'Accepted column numbers are: {field}'])

        reader = csv.reader(csv_reader, delimiter=':',)
        for line in reader:
            if len(line) >1: writer.writerow([line[col] for col in field])
        print('DONE')

"""
 Write a function that writes a dict to a CSV file. Each line in the CSV file should
contain three fields: (1) the key, which we’ll assume to be a string, (2) the value,
and (3) the type of the value (e.g., str or int).
"""
def export_dict_to_csv(fileout='out_dict_test.csv'):
    dict_data = {'a':1,'b':'a','c':[1,2,'a'],'d':(1,2)}
    with open(fileout, 'w') as csv_writer:
        writer = csv.writer(csv_writer)
        for key in dict_data:
            writer.writerow([key,dict_data[key],type(dict_data[key])])

"""
 Create a CSV file, in which each line contains 10 random integers between 10
and 100. Now read the file back, and print the sum and mean of the numbers
on each line.
"""
def random_numbers_csv_file(filename='random_numbers.csv'):
    from random import randint
    n, m = 7, 10 # number of rows and columns
    with open(filename,'w') as csv_writer:
        writer = csv.writer(csv_writer)
        for row in range(n): writer.writerow([randint(10,100) for _ in range(m)])

    row_counter = 0

    with open(filename, newline='\r\n') as csv_reader:
        for line in csv.reader(csv_reader):
            print(f'Row: {row_counter}\tSum: {sum([int(x) for x in line])}\tAverage: {sum([int(x) for x in line])/len(line)}'); row_counter += 1


if __name__=='__main__':
    # simple_test()
    # simple_test_writer()
    # passwd_to_csv()
    # passwd_to_csv_user_fields()
    # export_dict_to_csv()
    random_numbers_csv_file()

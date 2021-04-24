## IMPORTS
from pathlib import Path

#-------------------------MAIN TASK--------------------------------------------
"""
Create a function to imitate python function map(). A function should apply
a fucntion to each dictionary value
"""
def transform_values(func, d):
    return {k:func(v) for k,v in d.items()}
#-------------------------BEYOND THE TASK--------------------------------------
"""
Expand the transform_values exercise, taking two function arguments, rather
than just one. The first function argument will work as before, being applied to
the value and producing output. The second function argument takes two arguments,
a key and a value, and determines whether there will be any output at
all. That is, the second function will return True or False and will allow us to
selectively create a key-value pair in the output dict
"""
def transform_values_extended(func1, func2, d):
    return {k:func1(v) for k,v in d.items() if func2(k,v)}

"""
 Use a dict comprehension to create a dict in which the keys are usernames and
the values are (integer) user IDs, based on a Unix-style /etc/passwd file. Hint:
in a typical /etc/passwd file, the usernames are the first field in a row (i.e.,
index 0), and the user IDs are the third field in a row (i.e., index 2). If you need
to download a sample /etc/passwd file, you can get it from http://mng.bz/
2XXg. Note that this sample file contains comment lines, meaning that you’ll
need to remove them when creating your dict.
"""
def transform_values_from_file(f='passwd.txt'):
    d = {}
    with open(f) as f_reader:
        d = {line.split(':')[0]:line.split(':')[2] for line in f_reader if not line.startswith('#')}
    return d

"""
 Write a function that takes a directory name (i.e., a string) as an argument. The
function should return a dict in which the keys are the names of files in that
directory, and the values are the file sizes. You can use os.listdir or glob
.glob to get the files, but because only regular files have sizes, you’ll want to filter the results using methods from os.path. To determine the file size, you can
use os.stat or (if you prefer) just check the length of the string resulting from
reading the file.
"""
def transform_values_from_directory(mypath='.'):
    d = {}
    entries = Path(mypath)
    return {file.name:file.stat().st_size for file in entries.iterdir() if file.is_file()}


if __name__=="__main__":
    # print(transform_values(lambda x: x*x, {'a':1,'b':2,'c':3}))
    # print(transform_values_from_file())
    print(transform_values_from_directory())

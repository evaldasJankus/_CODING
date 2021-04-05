import shutil
from pathlib import Path

#-------------------------MAIN TASK--------------------------------------------
"""
Create xml string from given arguments, First argument - tag name, Second - tags content
all therest is atributes
"""
# In this case making *args to let people enter more content with different atributes,
# will be treated as separate sentences.
def myxml(*args, **kwargs):
    tag, content = " ".join(args[:1]), ". ".join(args[1:])
    atributes_dict = [f'{key}="{val}"' for key, val in kwargs.items()]
    atributes_dict.insert(0,tag)
    return f'<{" ".join(atributes_dict)}>{content}</{tag}>'

#-------------------------BEYOND THE TASK--------------------------------------
# TODO Next:
"""
 Write a copyfile function that takes one mandatory argument—the name of
an input file—and any number of additional arguments: the names of files to
which the input should be copied. Calling copyfile('myfile.txt', 'copy1
.txt', 'copy2.txt', 'copy3.txt') will create three copies of myfile.txt:
one each in copy1.txt, copy2.txt, and copy3.txt.
"""
def copy_file(filein,*args):
    if not args:
        print('no output file was provided!\nPROGRAM TERMINATING')
        return
    else:
        with open(filein) as f_reader:
            for file in args:
                with open(file,'w') as f_writer:
                    for line in f_reader:
                        f_writer.write(line)
                f_reader.seek(0)


# Using library shutil
def copy_file_with_shutil_copyfile(filein, *args):
    if not args:
        print('no output file was provided!\nPROGRAM TERMINATING')
        return
    else:
        for file in args: shutil.copyfile(Path(filein),Path(file))

"""
 Write a “factorial” function that takes any number of numeric arguments and
returns the result of multiplying them all by one another
"""
def factorial_func(*args):
    if len(args) == 1: return args[0]
    return args[0] * factorial_func(*args[1:])

"""
 Write an anyjoin function that works similarly to str.join, except that the first
argument is a sequence of any types (not just of strings), and the second argument is
the “glue” that we put between elements, defaulting to " " (a space). So
anyjoin([1,2,3]) will return 1 2 3, and anyjoin('abc', pass:'**') will
return pass:a**b**c
"""
def anyjoin(iter, jointer=' '):
    return jointer.join([str(item) for item in iter])

if __name__=='__main__':
    # print(myxml("strong", "Hello world",'My name is Evaldas'))
    # copy_file('data_input.txt','btask1/copy1.txt','btask1/copy2.txt')
    # print(factorial_func(-10,5,6,-1))
    print(anyjoin({1:'a',2:1,'b':3},'**'))

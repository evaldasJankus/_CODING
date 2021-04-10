#-------------------------MAIN TASK--------------------------------------------
"""
Read all files in the directory and find longest word in each file. Return dict_info
with key value as file name and VALUES as longest word
"""
def longest_word_in_file(filename):
    # print(filename)
    with open(filename) as f:
        return max([max(map(str.strip, line.split()), key=len) if line != '\n' else '' for line in f], key=len)

def all_longests_words(cpath='.'):
    import os
    # results_dict = {}
    with os.scandir(cpath) as entries:
        # for file in entries:
            # if file.name.endswith('.py'): continue
            # results_dict[file.name] = longest_word_in_file(file.name)
        # return results_dict
        return {file.name:longest_word_in_file(file.path) for file in entries if not file.name.endswith('.py') } # One liner

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Use the hashlib module in the Python standard library, and the md5 function
within it, to calculate the MD5 hash for the contents of every file in a userspecified
directory. Then print all of the filenames and their MD5 hashes.
"""
def hash_files_content(cpath='.'):
    import hashlib, os

    def hashed_file_content(filename):
        with open(filename,'rb') as f:
            return hashlib.md5(f.read()).hexdigest()

    with os.scandir(cpath) as entries:
        return {file.name:hashed_file_content(file.path) for file in entries if not file.name.endswith('.py')}

"""
 Ask the user for a directory name. Show all of the files in the directory, as well
as how long ago the directory was modified. You will probably want to use a
combination of os.stat and the Arrow package on PyPI (http://mng.bz/nPPK)
to do this easily.
"""
def last_time_modified_and_files(cpath='.'):
    from pathlib import Path
    from datetime import datetime
    output_dict = {}

    # datetime.datetime.utcfromtimestamp(ff1.stat().st_mtime)
    with Path(cpath) as dir:
        output_dict['Directory'] = str(dir.cwd())
        output_dict['Last modified'] = datetime.fromtimestamp(dir.stat().st_mtime).ctime()
        for file in dir.iterdir():
            if file.is_file():
                output_dict['Files'] = list(output_dict.get('Files',[])) + [[file.name,datetime.utcfromtimestamp(file.stat().st_mtime).ctime()]]
    return output_dict

"""
Open an HTTP server’s log file. (If you lack one, then you can read one from
me at http://mng.bz/vxxM.) Summarize how many requests resulted in numeric
response codes—202, 304, and so on.
"""
def search_log_file(filename='mini-access-log.txt'):
    codes_counter_dict = {}
    with open(filename) as f:
        for line in f:
            line = line.split()
            codes_counter_dict[line[8]] = codes_counter_dict.get(line[8],0) + 1
    return codes_counter_dict


if __name__ == '__main__':
    # print(all_longests_words('..\\task20'))
    # print(hash_files_content('..\\task20'))
    # print(last_time_modified_and_files())
    print(search_log_file())

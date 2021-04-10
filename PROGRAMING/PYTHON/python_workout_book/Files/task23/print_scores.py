from os import scandir
import json, csv, pathlib, time

#-------------------------MAIN TASK--------------------------------------------
"""
In this exercise, you’re analyzing test data in a high school. There’s a scores directory
on the filesystem containing a number of files in JSON format. Each file represents the
scores for one class. Write a function, print_scores, that takes a directory
name as an argument and prints a summary of the student scores it finds.
"""
def print_scores(cpath):
    scores_dict = {}
    with scandir(cpath) as entries:
        for file in entries:
            scores_dict[file.name] = {}
            # if file.name.startswith('10'):
            with open(file.path) as test:
                for line in json.load(test):
                    for key, val in line.items():
                        # Using with setdefault:
                        scores_dict[file.name].setdefault(key, [])
                        scores_dict[file.name][key].append(val)
                        # Using with dict.get:
                        # scores_dict[file.name][key] = scores_dict[file.name].get(key,[]) + [val]

    for key, val in scores_dict.items():
        if val:
            print(key,':')
            for subject in scores_dict[key]:
                print('\tSubject',subject,'\tMin:',min(scores_dict[key][subject]),end='')
                print('\tMax:',max(scores_dict[key][subject]),end='')
                print('\tAverage:',sum(scores_dict[key][subject])/len(scores_dict[key][subject]))


#-------------------------BEYOND THE TASK--------------------------------------
# For testing
def read_json(filename):
    with open(filename) as file:
        print(json.load(file))

"""
 Convert /etc/passwd from a CSV-style file into a JSON-formatted file. The
JSON file will contain the equivalent of a list of Python tuples, with each tuple
representing one line from the file.
"""
def csv_file_to_json(filename):
    list_tuple = []
    dict_tuple = {}
    counter = 0
    with open(filename) as csv_reader, open('json_out.json','w') as json_out:
        for line in csv.reader(csv_reader, delimiter=':'):
            if not line[0].startswith('#'):
                # Using list
                # list_tuple.append(tuple(line))

                # USing dict
                dict_tuple[counter]  = line
                counter += 1
        json.dump(dict_tuple, json_out, indent=4)

"""
 For a slightly different challenge, turn each line in the file into a Python dict.
This will require identifying each field with a unique column or key name. If
you’re not sure what each field in /etc/passwd does, you can give it an arbitrary name.
"""
def csv_file_to_json_dict(filename):
    dict_tuple = {}
    counter = 0
    with open(filename) as csv_reader, open('json_out.json','w') as json_out:
        for line in csv.reader(csv_reader, delimiter=':'):
            if not line[0].startswith('#'):
                # USing dict
                dict_tuple[counter]  = {ind:val for ind, val in enumerate(line)}
                counter += 1
        json.dump(dict_tuple, json_out, indent=4)

# LEFT TO DO
"""
 Ask the user for the name of a directory. Iterate through each file in that directory
(ignoring subdirectories), getting (via os.stat) the size of the file and when it was
last modified. Create a JSON-formatted file on disk listing each filename, size, and
modification timestamp. Then read the file back in, and identify which files were
modified most and least recently, and which files are largest and smallest, in that
directory.
"""
def read_directory_from_user(dirname='.'):
    files_info = {}
    for elem in pathlib.Path(dirname).iterdir():
        if elem.is_dir(): continue
        # print(elem.stat().)
        files_info[elem.name] = [elem.stat().st_size,elem.stat().st_mtime,]
    with open('file_info_results.json','w') as json_out:
        json.dump(files_info,json_out, indent=4)
    with open('file_info_results.json') as json_reader:

        data = json.load(json_reader)
        size_sorted = sorted(data, key=lambda x: data[x][0])
        date_sorted = sorted(data, key=lambda x: data[x][1])
        print(f'File modified most recent {date_sorted[-1]}: {time.ctime(data[date_sorted[-1]][1])}')
        print(f'File modified least recent {date_sorted[0]}: {time.ctime(data[date_sorted[0]][1])}')
        print(f'Largest file {size_sorted[-1]}: {data[size_sorted[-1]][0]/1000:.2f} KB')
        print(f'Smallest file {size_sorted[0]}: {data[size_sorted[0]][0]/1000:.2f} KB')

if __name__ == '__main__':
    # print_scores('scores')
    # csv_file_to_json('passwd.txt')
    # csv_file_to_json_dict('passwd.txt')
    read_directory_from_user()

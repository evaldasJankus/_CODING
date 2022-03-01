# Guided article to work with zip files in Python:: https://realpython.com/python-zipfile/#getting-started-with-zip-files
import zipfile, time, pathlib
from os import scandir

# Getting all file names, which is not given extension {given_extension} file, from given directory
# key incensitive.
def get_files(dir_path, given_extension=None):
    with scandir(dir_path) as files:
        if given_extension == None:
            return [file.name for file in files]
        return [file.name for file in files if not file.name.lower().endswith(given_extension)]

# Creating a zip file or appending a file to a zip file with given zipfile path
def create_modify_zip_file(zip_file_path, zip_file_name, files_to_zip):
    if pathlib.Path(f'{zip_file_path}/{zip_file_name}').exists():
        print('File already exist!')
        return

    with zipfile.ZipFile(f'{zip_file_path}\{zip_file_name}', 'a') as archive:

        print(f' CREATING {zip_file_name} '.center(3*len(zip_file_name),'-'))
        print(archive.namelist())
        for file in files_to_zip:
            if f'{zip_file_path}/{file}' in archive.namelist(): # To avoid duplicates
                continue
            else:
                print(f'CREATING {file} ... ', end='')
                time.sleep(2)
                archive.write(f'{zip_file_path}\{file}')
                print('Done')
        print(f'FILE {archive.filename} created!'.center(len(f'FILE {archive.filename} created!') * 2, '-'))
        archive.printdir()

# Prints a lsit of ZipInfo objects for all members of zipfile
def zipfile_infolist(zip_file_path, zip_file_name):
    with zipfile.ZipFile(f'{zip_file_path}\{zip_file_name}', 'r') as archive:
        print(archive.infolist())

# Returns name list of files in the zip, of given extension
def zipfile_namelist(zip_file_path, zip_file_name, given_extension=tuple('.txt')):
    with zipfile.ZipFile(f'{zip_file_path}\{zip_file_name}', 'r') as archive:
        return [file_name for file_name in archive.namelist() if file_name.endswith(given_extension)]

# Prints information of the each file in zipfile, have to privide file name
def zipfile_getInfo(zip_file_path, zip_file_name, file_names):
    with zipfile.ZipFile(f'{zip_file_path}\{zip_file_name}', 'r') as archive:
        for file in file_names:
            print(f"{file}".center(2*len(file),'*'))
            print(archive.getinfo(file))

# Read list of files from zip file, without opening it.
def zipfile_read_from_zippedFile(zip_file_path, zip_file_name, file_names):
    with zipfile.ZipFile(f'{zip_file_path}\{zip_file_name}', 'r') as archive:
        for file in file_names:
            print(f'READING {file}'.center(len(f'READING {file}') * 3, '-'))
            with archive.open(file, mode='r') as f:
                for line in f:
                    print(line.decode(encoding='utf-8').rstrip())

# Extract one given file from a zip, same approach for
def extract_zip_file(zip_file_path, zip_file_name, file_names, extract_dir):
    with zipfile.ZipFile(f'{zip_file_path}\{zip_file_name}', 'r') as archive:
        for file in file_names:
            extracted_path = archive.extract(f'{zip_file_path}/{file}', path=extract_dir)
            print(extracted_path.center(len(extracted_path)*2,'-'))

# Extract all files from zip archive
def extract_all_files_from_zip(zip_file_path, zip_file_name, extract_dir):
    with zipfile.ZipFile(f'{zip_file_path}\{zip_file_name}', 'r') as archive:
        archive.extractall(path=extract_dir)

# Compile and compress .zip archive, using ZIP_Deflate method
def compile_and_compress_zip(zip_file_path, zip_file_name, files_to_zip):
    if pathlib.Path(f'{zip_file_path}/{zip_file_name}').exists():
        print('File already exist!')
        return

    with zipfile.ZipFile(f'{zip_file_path}\{zip_file_name}', 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:

        print(f' CREATING {zip_file_name} '.center(3*len(zip_file_name),'-'))
        print(archive.namelist())
        for file in files_to_zip:
            if f'{zip_file_path}/{file}' in archive.namelist(): # To avoid duplicates
                continue
            else:
                print(f'CREATING {file} ... ', end='')
                time.sleep(2)
                archive.write(f'{zip_file_path}\{file}')
                print('Done')
        print(f'FILE {archive.filename} created!'.center(len(f'FILE {archive.filename} created!') * 2, '-'))
        archive.printdir()

# Checking files size in given directory and with given_extensions. Default given_extension is None which means to check all files in the directory
def check_file_size(scan_path_dir, file_extension=None):
    with scandir(scan_path_dir) as files:
        if file_extension == None:
            for file in files: print(f"{file.name} = {file.stat().st_size} (bytes), {(file.stat().st_size / 1024):.2f} (Kb), {file.stat().st_size / 1024 / 1024:.2f} (MB)")
        else:
            for file in [x for x in files if x.name.split('.')[-1] in file_extension]: print(f"{file.name} = {file.stat().st_size} (bytes), {(file.stat().st_size / 1024):.2f} (Kb), {file.stat().st_size / 1024 / 1024:.2f} (MB)")

def main():
    # Inicial data
    zip_file_path = 'files_to_zip'
    archive_name = 'new_zip.zip'
    extension_not_to_use = ('.zip')

    # Creating ZIP file
    files_list = get_files(zip_file_path, extension_not_to_use)
    # create_modify_zip_file(zip_file_path, archive_name, files_list)

    # Read file in a zip while not unzipping a file it self
    # zipfile_read_from_zippedFile(zip_file_path, archive_name, zipfile_namelist(zip_file_path, archive_name))

    # Extracting one file from a zip
    # extract_zip_file(zip_file_path, archive_name, ['simple_text_file.txt'], 'extracted_one_file')

    # Extracting one file from a zip
    # extract_all_files_from_zip(zip_file_path, archive_name, 'extracted_one_file')

    # Creating {.zip} archive file using ZIP_Deflate compress method
    # archive_name = 'compress_zip_file.zip'
    # compile_and_compress_zip(zip_file_path, archive_name, files_list)

    # Checking files size in given directory
    check_file_size(zip_file_path, ['txt', 'jpg', 'JPG', 'pdf'])


if __name__ == '__main__':
    main()
    # Ended in below:
    # Building Importable ZIP Files With PyZipFile

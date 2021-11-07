import os

def quit(var):
    if var.lower() == 'q':
        print('\nBye!')
        exit()

def wd(work_dir):
    if work_dir == '':
        work_dir = os.getcwd()
        os.chdir(work_dir)
        print('\nWorking directory: ' + os.getcwd())
    else:
        while os.path.exists(work_dir) == False:
            print('\nDirectory does not exist!')
            work_dir = input('\nEnter a valid directory: ')
            return False
        
        if os.path.exists(work_dir):
            print('Exists:', os.path.exists(work_dir))
            os.chdir(work_dir)
            print('Current working directory:', os.getcwd())
            return True

def extensions():
    with open(f"{os.path.abspath('file_formats.txt')}", 'r') as f:
        extensions = f.read().split(',')
        return extensions

def touch(file_name):
    exists = os.path.exists(file_name)
    extension = extensions()

wd(input(f'>Enter the working directory (leave empty for choose this folder: {os.getcwd()}): '))

name = ''
while name != 'done' or name != '':
    name = input('\nEnter the file name (leave empty to quit): ')
    if name == 'q':
        quit(name)
    if name == 'done' or name == '':
        break
    if name == '':
        break
    if os.path.exists(name):
        print('\nFile already exists!')
        continue
    else:
        print('\nFile does not exist!')
        extension = input('\nEnter the file extension (leave empty to quit): ')
        if extension == 'q':
            quit(extension)
        if extension == 'done':
            break
        if extension == '':
            continue
        if extension in extension:
            print('\nFile extension is valid!')
            with open(name, 'w') as f:
                f.write('')
            print('\nFile created!')
        else:
            print('\nFile extension is not valid!')
            continue

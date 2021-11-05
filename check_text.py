import os

def quit(var):
    if var.lower() == 'q':
        print('\nBye!')
        exit()

def chdir(work_dir):
    wd = ''
    while wd == '':
        wd = work_dir
        quit(wd)

        if wd == '':
            wd = os.getcwd()

        if os.path.exists(wd):
            os.chdir(wd)

        else:
            print('not exists')

    print('The current directory is: ', os.getcwd())

def check_text(file_name):
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            text = f.read()
            print(text)
            quit(input('\nPress q to quit or any other key to continue: '))
    else:
        print('\nFile not found!')
        quit(input('\nPress q to quit or any other key to continue: '))

chdir(input('\nEnter the working directory: '))

with open("file_formats.txt", 'r') as f:
    extensions = f.read().split(',')

name = ''
names = [] 
while name != 'done':
    name = input('Enter the name of the file / folder: ')
    quit(name)
    if name == 'done' or name == '':
        break
    names.append(name)

print('The names of the folders / files are:', names)

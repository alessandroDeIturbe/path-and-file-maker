import os

def create_folder(folder):
    if os.path.isdir(name):
        print(f'Directory {name} already exists')
        os.chdir(name)
    else:
        os.mkdir(name)
        print('\nFolder', name, 'created')
        os.chdir(name)
        print('\nWorking directory:', os.getcwd())

def create(name):
    
    if name[-4:] == '.txt':
        print('\nCreating file', name)
        f = open(name, 'w')
        f.close()
    else:
        create_folder(name)

name = ''
names = []

working_dir = input('Enter the directory you want to search: ')

if working_dir == '':
    working_dir = os.getcwd()
else:
    working_dir = os.path.abspath(working_dir)
    os.chdir(working_dir)

print('Current working directory: ' + os.getcwd(), '\n')

while True:
    name = input('Enter the name of the folder / file (type q for close the program, type done for create the folders): ')
    if name == 'q':
        print('Bye')
        exit()
    elif name == 'done' or name == '':
        break
    else:
        names.append(name)

for name in names:

    if name[-1] == ' ':
        name = name[:-1]

    create(name)


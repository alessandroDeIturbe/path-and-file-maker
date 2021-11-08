import os

def quit(var):
    if var.lower() == 'q':
        print('Bye!\n')
        exit()

def wd(work_dir):
    quit(work_dir)
    if work_dir == '':
        work_dir = os.getcwd()
        os.chdir(work_dir)
    else:
        while os.path.exists(work_dir) == False:
            print('\nDirectory does not exist!')
            work_dir = input('\nEnter a valid directory: ')
            return False
        
        if os.path.exists(work_dir):
            print('Exists:', os.path.exists(work_dir))
            os.chdir(work_dir)
            return True

extensions = ['py', 'txt', 'docx', 'doc', 'c', 'cpp', 'cs']

wd(input(f'>Enter the working directory (leave empty for choose this folder: {os.getcwd()}): '))
print('\nCurrent working directory:', os.getcwd())

name = ''
while name != 'done' or name != '':
    file = False
    folder = False
    
    name = input('\nEnter the name (leave empty to quit): ')
    if name == 'q' or name == 'done': 
        name = 'q'
        quit(name)
    if name == '':
        break
    if name.find('.') != -1:
        names = name.split('.')
        for ext in extensions:
            if names[1] == ext:
                file = True
                folder = False
                break
            else:
                file = False
                folder = True
        if not file:
            print('\nFile extension not supported! create an issue if you think your extension must be added!')
    else:
        file = False
        folder = True
    if file:
        if os.path.exists(name):
            print('\nFile already exists!')
            continue
        else:
            print('\nFile does not exist!')
            with open(name, 'w') as f:
                f.write('')
                print('\nFile created!')
    elif folder:
        if os.path.exists(name):
            print('\nDirectory already exists!')
            continue
        else:
            print('\nDirectory does not exist!')
            print('\nCreating the directory...')
            os.mkdir(name)
            os.chdir(name)
    else:
        print('\nError!')
        break

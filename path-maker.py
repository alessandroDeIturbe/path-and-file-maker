import os
import sys
from colorama import Fore, Back, Style

def error(message):
    return f'{Back.RED}{Fore.WHITE}{message}{Style.RESET_ALL}'

argvs = sys.argv
argvs.pop(0)

if len(argvs) == 0:
    print(error('ERROR: No arguments'))
    print('Insert the path of the folders/file you want to create (REMEMBER, THE ROOT DIRECTORY IS THE CURRENT DIRECTORY)')
    print('Example: /folder1/folder2/folder3/file.txt')
    sys.exit(1)
if len(argvs) > 2:
    print(error('ERROR: Too many arguments'))
    print('Insert the path of the folders/file you want to create (REMEMBER, THE ROOT DIRECTORY IS THE CURRENT DIRECTORY)')
    print('Example: /folder1/folder2/folder3/file.txt')
    sys.exit(1)
if argvs[0] == '-h' or argvs[0] == '--help':

    print('USAGE: path-maker.py [path] [start-folder (if you want to start from a specific folder)]')
    print('Example One: path-maker.py /folder1/folder2/folder3/file.txt\nExample Two: path-maker.py /folder1/folder2/folder3/file.txt /folder1/folder2/folder3\n')
    sys.exit(0)

path = argvs[0].split('/')
if len(argvs) == 2:
    if os.path.exists(argvs[1]):
        start_folder = argvs[1]
        print(f"Start folder: {start_folder}")
    else:
        print('error: start folder does not exist')
        sys.exit(1)
else:
    start_folder = os.getcwd()
    print(f"start_folder: {start_folder}")

if len(path) == 1:
    if '.' in path[0]:
       with open(path[0], 'w') as f:
           f.write('')
    else:
        os.mkdir(path[0])
else:
    for i in range(len(path) - 1):
        if os.path.exists(path[i]):
            print(f'{path[i]} already exists')
            os.chdir(path[i])
        else:
            print(f'Creating {path[i]}...')
            os.mkdir(path[i])
            os.chdir(path[i])

    print(f'Creating {path[-1]}...')
    with open(path[-1], 'w') as f:
        f.write('')

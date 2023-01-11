#!/usr/bin/env python

import os
import sys
from colorama import Fore, Back, Style


def error(message):
    return f'{Back.RED}{Fore.WHITE}{message}{Style.RESET_ALL}'


def message(message):
    return f'{Back.BLUE}{Fore.WHITE}{message}{Style.RESET_ALL}'


def detect_file(file):
    if '.' in file:
        return True
    else:
        return False


def detect_multiple_files(files):
    if ',' in files:
        return True
    else:
        return False


argvs = sys.argv
argvs.pop(0)

if len(argvs) == 0 or len(argvs) > 2:
    if len(argvs) == 0:
        print(error('ERROR: No arguments given.'))
    else:
        print(error('ERROR: Too many arguments given.'))
    print(error('Usage: pfm <path> <start-directory(OPTIONAL)>'))
    print('Use "pfm --help" for more information.')
    sys.exit(1)
if argvs[0] == '-h' or argvs[0] == '--help':
    print(
        message('USAGE: pfm [path] [start-folder (if you want to start from a specific folder)]'))
    print(
        message('Example: pfm folder,file.ext/folder/file.ext [OPTIONAL] starting_folder/'))
    sys.exit(0)

if len(argvs) == 2:
    if os.path.exists(argvs[1]):
        start_folder = argvs[1]
        os.chdir(start_folder)
        print(f"Start folder: {start_folder}")
    else:
        print('error: start folder does not exist')
        if input('Continue in the current folder? y/[N]').lower() == 'y':
            pass
        else:
            sys.exit(1)
else:
    start_folder = os.getcwd()
    os.chdir(start_folder)

path = argvs[0].split('/')
if len(path) == 1:
    if not os.path.exists(path[0]):
        if detect_file(path[0]):
            with open(path[0], 'w') as f:
                f.write('')
        else:
            os.mkdir(path[0])
    else:
        print(f'"{path[0]}" already exists')
else:
    for i in range(len(path)):
        if detect_multiple_files(path[i]):
            files = path[i].split(',')
            for j in range(len(files)):
                if os.path.exists(files[j]):
                    pass
                else:
                    if detect_file(files[j]):
                        with open(files[j], 'w') as f:
                            f.write('')
                        print(f'{files[j]} is file')
                    else:
                        os.mkdir(files[j])
                        print(f'{files[j]} is folder')
                        paretnt_folder = files[j]
            os.chdir(paretnt_folder)
        else:
            if detect_file(path[i]):
                with open(path[i], 'w') as f:
                    f.write('')
            else:
                os.mkdir(path[i])
                os.chdir(path[i])

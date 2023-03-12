#!/usr/bin/env python

import os
import sys
from colorama import Fore, Back, Style


def error(message):
    return f'{Back.RED}{Fore.WHITE}{message}{Style.RESET_ALL}'


def message(message):
    return f'{Back.BLUE}{Fore.WHITE}{message}{Style.RESET_ALL}'


def detect_file(file):
    return '.' in file


def detect_multiple_files(files):
    return ',' in files


def create_file_or_directory(path):
    if not os.path.exists(path):
        if detect_file(path):
            with open(path, 'w') as f:
                f.write('')
        else:
            os.mkdir(path)


argvs = sys.argv[1:]
num_argv = len(argvs)

if not 0 < num_argv < 3:
    if num_argv == 0:
        print(error('ERROR: No arguments given.'))
    else:
        print(error('ERROR: Too many arguments given.'))
    print(error('Usage: pfm <path> <start-directory(OPTIONAL)>'))
    print('Use "pfm --help" for more information.')
    sys.exit(1)

if argvs[0] in ['-h', '--help']:
    print(message('USAGE: pfm [path] [start-folder (if you want to start from a specific folder)]'))
    print(message('Example: pfm folder,file.ext/folder/file.ext [OPTIONAL] starting_folder/'))
    sys.exit(0)

if num_argv == 2:
    start_folder = argvs[1]
    if not os.path.exists(start_folder):
        print('error: start folder does not exist')
        if input('Continue in the current folder? y/[N]').lower() != 'y':
            sys.exit(1)
    os.chdir(start_folder)

path = argvs[0].split('/')
if len(path) == 1:
    create_file_or_directory(path[0])
    print(f'"{path[0]}" created successfully.')
else:
    for folder in path[:-1]:
        create_file_or_directory(folder)
        os.chdir(folder)
    create_file_or_directory(path[-1])
    print(f'"{path[-1]}" created successfully.')

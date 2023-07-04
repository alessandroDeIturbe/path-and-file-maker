#!/usr/bin/env python

import os
import argparse
from colorama import Fore, Back, Style


def error(message):
    # Format an error message with red background and white text.
    return f'{Back.RED}{Fore.WHITE}{message}{Style.RESET_ALL}'


def message(message):
    # Format a message with blue background and white text.
    return f'{Back.BLUE}{Fore.WHITE}{message}{Style.RESET_ALL}'


def create_file(path):
    # Create a file at the specified path.
    try:
        with open(path, 'w') as f:
            f.write('')
        print(f'File "{path}" created successfully.')
    except Exception as e:
        print(error(f'Error creating file "{path}": {str(e)}'))


def create_directory(path):
    # Create a directory at the specified path.
    try:
        os.mkdir(path)
        print(f'Directory "{path}" created successfully.')
    except Exception as e:
        print(error(f'Error creating directory "{path}": {str(e)}'))


def parse_arguments():
    # Parse command line arguments.
    parser = argparse.ArgumentParser(
        description='Create files or directories.')
    parser.add_argument('path', help='Path of the file or directory to create')
    parser.add_argument('--start-folder', '-s',
                        help='Starting folder path (optional)')
    return parser.parse_args()


def main():
    # Main function to handle the creation of files or directories.
    args = parse_arguments()
    path = args.path
    start_folder = args.start_folder

    if start_folder:
        try:
            os.chdir(start_folder)
        except Exception as e:
            print(
                error(f'Error changing directory to "{start_folder}": {str(e)}'))
            if input('Continue in the current folder? y/[N]').lower() != 'y':
                return

    if ',' in path:
        # Handle creation of files and directories in the same directory.
        segments = path.split(',')
        base_dir = os.path.dirname(segments[0])
        os.makedirs(base_dir, exist_ok=True)
        os.chdir(base_dir)
        for segment in segments:
            file_name, file_ext = os.path.splitext(segment)
            if file_ext:
                create_file(segment)
            else:
                create_directory(segment)
    else:
        if os.path.exists(path):
            print(error(f'Error: "{path}" already exists.'))
            return

        if os.path.isfile(path):
            print(error(f'Error: "{path}" is already an existing file.'))
        else:
            create_file(path)


if __name__ == '__main__':
    main()

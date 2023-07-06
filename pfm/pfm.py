#!/usr/bin/env python

import os
import argparse
from colorama import Fore, Back, Style


def error(message):
    # Formatta un messaggio di errore con sfondo rosso e testo bianco.
    return f'{Back.RED}{Fore.WHITE}{message}{Style.RESET_ALL}'


def message(message):
    # Formatta un messaggio con sfondo blu e testo bianco.
    return f'{Back.BLUE}{Fore.WHITE}{message}{Style.RESET_ALL}'


def create_file(path):
    # Crea un file nel percorso specificato.
    try:
        with open(path, 'w') as f:
            f.write('')
        print(f'File "{path}" creato con successo.')
    except Exception as e:
        print(error(f'Errore durante la creazione del file "{path}": {str(e)}'))


def create_directory(path):
    # Crea una cartella nel percorso specificato.
    try:
        os.makedirs(path, exist_ok=True)
<<<<<<< HEAD
        print(f'Directory "{path}" created successfully.')
=======
        print(f'Cartella "{path}" creata con successo.')
>>>>>>> d40a689 (fixed bugs)
    except Exception as e:
        print(error(f'Errore durante la creazione della cartella "{path}": {str(e)}'))


def parse_arguments():
    # Analizza gli argomenti della riga di comando.
    parser = argparse.ArgumentParser(
<<<<<<< HEAD
        description='Create files or directories.')
    parser.add_argument('paths', nargs='+', help='Paths of the files or directories to create')
=======
        description='Crea file o cartelle.')
    parser.add_argument('paths', help='Percorsi dei file o delle cartelle da creare')
>>>>>>> d40a689 (fixed bugs)
    parser.add_argument('--start-folder', '-s',
                        help='Percorso della cartella di partenza (opzionale)')
    return parser.parse_args()


def main():
    # Funzione principale per gestire la creazione di file o cartelle.
    args = parse_arguments()
<<<<<<< HEAD
    paths = args.paths
=======
    paths = args.paths.split(',')
>>>>>>> d40a689 (fixed bugs)
    start_folder = args.start_folder

    if start_folder:
        try:
            os.chdir(start_folder)
        except Exception as e:
            print(
                error(f'Errore durante il cambio della directory a "{start_folder}": {str(e)}'))
            if input('Continuare nella cartella corrente? y/[N]').lower() != 'y':
                return

    for path in paths:
<<<<<<< HEAD
        base_dir = os.path.dirname(path)
        if base_dir:
            os.makedirs(base_dir, exist_ok=True)
        if os.path.isfile(path):
=======
        if '/' in path:
            segments = path.split('/')
            for segment in segments[:-1]:
                create_directory(segment)
                os.chdir(segment)
            create_file(segments[-1])
        else:
>>>>>>> d40a689 (fixed bugs)
            create_file(path)
        else:
            create_directory(path)


if __name__ == '__main__':
    main()

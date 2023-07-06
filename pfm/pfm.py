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
        print(f'Cartella "{path}" creata con successo.')
    except Exception as e:
        print(error(f'Errore durante la creazione della cartella "{path}": {str(e)}'))


def parse_arguments():
    # Analizza gli argomenti della riga di comando.
    parser = argparse.ArgumentParser(
        description='Crea file o cartelle.')
    parser.add_argument('paths', help='Percorsi dei file o delle cartelle da creare')
    parser.add_argument('--start-folder', '-s',
                        help='Percorso della cartella di partenza (opzionale)')
    return parser.parse_args()


def main():
    # Funzione principale per gestire la creazione di file o cartelle.
    args = parse_arguments()
    paths = args.paths.split(',')
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
        if '/' in path:
            segments = path.split('/')
            for segment in segments[:-1]:
                create_directory(segment)
                os.chdir(segment)
            create_file(segments[-1])
        else:
            create_file(path)


if __name__ == '__main__':
    main()

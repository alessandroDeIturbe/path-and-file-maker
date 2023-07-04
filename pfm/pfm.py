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
        print(
            error(f'Errore durante la creazione del file "{path}": {str(e)}'))


def create_directory(path):
   # Crea una cartella nel percorso specificato.
    try:
        os.mkdir(path)
        print(f'Cartella "{path}" creata con successo.')
    except Exception as e:
        print(
            error(f'Errore durante la creazione della cartella "{path}": {str(e)}'))


def parse_arguments():
   # Analizza gli argomenti della riga di comando.
    parser = argparse.ArgumentParser(
        description='Crea file o cartelle.')
    parser.add_argument(
        'path', help='Percorso del file o della cartella da creare')
    parser.add_argument('--start-folder', '-s',
                        help='Percorso della cartella di partenza (opzionale)')
    return parser.parse_args()


def main():
   # Funzione principale per gestire la creazione di file o cartelle.
    args = parse_arguments()
    path = args.path
    start_folder = args.start_folder

    if start_folder:
        try:
            os.chdir(start_folder)
        except Exception as e:
            print(
                error(f'Errore durante il cambio della directory a "{start_folder}": {str(e)}'))
            if input('Continuare nella cartella corrente? y/[N]').lower() != 'y':
                return

    if ',' in path:
        # Gestisci la creazione di file e cartelle nella stessa directory.
        segments = path.split(',')
        base_dir = os.path.dirname(segments[0])
        os.makedirs(base_dir, exist_ok=True)
        os.chdir(base_dir)
        for segment in segments:
            if os.path.isfile(segment):
                print(error(f'Errore: "{segment}" è già un file esistente.'))
            else:
                create_directory(segment)
    else:
        if os.path.exists(path):
            print(error(f'Errore: "{path}" esiste già.'))
            return

        if os.path.isfile(path):
            print(error(f'Errore: "{path}" è già un file esistente.'))
        else:
            create_file(path)


if __name__ == '__main__':
    main()

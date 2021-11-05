import os

wd = ''

while wd == '':
    wd = input('Enter the path of the working directory: ')

    if wd == '':
        wd = os.getcwd()

    if os.path.exists(wd):
        print('exists')
        os.chdir(wd)
        print(os.getcwd())

    else:
        print('not exists')

    pass

with open("file_formats.txt", 'r') as f:
    text = f.read().split(',')

print(text)

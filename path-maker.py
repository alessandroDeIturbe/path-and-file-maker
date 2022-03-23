import os
import sys

argvs = sys.argv
argvs.pop(0)
    
if len(argvs) == 0:
    print("ERROR: No arguments")
    print('Insert the path of the folders/file you want to create (REMEMBER, THE ROOT DIRECTORY IS THE CURRENT DIRECTORY)')
    print('Example: /folder1/folder2/folder3/file.txt')
    sys.exit(1)
if len(argvs) > 1:
    print("ERROR: Too may argumets")
    print('Insert the path of the folders/file you want to create (REMEMBER, THE ROOT DIRECTORY IS THE CURRENT DIRECTORY)')
    print('Example: /folder1/folder2/folder3/file.txt')
    sys.exit(1)

path = argvs[0].split('/')
print(path)

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
    
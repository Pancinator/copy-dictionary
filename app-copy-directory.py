import shutil
import argparse
import os

parser = argparse.ArgumentParser(description='Copy all file structure from one folder to new one.')
parser.add_argument('-c', '--copy', dest='copy', nargs='+',
                    help='[path to source folder] [path to destination folder]')
try:
    args = parser.parse_args()
    new_folder_path = shutil.copytree(args.copy[0], args.copy[1])
    print(f'folder {args.copy[0]} was copied to {args.copy[1]}')
    print(new_folder_path)

    with(open(new_folder_path+'\README.txt', 'w')) as readme:
        readme.write(f'this Folders structure was copied from {args.copy[0]}')
except:
    print('File already exist. Please choose another destination path!')




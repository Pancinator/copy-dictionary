import shutil
import argparse
import os

parser = argparse.ArgumentParser(description='Manipulating with file structures.')
parser.add_argument('-c', '--copy', dest='copy', nargs='+',
                    help='[path to source folder] [path to destination folder]'
                         'The source folder will be copied and whole structure will be added to new destination folder.'
                         'If the destination folder does not exist, it will be created.')


parser.add_argument('-m', '--move', dest='move', nargs='+',
                    help='[path to source folder] [path to destination folder]'
                         'The source folder will be moved to new destination folder, origin source folder will be deleted'
                         'If the destination folder does not exist, it will be created.')

args = parser.parse_args()
#Copy argument usage
def copy_directory():
    try:
        new_folder_path = shutil.copytree(args.copy[0], args.copy[1])
        print(f'folder {args.copy[0]} was copied to {args.copy[1]}')
        print(new_folder_path)

        with(open(new_folder_path+'\README.txt', 'w')) as readme:
                readme.write(f'this Folders structure was copied from {args.copy[0]}'
                             f'The copy action was processed by copy-directory.py from pancakefactory.com'))
    except:
        print('Some problem occurs, please be sure that the paths of directories are correct')


#Move argument usage
def move_directory():
    try:
        new_folder_path = shutil.move(args.move[0], args.move[1])
        print(f'folder {args.move[0]} was moved to {args.move[1]}')
        print(new_folder_path)
        #addinf readMe file with some informations
        with(open(new_folder_path+'\README.txt', 'w')) as readme:
                readme.write(f'this Folders structure was moved from {args.move[0]}'
                             f'The move action was processed by copy-directory.py from pancakefactory.com')
    except:
        print('Some problem occurs, please be sure that the paths of directories are correct')


if args.copy != [] and args.copy != None:
    copy_directory()
elif args.move != []:
    move_directory()

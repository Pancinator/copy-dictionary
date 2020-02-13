import shutil
import argparse
import os
import shutil
import hashlib, os
from pathlib import Path

parser = argparse.ArgumentParser(description='Manipulating with file structures.')
parser.add_argument('-c', '--copy', dest='copy', nargs='+',
                    help='[path to source folder] [path to destination folder]'
                         'The source folder will be copied and whole structure will be added to new destination folder.'
                         'If the destination folder does not exist, it will be created.')


parser.add_argument('-m', '--move', dest='move', nargs='+',
                    help='[path to source folder] [path to destination folder]'
                         'The source folder will be moved to new destination folder, origin source folder will be deleted'
                         'If the destination folder does not exist, it will be created.')

parser.add_argument('-s', '--sha', dest='sha', nargs='+',
                    help='[path to folder]'
                         'Create and md5 hash of the selected file or folder')

parser.add_argument('-cs', '--checksha', dest='csha', nargs='+',
                    help='[path to folder]'
                         'Create and md5 hash of the selected file or folder')

#Usefull variables initialization
args = parser.parse_args()
#directory = args.sha[0]
directory = args.csha[0]
home_directory = str(Path.home())

#Copy argument usage
def copy_directory():
    try:
        new_folder_path = shutil.copytree(args.copy[0], args.copy[1])
        print(f'folder {args.copy[0]} was copied to {args.copy[1]}')
        print(new_folder_path)

        with(open(new_folder_path+'\README.txt', 'w')) as readme:
                readme.write(f'this Folders structure was copied from {args.copy[0]}'
                             f'The copy action was processed by copy-directory.py from pancakefactory.com')
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

#Creating an md5 for the selected directory
def craete_md5(directory, verbose=0):
    sha_hash = hashlib.md5()
    if not os.path.exists(directory):
        print('Directory or file does not exist')
        return
    try:
        for root, dirs, files in os.walk(directory):
            for names in files:
                if verbose == 1:
                    print('Hashing', names)
                filepath = os.path.join(root,names)
                with(open(filepath, 'rb')) as file:
                    #file_content = file.read()
                    while True:
                        buf = file.read(4096)
                        if not buf : break
                        sha_hash.update(buf)
    except:
        import traceback
    # Print the stack traceback
        traceback.print_exc()
        return -2

    with(open(home_directory+'\md5-hashes.txt', 'w')) as hash_file:
        hash_file.write(directory + ' ' + sha_hash.hexdigest())
    return sha_hash.hexdigest()


def check_md5(directory):
    # Creating the dictionary of directories and its hashes
    print('hello')
    hash_dict = {}
    with(open(home_directory+'\md5-hashes.txt')) as hash_file:
        for line in hash_file:
            (key, value) = line.split()
            hash_dict[str(key)] = value

    print(hash_dict.keys())
    # if directory in hash_dict.keys():
    #    print("Hash for this directory is already created")
    # else:
    #    craete_md5(directory, 1)

    if directory not in hash_dict.keys():
        print('Hash was not already created')
        return

    actual_hash = craete_md5(directory, 1)
    stored_hash = hash_dict[directory]

    if actual_hash != stored_hash:
        print('Your file was corrupted!')

    else:
        print("Files was not corrupted")





if args.copy != [] and args.copy != None:
    copy_directory()
elif args.move != [] and args.move != None:
    move_directory()
elif args.sha !=  [] and args.sha != None:
    print(craete_md5(directory, 1))
elif args.csha != [] and args.csha is not None:
    check_md5(directory)
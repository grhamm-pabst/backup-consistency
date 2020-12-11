import os
import sys
import colorama
from colorama import Fore, Style

def iterate_in_path(path):
    for (dirpath, dirnames, filenames) in os.walk(path):
        files=[]
        folders=[]
        files.extend(filenames)
        folders.extend(dirnames)
        return (folders, files)

def diff(folders_origin, folders_backup, files_origin, files_backup):
    return (list(list(set(folders_origin)-set(folders_backup)) + list(set(folders_backup)-set(folders_origin)))), (list(list(set(files_origin)-set(files_backup)) + list(set(files_backup)-set(files_origin)))) 

def walk_in_path(path_backup, path_origin):

    folders_origin, files_origin = iterate_in_path(path_origin)
    folders_backup, files_backup = iterate_in_path(path_backup)

    diff_folders, diff_files = diff(folders_origin, folders_backup, files_origin, files_backup)
    if len(diff_files) > 0 or len(diff_folders) > 0:
        raise Exception("{0}WARNING: {1}Different files or folders in PATHS: {2}\n{3}\n{4}".format(Fore.RED, Fore.LIGHTRED_EX, Fore.YELLOW, path_origin, path_backup))
    else:
        for dirname in folders_origin:
            next_path_backup = "{0}\\{1}".format(path_backup, dirname)
            next_path_origin = "{0}\\{1}".format(path_origin, dirname)
            walk_in_path(next_path_backup, next_path_origin)

def main():
    colorama.init()
    print(Fore.CYAN + "Type the PATH to the first folder: " + Style.RESET_ALL, end="")
    path_origin_input = input()
    print(Fore.CYAN + "Type the PATH to the second folder: " + Style.RESET_ALL, end="")
    path_backup_input = input()

    try:
        walk_in_path(path_origin_input, path_backup_input)
        print(Fore.GREEN + "Finished without no errors" + Style.RESET_ALL)
    except Exception as e:
        print(e)

main()
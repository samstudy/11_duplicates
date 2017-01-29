import os
import itertools
import argparse
from collections import defaultdict


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder_for_check', help='Put a path where need to check')
    arg = parser.parse_args()
    return arg.folder_for_check


def get_files_information(folder_for_look):
    files_size = []
    files_name = []
    files_path = []
    for dirs, subdirs, files in os.walk(folder_for_check):
        files_name.extend(os.path.join(filename) for filename in files)
        files_path.extend(os.path.join(dirs,filename) for filename in files)
        files_size.extend(os.path.getsize(filename) for filename in files)
    name_and_size_store = zip(files_name, files_size)
    basic_store = zip(name_and_size_store,files_path)
    return basic_store


def get_duplicated_files(files_info):
    filename_and_size_to_paths = {}
    for filename_size, filepath in files_info:
        filename_and_size_to_paths.setdefault(filename_size, []).append(filepath)
    duplicates = {filename: uniq_files for filename, uniq_files in filename_and_size_to_paths.items() if len(uniq_files) > 1}
    for name_size,path in duplicates.items():
        print('This file-->', name_size[0],'has duplic', 'which occupy',(name_size[1])/1024,'Mb','and locates here',path)


if __name__ == '__main__':
    folder_for_check = get_args()
    if not os.path.isdir(folder_for_check):
        print('There is none check for find out')
        exit()
    files_info = get_files_information(folder_for_check)
    get_duplicated_files(files_info)
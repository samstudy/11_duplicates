import os
import itertools
from collections import defaultdict


def get_usefull_information(folder_for_check):
    files_size = []
    files_name = []
    files_path = []
    for dirs, subdirs, files in os.walk(folder_for_check):
        files_name.extend(os.path.join(filename) for filename in files)
        files_path.extend(os.path.join(dirs,filename) for filename in files)
        files_size.extend(os.path.getsize(filename) for filename in files)
    name_and_size_store = list(zip(files_name, files_size))
    basic_store = list(zip(name_and_size_store,files_path))
    return basic_store


if name == '__main__':
    files_info = get_usefull_information('put_a_path')
filename_and_size_to_paths = {}
for filename_size, filepath in files_info:
    filename_and_size_to_paths.setdefault(filename_size, []).append(filepath)
duplicates = {filename: uniq_files for filename, uniq_files in filename_and_size_to_paths.items() if len(uniq_files) > 1}
for name_size,path in duplicates.items():
    print('This file-->', name_size[0],'has duplic', 'which occupy',(name_size[1])/1024,'Mb','and locates here',path)
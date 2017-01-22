import os
import itertools
import filecmp


def compare_files(file1, file2):
    if  filecmp.cmp(file1 ,file2):
        return True
    return False


def get_duplicate_files(folder_for_check):
    duplic_store = []
    path_name = []
    for dirs, subdirs, files in os.walk(folder_for_check):
        path_name.extend(os.path.join(dirs,filename) for filename in files)
    for file1, file2 in itertools.combinations(path_name, 2):
        if compare_files(file1,file2):
            duplic_store.extend([file1, file2])
    return duplic_store


if __name__ == '__main__':
    duplic_files= get_duplicate_files('input_a_path')
    print('Was found those identical files:')
    for files in duplic_files:
        print(files)
    
import os
import itertools


def get_duplicate_files(folder_for_check):
    duplic_store = []
    path_name = []
    for dirs, subdirs, files in os.walk(folder_for_check):
        path_name.extend(os.path.join(dirs,filename) for filename in files)
    for file1, file2 in itertools.combinations(path_name, 2):
        fname, fname2 = os.path.basename(file1), os.path.basename(file2),
        fsize, fsize2 = os.path.getsize(file1), os.path.getsize(file2)
        if fname == fname2 and fsize == fsize2:
            duplic_store.extend([file1, file2])
    return duplic_store


if __name__ == '__main__':
    duplic_files= get_duplicate_files('input_a_path')
    print('Was found those identical files:')
    for files in duplic_files:
        print(files)
    
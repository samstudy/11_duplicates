import os 
import sys
import hashlib


def get_duplicate_files(folder_for_check):
    duplicates = {}
    for dirs, subdirs, files in os.walk(folder_for_check):
        print('Scanning %s...' % dirs)
        for filename in files:
            path = os.path.join(dirs, filename)
            file_hash = get_hashfile(path)
            if file_hash in duplicates:
                duplicates[file_hash].append(path)
            else:
                duplicates[file_hash] = [path]
    return duplicates


def get_hashfile(path):
    with open(path,encoding='utf-8', errors='ignore') as file_handler:
        hash_object = hashlib.md5()
        buf = file_handler.read()
        while len(buf) > 0:
            hash_object.update(buf.encode('utf-8'))
            buf = file_handler.read()
        return hash_object.hexdigest()


def are_files_duplicates(path):
    duplicate = get_duplicate_files(path)
    results = list(filter(lambda x: len(x) > 1, duplicate.values()))
    if len(results) > 0:
        print('The following files are identical:')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
    else:
        print('No duplicate files found.')


if __name__ == '__main__':
    are_files_duplicates('input_a_path')
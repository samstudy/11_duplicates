import os 
import sys
import hashlib



def get_identical_files(folder_for_check):
    identical_files = {}
    for dirs, subdirs, files in os.walk(folder_for_check):
        for filename in files:
            path = os.path.join(dirs, filename)
            file_hash = get_hash_of_files(path)
            if file_hash in identical_files:
                identical_files[file_hash].append(path)
            else:
                identical_files[file_hash] = [path]
    return identical_files


def get_hash_of_files(path):
    block_size = 64
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(block_size)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(block_size)
    afile.close()
    return hasher.hexdigest()


def show_identical_files(dict):
    results = list(filter(lambda x: len(x) > 1, dict.values()))
    if len(results) > 0:
        for result in results:
            print('This files are identical:')
            for subresult in result:
                print('\t\t%s' % subresult)
    else:
        print('No duplicate files found.')


if __name__ == '__main__':
    identical_files = get_identical_files('put_a_folder_path')
    show_identical_files(identical_files)



  
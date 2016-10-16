import os, sys
import hashlib


block_size = 64

def duplic(basicfolder):
    dups = {}
    for dirs, subdirs, files in os.walk(basicfolder):
        print('Scanning %s...' % dirs)
        for filename in files:
            path = os.path.join(dirs, filename)
            file_hash = hashfile(path)
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups

def hashfile(path):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(block_size)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(block_size)
    afile.close()
    return hasher.hexdigest()

def results(dict):
    results = list(filter(lambda x: len(x) > 1, dict.values()))
    if len(results) > 0:
        print('The following files are identical.')
        print('___________________')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('___________________')
 
    else:
        print('No duplicate files found.')


if __name__ == '__main__':
    data = duplic('/home/trash/')
    print  (results(data))
  
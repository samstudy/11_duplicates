import os 


def get_name_size_of_files(folder_for_check):
    name_store = []
    size_store = []
    for dirs, subdirs, files in os.walk(folder_for_check):
        name_store.extend(os.path.join(filename) for filename in files)
        size_store.extend(os.path.getsize(filename) for filename  in files) 
    basic_store = list(zip(name_store, size_store)) 
    return basic_store


if __name__ == '__main__':
    all_files = get_name_size_of_files('put a path')
    duplicates = [subject for subject in all_files if all_files.count(subject) > 1]
    print('Was found those identical files:')
    for duplicate in duplicates:
        print('name of file:', duplicate[0],'size of file:', duplicate[1])
    
    
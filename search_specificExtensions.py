import os

def search(dirname):
    try:
        filename_list = os.listdir(dirname)
        for filename in filename_list:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.vtt': 
                    print(full_filename)
    except PermissionError:
        pass

search("../")
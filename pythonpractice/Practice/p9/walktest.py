import os

for folder_name, sub_folder, filenames in os.walk('.\\'):
    print(folder_name)
    for folder in sub_folder:
        print('sub_folder is :' + folder)
    for files in filenames:
        print('files is :' + files)

    print(' ')
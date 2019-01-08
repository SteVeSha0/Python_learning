# 针对一个工作文件夹，防止文件丢失，用创建zip文件的方法进行备份，
# 每次变化运行程序会按照编号建立新的zip文件

import zipfile, os

def backup_to_zip(folder):
    
    folder = os.path.abspath(folder)

    number = 1

    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number = number + 1
    
    #TODO：创建zip文件
    print('creating %s ....' %(zip_filename))
    backupZip = zipfile.ZipFile(zip_filename , 'w')

    #TODO：遍历需要备份的目录

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s ...' % (foldername))
        backupZip.write(foldername)
        print(subfolders)
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
        backupZip.close

    print('Done!')

backup_to_zip('D:\\123')



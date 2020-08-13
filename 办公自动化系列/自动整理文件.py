import os
import shutil
import glob

#下面两个路径需要自行修改
mkdir_path = r'C:\Users\chenx\文件夹分类'
goal_dir = r'C:\xxxxxxxx'

if not os.path.exists(mkdir_path):
    os.mkdir(mkdir_path)

file_num = 0
dir_num = 0

for file in glob.glob(f'{goal_dir}/**/*', recursive=True):
    if os.path.isfile(file):
        filename = os.path.basename(file)
        if '.' in filename:
            suffix = filename.split('.')[-1]
        else:
            suffix = 'others'
        if not os.path.exists(f'{mkdir_path}/{suffix}'):
            os.mkdir(f'{mkdir_path}/{suffix}')
            dir_num += 1
        shutil.copy(file, f'{mkdir_path}/{suffix}')
        file_num += 1

print(f'整理完成，有{file_num}个文件分类到了{dir_num}个文件夹中')

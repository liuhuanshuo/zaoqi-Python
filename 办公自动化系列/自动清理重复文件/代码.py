import os
import glob
import filecmp

dir_path = r'C:\xxxx'

file_lst = []

for i in glob.glob(dir_path + '/**/*', recursive=True):
    if os.path.isfile(i):
        file_lst.append(i)

for x in file_lst:
    for y in file_lst:
        if x != y and os.path.exists(x) and os.path.exists(y):
            if filecmp.cmp(x, y):
                os.remove(y)

import glob
import os
import gzip
import tarfile
import zipfile
import rarfile
import time

path = r'C:\xxxx\download'
file_lst = glob.glob(path + '/*')
filename_lst = [os.path.basename(i) for i in file_lst]

def ungz(filename):
    filename = filename[:-3]
    gz_file = gzip.GzipFile(filename)
    with open(filename, "w+") as file:
        file.write(gz_file.read())
    return filename

def untar(filename):
    tar = tarfile.open(filename)
    names = tar.getnames()
    if not os.path.isdir(filename + "_dir"):
        os.mkdir(filename + "_dir")
    for name in names:
        tar.extract(name, filename + "_dir/")
    tar.close()

def unzip(filename):
    zip_file = zipfile.ZipFile(filename)
    if not os.path.isdir(filename + "_dir"):
        os.mkdir(filename + "_dir")
    for names in zip_file.namelist():
        zip_file.extract(names, filename + "_dir/")
    zip_file.close()

def unrar(filename):
    rar = rarfile.RarFile(filename)
    if not os.path.isdir(filename + "_dir"):
        os.mkdir(filename + "_dir")
    os.chdir(filename + "_dir")
    rar.extractall()
    rar.close()

def unzip_files():
    for filename in filename_lst:
        if '.' in filename:
            suffix = filename.split('.')[-1]
            if suffix == 'gz':
                new_filename = ungz(filename)
                os.remove(filename)
                if new_filename.split('.')[-1] == 'tar':
                    untar(new_filename)
                    os.remove(new_filename)
            if suffix == 'tar':
                untar(filename)
                os.remove(filename)
            if suffix == 'zip':
                unzip(filename)
                os.remove(filename)
            if suffix == 'rar':
                unrar(filename)
                os.remove(filename)

while True:
    unzip_files()
    time.sleep(5)

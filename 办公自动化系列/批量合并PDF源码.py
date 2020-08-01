import os
from PyPDF2 import PdfFileReader, PdfFileWriter


def GetFileName(dir_path):
    file_list = [os.path.join(dirpath, filesname)
                 for dirpath, dirs, files in os.walk(dir_path)
                 for filesname in files]
    return file_list


def MergePDF(dir_path, file_name):
    output = PdfFileWriter()
    outputPages = 0
    file_list = GetFileName(dir_path)
    for pdf_file in file_list:
        print("文件：%s" % pdf_file.split('\\')[-1], end=' ')
        # 读取PDF文件
        input = PdfFileReader(open(pdf_file, "rb"))
        # 获得源PDF文件中页面总数
        pageCount = input.getNumPages()
        outputPages += pageCount
        print("页数：%d" % pageCount)
        # 分别将page添加到输出output中
        for iPage in range(pageCount):
            output.addPage(input.getPage(iPage))
    print("\n合并后的总页数:%d" % outputPages)
    # 写入到目标PDF文件
    print("PDF文件正在合并，请稍等......")
    with open(os.path.join(dir_path, file_name), "wb") as outputfile:
        # 注意这里的写法和正常的上下文文件写入是相反的
        output.write(outputfile)
    print("PDF文件合并完成")


if __name__ == '__main__':
    # 设置存放多个pdf文件的文件夹
    dir_path = r'C:\Scientific Research\Knowladge\Ophthalmology\Chinese Ophthalmology'
    # 目标文件的名字
    file_name = "中华眼科学（第3版）合并版.pdf"
    MergePDF(dir_path, file_name)

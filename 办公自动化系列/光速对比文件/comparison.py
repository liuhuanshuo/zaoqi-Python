'''
公众号：早起Python
作者：刘早起
version：1.0
'''
###对比Excel，请在Excel文件的存放目录下执行本代码
import pandas as pd
import numpy as np
df1 = pd.read_excel('data1.xlsx')
df2 = pd.read_excel('data2.xlsx')
comparison_values = df1.values == df2.values
rows,cols=np.where(comparison_values==False)
for item in zip(rows,cols):
    df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]],df2.iloc[item[0], item[1]])
df1.to_excel('diff.xlsx',index=False,header=True)
print('对比Excel保存成功')

####对比Word，请在word存放目录下执行
####请确保两个word仅有文字不同，段落、标点出现不同将会导致报错
####仅在Python3.6版本以上可以运行，否则f表达式部分会报错
from docx import Document
import re, sys
def getText(wordname):
    '''
    提取文字
    '''
    d = Document(wordname)
    texts = []
    for para in d.paragraphs:
        texts.append(para.text)
    return texts

def is_Chinese(word):
    '''
    识别中文
    '''
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def msplit(s, seperators = ',|\.|\?|，|。|？|！|、'):
    '''
    根据标点符号分句
    '''
    return re.split(seperators, s)

def readDocx(docfile):
    '''
    读取文档
    '''
    print(f"======正在读取{docfile}======")
    paras = getText(docfile)
    segs = []
    for p in paras:
        temp = []
        for s in msplit(p):
            if len(s) > 2:
                temp.append(s.replace(' ', ""))
        if len(temp) > 0:
            segs.append(temp)
    return segs


def comparsion(doc1,doc2,p,s):
    if doc1 == doc2:
        print('两个word完全一致')
    else:
        if doc1[p][s] != doc2[p][s]:
            print(f"第{p+1}段，第{s+1}句不相同: {doc1[p][s]} ----> {doc2[p][s]}")


doc1 = readDocx('word1.docx')
doc2 = readDocx('word2.docx')

for p in range(len(doc1)):
    for s in range(len(doc1[p])):
        comparsion(doc1,doc2,p,s)
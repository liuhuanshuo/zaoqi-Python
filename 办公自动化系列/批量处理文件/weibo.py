'''
公众号：早起Python
作者：刘早起
'''


from pathlib import Path
import re
import pandas as pd
import os

# 请将热搜数据文件夹保存至桌面
#如果执行失败说明Path路径手动设置为自己的桌面对应路径
path = os.path.join(os.path.expanduser("~"), 'Desktop') + '/热搜数据/'

p = Path(path)  # 初始化构造Path对象

FileList = list(p.glob("**/*.md"))  # 得到所有的markdown文件

filelist = list(filter(lambda x: str(x).find(
    "23点") >= 0, FileList))  # 去重，每天保留一条数据

df = pd.DataFrame(columns=['时间', '热搜', '热度'])
for file in filelist:
    with open(file) as f:
        lines = f.readlines()
        lines = [i.strip() for i in lines]  # 去除空字符
        data = list(filter(None, lines))
        del data[0]
        data = data[0:100]
        date = re.findall('年(.+)2', str(file))[0]
        content = data[::2]  # 奇偶分割
        rank = data[1::2]
        # 提取内容与排名
        for i in range(len(content)):
            content[i] = re.findall('、(.+)', content[i])[0]
        for i in range(len(rank)):
            rank[i] = re.findall(' (.+)', rank[i])[0]

        dict = {'热搜': content,
                '热度': rank}
        df1 = pd.DataFrame(dict)
        df1.insert(0, '时间', date)
        df = df.append(df1)
df = df.sort_values(by="时间", ascending=True).reset_index(drop=True)

df.to_excel('热搜数据.xlsx')
print('文件已生成')

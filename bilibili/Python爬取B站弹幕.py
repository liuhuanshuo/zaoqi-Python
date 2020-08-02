'''
作者：刘早起
公众号：早起Python
Version：1.0
Python：3.6+
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
from tqdm import trange


def get_danmu(url_list, name):
    '''
    下载弹幕存至本地txt
    请先登录B站之后F12获取自己的Cookie
    '''
    headers = {"cookie": "替换为自己的Cookie",
               "origin": "https://www.bilibili.com",
               "referer": "https://www.bilibili.com/video/BV1gW411b735",
               "sec-fetch-dest": "empty",
               "sec-fetch-mode": "cors",
               "sec-fetch-site": "same-site",
               "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

    file = open(f"{name}.txt", 'w')

    for i in trange(len(url_list)):
        url = url_list[i]
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text)
        data = soup.find_all("d")
        danmu = [data[i].text for i in range(len(data))]
        for items in danmu:
            file.write(items)
            file.write("\n")
        time.sleep(2)

    file.close()


def get_url(oid, start, end):
    '''
    获取指定日期的弹幕
    oid：视频oid
    start，end：起止日期
    '''
    url_list = []

    date_list = [i for i in pd.date_range(start, end).strftime('%Y-%m-%d')]

    for date in date_list:

        url = f"https://api.bilibili.com/x/v2/dm/history?type=1&oid={oid}&date={date}"
        url_list.append(url)

    return url_list


if __name__ == "__main__":
    #需要手动设置爬取弹幕的起止日期！
    #oid获取说明详见公众号：早起Python文章
    start = '7/6/2020'
    end = '7/30/2020'
    name = input("请输入视频名称")
    oid = input("请输入对应视频oid")
    # print("========正在爬取弹幕=========")
    url_list = get_url(oid, start, end)
    get_danmu(url_list, name)
    print(f"{name}.txt已生成")

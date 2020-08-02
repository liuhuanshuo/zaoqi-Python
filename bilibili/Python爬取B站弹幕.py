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
    '''
    headers = {"cookie": "LIVE_BUVID=AUTO9915517606726630; im_notify_type_180143162=0; stardustvideo=1; CURRENT_FNVAL=16; fts=1554365582; rpdid=|(u||uuJuulu0J'ullY)Y|~Ru; _uuid=B9AB21E1-2195-504F-0F06-F6F422E3971C95847infoc; laboratory=1-1; DedeUserID=180143162; DedeUserID__ckMd5=6a199ea2f7d9ed69; SESSDATA=1362c3b2%2C1605078424%2Ccd9c2*51; bili_jct=33acf2c74709c63d0792cbfbe4e46e1e; sid=4ju11ogf; bsource=search_baidu; buvid3=2669E417-F7AC-4AFA-8145-00CAC77F870D138383infoc; PVID=1; bfe_id=463d72211d8612b93e1aed57df2ab3d4",
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

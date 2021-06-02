import requests
from lxml import html
import json
import random
from hashlib import md5
import time
from openpyxl import Workbook

wb = Workbook()
sheet = wb.active
header = ['序号', '题目', '题目(译)', '摘要', '摘要(译)']
sheet.append(header)
path = r'C:\Users\chenx\Desktop' # 希望保存文件的路径

def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

def Baidu_translate(query):
    # Set your own appid/appkey.
    appid = 'xxx'
    appkey = 'xxx'

    from_lang = 'en'
    to_lang = 'zh'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path
    try:
        salt = random.randint(32768, 65536)
        sign = make_md5(appid + query + str(salt) + appkey)
        # Build request
        headers_new = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}
        # Send request
        r = requests.post(url, params=payload, headers=headers_new)
        result = r.json()['trans_result'][0]['dst']
        return result
    except:
        return '翻译出错'

num = 0
keyword = 'GAN+fundus'
url_init = r'https://dl.acm.org/action/doSearch?AllField='
url =url_init + keyword
html_data = requests.get(url).text
selector = html.fromstring(html_data)
articles = selector.xpath('//*[@id="pb-page-content"]/div/main/div[1]/div/div[2]/div/ul/li')

for article in articles:
    num += 1
    url_new = 'https://dl.acm.org' + article.xpath('div[2]/div[2]/div/h5/span/a/@href')[0]
    html_data_new = requests.get(url_new).text
    selector_new = html.fromstring(html_data_new)

    title = selector_new.xpath('//*[@id="pb-page-content"]/div/main/div[2]/article/div[1]/div[2]/div/div[2]/h1/text()')[0]
    abstract = selector_new.xpath('//div[@class="abstractSection abstractInFull"]/p/text()')[0]

    title = 'Title: ' + title
    translated_title = Baidu_translate(title)
    print(title)
    print(translated_title)
    time.sleep(1)

    abstract = 'Abstract: ' + abstract
    translated_abstract = Baidu_translate(abstract)
    print(abstract)
    print(translated_abstract)
    time.sleep(1)

    print('-' * 20)
    sheet.append([num, title, translated_title, abstract, translated_abstract])

wb.save(path + r'\文献输出.xlsx')
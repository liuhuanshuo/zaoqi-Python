import threading
import time
from playsound import playsound
import pyttsx3
import random
import warnings
warnings.filterwarnings("ignore")


engine = pyttsx3.init()


def bgm():

    playsound('music.mp3')


t_bgm = threading.Thread(target=bgm)  # 后台播放bgm
t_bgm.start()

word1 = ['Python、', 'Java、', '数据库、', '.Net、', 'GO、', 'html、', 'C++、', 'web、']
word2 = ['前端、', '后端、', '运维、', '开发、', '测试、', '产品、', '算法、', '全栈、', '工程师、']
word3 = ['程序员、', '单身、', '写代码、', '码农、', 'Bug、', '秃头、',
         '九九六、', '加班、', '头发、', '年终奖、', '女朋友、', '暴富、']
word4 = ['我、', '他没', '他要''这', '那', '没了', '不过', '许我一场', '最后不过', '后来', '而']

a = random.choice(word1) + random.choice(word2) + random.choice(word2) + \
    random.choice(word4) + random.choice(word3)
b = random.choice(word1) + random.choice(word2) + random.choice(word2) + \
    random.choice(word4) + random.choice(word3)
c = random.choice(word1) + random.choice(word2) + random.choice(word2) + \
    random.choice(word4) + random.choice(word3)
d = random.choice(word1) + random.choice(word2) + random.choice(word2) + \
    random.choice(word4) + random.choice(word3)

print(a)
print(b)
print(c)
print(d)

msg = a + b + c + d

time.sleep(2)
engine.say(msg)
engine.runAndWait()

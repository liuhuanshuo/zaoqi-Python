'''
@author: liuzaoqi
@wechat: zaoqi-python
@software: PyCharm
@time: 2020/09/08
@version: 1.0
'''
from pynput.mouse import Button, Controller
import time
from pynput.keyboard import Key
from pynput.keyboard import Controller as Controller1
import pyperclip

mouse = Controller()
keyboard = Controller1()


def click_wechat():
    '''
    点击微信图标
    '''
    mouse.position = (1056.6328125, 5.35546875)
    time.sleep(3)
    mouse.press(Button.left)
    mouse.release(Button.left)


def get_id():
    '''
    获取微信号
    '''
    mouse.position = (1478.1640625, 399.75)
    time.sleep(2)
    mouse.press(Button.left)
    mouse.release(Button.left)

    # 点击选中文本
    mouse.position = (1235.55078125, 318.26171875)
    time.sleep(1)
    mouse.click(Button.left, 2)

    with keyboard.pressed(Key.cmd):
        keyboard.press('c')
        keyboard.release('c')
        time.sleep(1)

    wechatid = pyperclip.paste()
    print(f"微信号{wechatid}疑似广告号" if len(wechatid) > 20 else f"微信号{wechatid}不是广告号")


def move_mouse():
    '''
    移动鼠标至下一微信号位置
    '''
    mouse.position = (1673.47265625, 332.20703125)
    mouse.press(Button.left)
    mouse.position = (1675.05859375, 337.9453125)
    mouse.release(Button.left)


click_wechat()
while True:
    get_id()
    move_mouse()

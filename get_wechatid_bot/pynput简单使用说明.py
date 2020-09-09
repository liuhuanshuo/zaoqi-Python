from pynput.mouse import Button, Controller
import time 

mouse = Controller()
print(mouse.position)
time.sleep(3)
print('鼠标现在的位置在 {0}'.format(mouse.position))


#移动位置
mouse.position = (277, 645)
print('鼠标移动到 {0}'.format(mouse.position))

#鼠标移动（x,y）个距离
mouse.move(5, -5)
print(mouse.position)

#点击
mouse.press(Button.left)
mouse.release(Button.left)

#双击
mouse.click(Button.left, 1)


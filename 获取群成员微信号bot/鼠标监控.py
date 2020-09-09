from pynput import mouse

# def on_move(x, y ):
#  print('鼠标移动至 {0}'.format(
#   (x,y)))

def on_click(x, y , button, pressed):
 print('{0} 在坐标 {1}'.format('点击' if pressed else '释放', (x, y)))
 if not pressed:
  return False

# def on_scroll(x, y ,dx, dy):
#  print('scrolled {0} at {1}'.format(
#   'down' if dy < 0 else 'up',
#   (x, y)))

while True:
 with mouse.Listener( on_click = on_click) as listener:
  listener.join()
from PIL import Image, ImageGrab, ImageChops
import numpy as np
import pyautogui
from pyautogui import moveTo, press, click, rightClick
import time as t
import matplotlib.pyplot as plt
import random


# Screenshot
"""
img = ImageGrab.grab()
img.save('test.png')
"""


"""
gray = cv2.imread('test.png')
print(gray.shape)
gray[gray < 180] = 0
cv2.imwrite('test1.png', gray)
pyautogui.moveTo(0, 0)
"""


# Find and save label
"""
tmp = cv2.imread('ss.jpg')
print(tmp.shape)
plt.imshow(tmp[506:546, 1136:1177])
cv2.imwrite('label.png', tmp[506:546, 1136:1177])
"""


Label = Image.open('label.png')
Label = np.asarray(Label)
pause = 5


# Сравнение изображений
def sravn(im):
    im = im[506:546, 1136:1177]
    diff = ImageChops.difference(Image.fromarray(Label), Image.fromarray(im))
    d = np.asarray(diff).mean()
    # print(d)
    if d < 10:
        return 1
    return 0


g_counter = random.randint(5, 50)
counter = 0
timer = t.time()
print('Success start')


while True:
    img = ImageGrab.grab()
    # img.save(f'data/trase/{int(t.time())}.png')
    img = np.asarray(img)
    # print(int(t.time()))
    if sravn(img) == 1:
        # pause
        t.sleep(random.randint(1, 500) / 1000)
        # press f
        pyautogui.press('f')
        pyautogui.press('f')
        pyautogui.press('f')
        # Global pause
        t.sleep(random.randint(0, pause) + random.randint(0, 999) / 1000)
        # pause
        t.sleep(3 + random.randint(0, 5) + random.randint(100, 999) / 1000)
        pyautogui.press('8')
        pyautogui.press('8')
        pyautogui.press('8')
        t.sleep(random.randint(0, 2) + random.randint(0, 999) / 1000)
        pyautogui.moveTo(random.randint(1, 1000), random.randint(1, 1000), duration=random.randint(1000, 3000) / 1000)
        timer = t.time()
        counter += 1
    if t.time() - timer > 60:
        pyautogui.keyDown('i')
        t.sleep(random.randint(100, 500) / 1000)
        pyautogui.press('8')
        pyautogui.press('8')
        pyautogui.press('8')
        t.sleep(random.randint(0, 3) + random.randint(0, 999) / 1000)
        pyautogui.moveTo(random.randint(1, 1000), random.randint(1, 1000), duration=random.randint(1000, 3000) / 1000)
        timer = t.time()
        print('Error, so try again')
    if counter > g_counter:
        """r = random.randint(100, 500) / 1000
        pyautogui.keyDown('w')
        t.sleep(r)
        pyautogui.keyUp('w')
        t.sleep(r)
        pyautogui.keyDown('s')
        t.sleep(r)
        pyautogui.keyUp('s')
        t.sleep(r)
        r = random.randint(50, 500) / 1000
        pyautogui.keyDown('a')
        t.sleep(r)
        pyautogui.keyUp('a')
        t.sleep(r)
        pyautogui.keyDown('d')
        t.sleep(r)
        pyautogui.keyUp('d')"""

        g_counter = random.randint(5, 50)
        counter = 0

        t.sleep(300)
        pyautogui.press('8')
        pyautogui.press('8')
        pyautogui.press('8')
        timer = t.time()
        print('New Epoch')

from PIL import Image, ImageGrab, ImageChops
import numpy as np
import pyautogui
from pyautogui import moveTo, press, click, rightClick
import time as t
import matplotlib.pyplot as plt
import random
import cv2
from sys import exit
# import keyboard
import random


"""
for i in range(1, 7, 1):
    img = np.asarray(Image.open(f'{i}.jpg'))
    img = img[:900, 200:1500]
    plt.imsave(f'test1{i}.png', img)
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    # RED
    hsv_min = np.array((0, 50, 150), np.uint8)
    hsv_max = np.array((10, 255, 255), np.uint8)
    th = cv2.inRange(hsv, hsv_min, hsv_max)

    # th = th[:650, 200:1500]

    # Find enemy
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 4))
    closed = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, kernel, iterations=1)
    closed = cv2.dilate(closed, kernel, iterations=1)

    # closed[753:755, 590:905]
    plt.imsave(f'test{i}.png', closed[90:95, 590:935])
"""


# exit()

def POS_KV(closed):
    return closed[67:69, 630:770]


def POS(closed):
    return closed[67:69, 600:740]


# Finish and take kvest
def check_kv():
    pyautogui.keyDown('alt')
    t.sleep(0.1)
    XY = (1700, 550)
    pyautogui.moveTo(1700, 470, duration=0.1)
    pyautogui.click()
    pyautogui.moveTo(1700, 500, duration=0.1)
    pyautogui.click()
    pyautogui.moveTo(1700, 520, duration=0.1)
    pyautogui.click()
    pyautogui.moveTo(1700, 550, duration=0.1)
    pyautogui.click()
    pyautogui.moveTo(1700, 580, duration=0.1)
    pyautogui.click()
    pyautogui.moveTo(1700, 600, duration=0.1)
    pyautogui.click()
    pyautogui.moveTo(1700, 620, duration=0.1)
    pyautogui.click()
    pyautogui.keyUp('alt')
    for i in range(20):
        pyautogui.press('f')
    t.sleep(0.1)
    pyautogui.press('esc')
    t.sleep(0.3)
    pyautogui.keyDown('j')
    t.sleep(0.2)
    pyautogui.keyUp('j')
    XY = (240, 315)
    pyautogui.moveTo(240, 315, duration=0.1)
    pyautogui.click()
    XY = (350, 995)
    pyautogui.moveTo(350, 995, duration=0.1)
    for i in range(10):
        pyautogui.scroll(-1)
    pyautogui.click()
    for i in range(20):
        pyautogui.press('f')
    t.sleep(0.1)
    pyautogui.press('esc')


# Отступы: y - 0:500 (900), x - 200:1500
# Середина x - 960

time_attack = t.time()


# Movement
def movement(closed):
    def find_nearest():
        nearest = 960
        g_m = 0
        centers, hierarchy = cv2.findContours(closed[:500], cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for i in range(len(centers)):
            # print(centers)
            k = (centers[i][0, 0, 0] + centers[i][2, 0, 0] + 200 + 200) / 2
            if np.abs(960 - k) < nearest:
                nearest = np.abs(960 - k)
                g_m = k
        return g_m
    def go_straight():
        pyautogui.press('f')
        pyautogui.press('f')
        pyautogui.keyDown('w')
        t.sleep(0.8)
        pyautogui.keyUp('w')
        #print('Straight')
    def turn_left():
        pyautogui.keyDown('left')
        pyautogui.keyDown('f')
        t.sleep(0.001)
        pyautogui.keyUp('left')
        pyautogui.keyUp('f')
        #print('Left')
    def turn_right():
        pyautogui.keyDown('right')
        pyautogui.keyDown('f')
        t.sleep(0.001)
        pyautogui.keyUp('right')
        pyautogui.keyUp('f')
        #print('Right')
    def see_nothing():
        pyautogui.keyDown('right')
        pyautogui.keyDown('f')
        t.sleep(0.2)
        pyautogui.keyUp('right')
        pyautogui.keyUp('f')
        #print('See nothing')
    g_m = 0
    try:
        g_m = find_nearest()
    except Exception as e:
        with open('log.txt', 'a') as f:
            f.write(str(e) + '\n')
    if g_m == 0:
        see_nothing()
    elif g_m > 1080:
        turn_right()
    elif g_m < 800:
        turn_left()
    else:
        go_straight()


AUTO_ATTACK = 'right'
FAST_MOVE = '1'
OTHER = {'2': 50, '4': 30, 'x': 30, 'z': 30, 'c': 20}


# Комбинации атаки
# Need fix
def attack():
    pyautogui.keyDown(FAST_MOVE)
    t.sleep(0.15)
    pyautogui.keyUp(FAST_MOVE)
    pyautogui.mouseDown(button=AUTO_ATTACK)
    tmp = t.time()
    while t.time() - tmp < 2:
        closed, _, problems = take_screen()
    pyautogui.mouseUp(button=AUTO_ATTACK)
    if random.randint(0, 100) < 50:
        pyautogui.press('2')
        pyautogui.press('2')
        t.sleep(0.2)
        pyautogui.press('2')
        pyautogui.press('2')
    elif random.randint(0, 100) < 30:
        pyautogui.press('4')
        pyautogui.press('4')
        t.sleep(0.2)
    elif random.randint(0, 100) < 20:
        pyautogui.press('x')
        pyautogui.press('x')
        t.sleep(0.2)
        pyautogui.press('x')
        pyautogui.press('x')
    elif random.randint(0, 100) < 30:
        pyautogui.keyDown('z')
        t.sleep(0.15)
        pyautogui.keyUp('z')
        t.sleep(0.4)
        pyautogui.keyDown('z')
        t.sleep(0.15)
        pyautogui.keyUp('z')
    elif random.randint(0, 100) < 20:
        pyautogui.press('c')
        t.sleep(3.5)
    # print('Attack')


def HP_BOSS(closed):
    if closed[90:95, 590:935].min() == 255:
        return 100
    elif closed[90:95, 590:866].min() == 255:
        return 80
    elif closed[90:95, 590:797].min() == 255:
        return 60
    elif closed[90:95, 590:728].min() == 255:
        return 40
    elif closed[90:95, 590:659].min() == 255:
        return 20
    return 0


def HP_PERS(closed):
    if closed[753:755, 590:905].min() == 255:
        return 100
    elif closed[753:755, 590:842].min() == 255:
        return 80
    elif closed[753:755, 590:779].min() == 255:
        return 60
    elif closed[753:755, 590:716].min() == 255:
        return 40
    elif closed[753:755, 590:653].min() == 255:
        return 20
    return 0
   

def control_hp(closed):
    # print('PERS -', HP_PERS(closed))
    # print('BOSS -', HP_BOSS(closed))
    if HP_PERS(closed) <= 40:
        # Drink smth to heal
         pyautogui.press(HEAL)
         return 1
    return 0


# Screenshot
def take_screen():
    img = np.asarray(ImageGrab.grab())
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    # RED
    hsv_min = np.array((0, 50, 150), np.uint8)
    hsv_max = np.array((15, 255, 255), np.uint8)
    th = cv2.inRange(hsv, hsv_min, hsv_max)
    # Find enemy
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 4))
    closed = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, kernel, iterations=1)
    closed = cv2.dilate(closed, kernel, iterations=1)
    closed = closed[:900, 200:1500]
    hp_error = control_hp(closed)
    if POS(closed).min() == 255 or POS_KV(closed).min() == 255:
        return closed, 1, hp_error
    return closed, 0, hp_error


fight = 0
fin = 0
g_time = t.time()

HEAL = '7'
REPAIR = '5'

while True:
    # Try to catch smth while taking screen
    pyautogui.keyDown('f')
    # Take screenshot and check enemy
    closed, att, problems = take_screen()
    pyautogui.keyUp('f')
    # Start fighting
    if att == 1:
        if POS(closed).min() == 255:
            fin = 1
        attack()
        fight = 1
    else:
        # Check territory arround after fighting
        if fight == 1 or problems == 1:
            # Remember last attack time
            time_attack = t.time()
            
            # ---Try to find loot---
            pyautogui.keyDown('f')
            t.sleep(0.05)
            pyautogui.keyDown('right')
            
            # Chechk enemy
            tmp = t.time()
            while t.time() - tmp < 3.8 and att == 0:
                closed, att, problems = take_screen()
            
            pyautogui.keyUp('right')
            t.sleep(0.05)
            pyautogui.keyUp('f')
            
            closed, att, problems = take_screen()
            fight = 0
            if att == 0 and t.time() - g_time > 10800:
                pyautogui.press(REPAIR)
                pyautogui.press(REPAIR)
                g_time = t.time()
                t.sleep(5)
        elif att == 0:
            # Finish kvest
            if fin == 1:
                check_kv()
                fin = 0
            else:
                pyautogui.press('f')
                pyautogui.press('f')
                # If blocked
                if t.time() - time_attack > 50:
                    pyautogui.keyDown('right')
                    pyautogui.keyDown('f')
                    t.sleep(1.8)
                    pyautogui.keyUp('right')
                    pyautogui.keyUp('f')
                    pyautogui.keyDown('w')
                    t.sleep(2)
                    pyautogui.keyUp('w')
                    time_attack = t.time()
                # Movement
                movement(closed)
                # print('movement finish')
'''    
    except Exception as e:
        with open('log.txt', 'a') as f:
            f.write(str(e) + '\n')
'''

exit()

import keras
import os

for roots, dirs, f in os.walk('data/good'):
    pass
arr = []
for i in f:
    img = np.asarray(Image.open(f'data/good/{i}'))
    arr.append(img)
plt.imshow(arr[10])
plt.show()
arr1 = []
for roots, dirs, f in os.walk('data/bad'):
    pass
for i in f:
    img = np.asarray(Image.open(f'data/bad/{i}'))
    arr1.append(img)
plt.imshow(arr1[10])
plt.show()


arr = np.asarray(arr)
arr1 = np.asarray(arr1)
y = np.ones(len(arr))
y1 = np.zeros(len(arr1))


model = keras.models.Sequential()
model.add(keras.layers.Conv2D(3, (3, 3), input_shape=arr[0].shape, activation='relu'))
model.add(keras.layers.MaxPooling2D(5))
model.add(keras.layers.Conv2D(3, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D(5))
model.add(keras.layers.Conv2D(3, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D(5))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(1, activation='sigmoid'))
print(model.summary())

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
history = model.fit(arr[:], y[:], epochs=5)
model.save('data/model')





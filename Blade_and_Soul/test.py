from PIL import Image, ImageGrab, ImageChops
import numpy as np
import pyautogui
from pyautogui import moveTo, press, click, rightClick
import time as t
import matplotlib.pyplot as plt
import random
import cv2
import skimage
from skimage import filters

"""
img = ImageGrab.grab()
img.save(f'data/trase/{int(t.time())}.png')
"""

"""
img = cv2.imread('data/trase/1578049500.png', cv2.IMREAD_GRAYSCALE)

# img[300:320, 700:720] = 0
# print(img[300:320, 700:720].mean())
img = skimage.filters.sobel(img)
print(img)
plt.imshow(img, cmap='gray')
plt.show()
"""




"""
img = cv2.imread('testing.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img.shape)
img = img[857:894, 1177:1210]
cv2.imwrite('label1.png', img)

plt.imshow(img)
plt.show()
"""








quit()


import os


# Отступы: y - 0:650, x - 200:1500
# Середина x - 960

for roots, dirs, f in os.walk('data/good'):
    pass
f = ['1.jpg']
for i in f:
    img = cv2.imread(f'data/{i}')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hsv_min = np.array((0, 100, 0), np.uint8)
    hsv_max = np.array((10, 255, 255), np.uint8)
    th = cv2.inRange(hsv, hsv_min, hsv_max)
    th = th[:650, 200:1500]

    cv2.imwrite('check1.png', th)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 5))
    closed = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, kernel, iterations=1)
    closed = cv2.dilate(closed, kernel, iterations=1)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 5))
    closed = cv2.morphologyEx(closed, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, kernel, iterations=1)
    closed = cv2.dilate(closed, kernel, iterations=1)

    cv2.imwrite('check2.png', closed)
    cv2.imwrite(f'data/{i}', closed)

    if closed[51:69, 600:900].min() == 255:
        print('Straight')
    else:
        centers, hierarchy = cv2.findContours(closed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        nearest = 960
        g_m = 0
        for i in range(len(centers)):
            print(centers)
            k = (centers[i][0, 0, 0] + centers[i][2, 0, 0] + 200 + 200) / 2
            if np.abs(960 - k) < nearest:
                nearest = np.abs(960 - k)
                g_m = k
        if g_m == 0:
            pass
        elif g_m > 1010:
            print('Right')
        elif g_m < 900:
            print('Left')
        else:
            print('Straight')










quit()

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





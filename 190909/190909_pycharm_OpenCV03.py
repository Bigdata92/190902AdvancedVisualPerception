import cv2                              #OpenCV     BGR 순서
from matplotlib import pyplot as plt    #matplotlib RGB 순서

img = cv2.imread('monkey.jpg', cv2.IMREAD_COLOR)
plt.imshow(img[...,::-1], interpolation='bicubic') #B & R change 되서 show
plt.xticks([]), plt.yticks([])
plt.show()


img_BGR = cv2.imread('monkey.jpg')
img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

plt.imshow(img_RGB, interpolation='bicubic')
plt.show()


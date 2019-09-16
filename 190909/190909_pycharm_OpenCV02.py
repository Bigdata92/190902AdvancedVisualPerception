import cv2 #Esc로 프로그램 끄는 ex
img = cv2.imread('monkey.jpg', cv2.IMREAD_COLOR)
while True:
    cv2.imshow('img', img)
    c = cv2.waitKey(30)
    if c == 27: #Esc ASCII 27
        break

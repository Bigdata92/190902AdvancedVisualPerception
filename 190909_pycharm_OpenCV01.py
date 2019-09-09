import cv2

img = cv2.imread('monkey.jpg', cv2.IMREAD_UNCHANGED)

print('type(img) = ', type(img))
print('img.shape, img.dtype = ', img.shape, img.dtype)

cv2.imshow('img', img)
cv2.waitKey(3000) #숫자 만큼 기다리다가 꺼짐 단위: ms




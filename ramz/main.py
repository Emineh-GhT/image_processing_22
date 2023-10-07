import cv2


img_a = cv2.imread('a.png', 0)
img_b = cv2.imread('b.png', 0)

result = img_a//2 + img_b//2

cv2.imshow('output' , result)
cv2.waitKey()

cv2.imwrite('result.jpg' , result)
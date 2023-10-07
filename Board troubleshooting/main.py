import cv2

origin = cv2.imread('board - origin.bmp', 0)
test = cv2.imread('board - test.bmp', 0)

test = cv2.flip(test, 1) #enekas

result = cv2.subtract(origin , test)

cv2.imwrite('Result.jpg' , result)
cv2.imshow('result' , result)
cv2.waitKey()
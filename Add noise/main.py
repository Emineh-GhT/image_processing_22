import random
import cv2

image = cv2.imread('Mona_Lisa.jpg', 0 )
height , width = image.shape

for n in range(1000):
    a = random.randint(0,height-1)
    b = random.randint(0,width-1)
    image[a,b] = 255

for n in range(1000):
    c = random.randint(0,height-1)
    d = random.randint(0,width-1)
    image[c,d] = 0

cv2.imwrite('result.jpg', image)
cv2.imshow('result', image)
cv2.waitKey()
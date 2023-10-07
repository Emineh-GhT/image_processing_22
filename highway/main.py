import numpy as np
import cv2

images = []
for i in range (0,15):
    img = cv2.imread(f'images/h{i}.jpg', 0)
    images.append(img)
    rows , cols = img.shape
result = np.zeros((rows,cols), dtype="uint8")
for image in images:
    result += image//15

cv2.imwrite('Result.jpg' , result)
cv2.imshow('output' , result)
cv2.waitKey()
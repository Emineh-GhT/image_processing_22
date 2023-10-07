import numpy as np
import cv2

images1 = []
for i in range (1,6):
    img1 = cv2.imread(f'1/{i}.jpg', 0)
    images1.append(img1)
    rows1 , cols1 = img1.shape
result1 = np.zeros((rows1,cols1), dtype="uint8")
for image in images1:
    result1 += image//5
height1 , width1 = result1.shape

images2 = []
for i in range (1,6):
    img2 = cv2.imread(f'2/{i}.jpg', 0)
    images2.append(img2)
    rows2 , cols2 = img2.shape
result2 = np.zeros((rows2,cols2), dtype="uint8")
for image in images2:
    result2 += image//5
height2 , width2 = result2.shape

images3 = []
for i in range (1,6):
    img3 = cv2.imread(f'3/{i}.jpg', 0)
    images3.append(img3)
    rows3 , cols3 = img3.shape
result3 = np.zeros((rows3,cols3), dtype="uint8")
for image in images3:
    result3 += image//5
height3 , width3 = result3.shape

images4 = []
for i in range (1,6):
    img4 = cv2.imread(f'4/{i}.jpg', 0)
    images4.append(img4)
    rows4 , cols4 = img4.shape
result4 = np.zeros((rows4,cols4), dtype="uint8")
for image in images4:
    result4 += image//5
height4 , width4 = result4.shape

# افزودن تصاویر به صورت افقی
top_row = cv2.hconcat([result1, result2])
bottom_row = cv2.hconcat([result3, result4])

# افزودن تصاویر به صورت عمودی
result = cv2.vconcat([top_row, bottom_row])
cv2.imwrite('result.jpg' , result)

# نمایش تصویر حاصل
cv2.imshow('Result', result)
cv2.waitKey(0)
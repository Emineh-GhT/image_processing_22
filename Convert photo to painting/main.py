import cv2

image = cv2.imread('lion.jpg' )

# تبدیل تصویر به تصویر سیاه و سفید
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# تطبیق فیلتر گاوسی
gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)

# تشدید لبه‌ها
edges = cv2.Laplacian(gray_blur, cv2.CV_8U, ksize=5)

# تبدیل تصویر به نقاشی
threshold, result = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

cv2.imwrite('Result.jpg', result)
# نمایش نقاشی
cv2.imshow('Painting Effect', result)
cv2.waitKey(0)
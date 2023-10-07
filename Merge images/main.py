import cv2

# بارگیری تصاویر
emi = cv2.imread('images/emi.jpg' , 0)
scarlett = cv2.imread('images/scarlett-johansson_0.jpg' , 0)

print(emi.shape)
print(scarlett.shape)

emi = cv2.resize(emi , (1000 , 800))
scarlett = cv2.resize(scarlett , (1000 , 800))


# توزیع وزن
alpha = 0  # وزن تصویر اول
beta = 1   # وزن تصویر دوم
gamma = 0    # پارامتر gamma
# ادغام تصاویر با توزیع وزن
result1 = cv2.addWeighted(emi, alpha, scarlett, beta, gamma)
cv2.imwrite('result1.jpg' , result1)
cv2.imshow('result' , result1)
cv2.waitKey()

# توزیع وزن
alpha = 0.7  # وزن تصویر اول
beta = 0.3   # وزن تصویر دوم
gamma = 0    # پارامتر gamma
# ادغام تصاویر با توزیع وزن
result2 = cv2.addWeighted(emi, alpha, scarlett, beta, gamma)
cv2.imwrite('result2.jpg' , result2)
cv2.imshow('result' , result2)
cv2.waitKey()

# توزیع وزن
alpha = 0.3  # وزن تصویر اول
beta = 0.7   # وزن تصویر دوم
gamma = 0    # پارامتر gamma
# ادغام تصاویر با توزیع وزن
result3 = cv2.addWeighted(emi, alpha, scarlett, beta, gamma)
cv2.imwrite('result3.jpg' , result3)
cv2.imshow('result' , result3)
cv2.waitKey()

# توزیع وزن
alpha = 1  # وزن تصویر اول
beta = 0   # وزن تصویر دوم
gamma = 0    # پارامتر gamma
# ادغام تصاویر با توزیع وزن
result4 = cv2.addWeighted(emi, alpha, scarlett, beta, gamma)
cv2.imwrite('result4.jpg' , result4)
cv2.imshow('result' , result4)
cv2.waitKey()
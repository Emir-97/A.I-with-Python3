from cv2 import cv2
import numpy as np
gaussValue = 3
kernelValue = 3
original = cv2.imread('monedas.jpg')
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(gray, (gaussValue, gaussValue), 0)
canny = cv2.Canny(gauss, 60, 100)
kernel = np.ones((kernelValue, kernelValue), np.uint8)
close = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
contours1, hierarchy = cv2.findContours(close.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Found coinds: {}".format(len(contours1)))
cv2.drawContours(original, contours1, -1, (0, 0, 255), 2)


# show results

cv2.imshow('gray picture', gray)
cv2.imshow('gauss picture', gauss)
cv2.imshow('canny picture', canny)
cv2.imshow('final picture', original )
cv2.imshow('close picture', close)
cv2.waitKey(0)

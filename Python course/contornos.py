import cv2
image = cv2.imread('contorno.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_,threshold1 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
contours1, hierarchy = cv2.findContours(threshold1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours1, -1, (10,200,100), 3)
#show
cv2.imshow('original image', image)
cv2.imshow('gray image', gray)
cv2.imshow('image threshold1', threshold1)
cv2.waitKey(0)
cv2.destroyAllWindows()
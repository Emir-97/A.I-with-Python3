import cv2 as cv

videoCapture1 = cv.VideoCapture(0)
if not videoCapture1.isOpened():
      print('The videocamera is closed.')
      exit()
while True :
   typeCamera,Camera = videoCapture1.read(1)
   gray = cv.cvtColor(Camera, cv.COLOR_BGR2GRAY)
    
   cv.imshow('In Live', gray)
     
   if cv.waitKey(1)== ord("e"):
      break
videoCapture1.release()
cv.destryAllWindows()
    
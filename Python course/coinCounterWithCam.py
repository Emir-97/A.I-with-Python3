# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:38:45 2021

@author: EMIR
"""

import cv2 as cv
import numpy as np
def orderPoints(points):
    n_points = np.concatenate([points[0], points[1], points[2], points[3]]).tolist()
    y_order = sorted(n_points, key=lambda n_points: n_points[1])
    x1_order = y_order[:2]
    x1_order = sorted(x1_order, key= lambda x1_order: x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key = lambda x2_order: x2_order[0])
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]
def alignments(image, width, height):
    aligned_image = None
    gray =  cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    thresholdType, threshold1 = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
    cv.imshow('Threshold', threshold1)
    contour = cv.findContours(threshold1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
    contour =  sorted(contour, key=cv.contourArea, reverse = True)[:1]
    for c in contour:
        epsilon = 0.01 * cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, epsilon, True)
        if len(approx)==4:
            points = orderPoints(approx)
            points1 = np.float32(points)
            points2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])
            M = cv.getPerspectiveTransform(points1, points2)
            aligned_image = cv.warpPerspective(image, M, (width, height))
    return aligned_image
videoCapture1 = cv.VideoCapture(0)

while True:
    cameraType, camera = videoCapture1.read()
    if cameraType == False:
        break
    A6_image = alignments(camera, width=480, height=640)
    if A6_image is not None:
        points = []
        gray_image = cv.cvtColor(A6_image, cv.COLOR_BGR2GRAY)
        gaussianImage = cv.GaussianBlur(gray_image, (5,5), 1)
        _, threshold2 = cv.threshold(gaussianImage, 0, 255, cv.THRESH_OTSU + cv.THRESH_BINARY_INV)
        cv.imshow('Threshold', threshold2)
        contour1 = cv.findContours(threshold2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
        cv.drawContours(A6_image, contour1, -1, (255,0,0), 2)
        sum1 = 0.0
        sum2 = 0.0
        sum3 = 0.0
        sum4 = 0.0
        for c_1 in contour1:
            area = cv.contourArea(c_1)
            moments1 = cv.moments(c_1)
            if (moments1["m00"] == 0):
                moments1["m00"] = 1.0
            x = int(moments1["m10"]/ moments1["m00"])
            y = int(moments1["m01"] / moments1["m00"])
            if area > 6700 and area < 7200:
                font = cv.FONT_HERSHEY_SIMPLEX     
                cv.putText(A6_image, "P/. $1", (x,y), font, 0.75, (0,255,0), 2)
                sum1 = sum1 + 1
            if area > 7300 and area < 8200:
                font = cv.FONT_HERSHEY_SIMPLEX
                cv.putText(A6_image, "P/. $2", (x,y), font, 0.75, (0,255,0), 2)
                sum2 += 2
            if area > 8500 and area < 1075:
                font = cv.FONT_HERSHEY_SIMPLEX
                cv.putText(A6_image, "P/. $0.25", (x,y), font, 0.75, (0,255,0), 2)
                sum3 += 0.25
            if area > 1080 and area < 1100:
                font = cv.FONT_HERSHEY_SIMPLEX
                cv.putText(A6_image, "P/. $0.50", (x,y), font, 0.75, (0,255,0), 0)
                sum4 += 0.50
        
        total = sum1 + sum2 + sum3 + sum4
        print("The total sum is the: ", round(total, 2))
        cv.imshow("This is the A6 image", A6_image)
        cv.imshow("This is the camera image", camera)
    if cv.waitKey(1) == ord('e'):
        break
videoCapture1.release()
cv.destroyAllWindows()
        

            
    
    

    
    
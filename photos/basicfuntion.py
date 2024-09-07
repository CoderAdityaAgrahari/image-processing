import cv2 as cv
import numpy as np
img = cv.imread("D:\photos\spider.jpg")                  #it gives address of img
kernel= np.ones((5,5),np.uint8)                         #it gives matrix here 5,5 is and the value of all is one type in unsignedintegern8bit
imggray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)               #for change the color bgr to gray
imgblur=cv.GaussianBlur(imggray,(9,9),0)                #it gives us in kennel from blur img
imgcan=cv.Canny(img,100,500)                            #it gives canny image here 100 is max and 50 min thersold
imgDialation=cv.dilate(imgcan,kernel,iterations=1)      #this dilate is use for thikness we use kernel for matrix and iterations increase by multipication  on matrix
imgerode=cv.erode(img,kernel,iterations=1)




cv.imshow('spiderman', img)                             #this is use  for show in new window and there is name of variable
cv.imshow('spgray',imggray)
cv.imshow('spblur',imgblur) 
cv.imshow('canney spider', imgcan) 
cv.imshow('delate spider', imgDialation) 
cv.waitKey(0)                                            #this is use for infinite time means with out any keys


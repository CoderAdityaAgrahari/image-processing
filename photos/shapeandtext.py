import cv2 as cv
import numpy as np
img= np.zeros((512,512,3),np.uint8)                 #for black image we use zeros and the size of it s by 512 and 3 is use for color in bgr


# cv.line(img,(0,0),(300,300),(0,255,0),3)           #this is use for make a line img is black and 0 is starting point and 300 is ending point and (0,255,0)is use for color and 3 is thickness
# cv.rectangle(img,(0,0),(300,300),(0,0,255),2)      #this is use  for make a rectangle and there is also same for line 
cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,200),2)
cv.rectangle(img,(0,0),(img.shape[1],img.shape[0]),(200,0,100),cv.FILLED)   #this is use for only here is one change img.shape or other is same

                                                                            #there is use cv.filled to fill the rectangle


cv.circle(img,(300,250),(60),(255,255,0),3)                                #ther == circle for immg and after that center point and radius and color and thickness
cv.putText(img," IM  ",(220,270),cv.FONT_HERSHEY_PLAIN,5,(0,0,255))         #this is use for insert text here img and after that text and its position and font scale and color



print(img)
cv.imshow("image",img)
cv.waitKey(0)
import cv2 as cv
img= cv.imread("D:\photos\spider.jpg")
print(img.shape)                                   #it gives the shape means size in width and height and which ide its work here is 3 for bgr
imgResize = cv.resize(img,(500,500))               #it resize thee img by which value we  give 
print(imgResize.shape)
imgcrope=img[10:200,10:500]                      #it use for crope first is height and after that width and 200 and 500 is size where to we want to cut

cv.imshow('image',img)
cv.imshow('resize',imgResize)
cv.imshow("crope",imgcrope)
cv.waitKey(0)
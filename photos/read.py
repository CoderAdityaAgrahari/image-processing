
import cv2 as cv

# Read the image from the specified path
img = cv.imread("D:\photos\spider.jpg")
# Check if the image is loaded correctly
if img is None:
    print("Error: Image not found.")
    exit()

# Display the image in a window
cv.imshow('Spiderman', img)

# Wait indefinitely for a key press
cv.waitKey(0)

# cap = cv.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(10, 200)

# while True:
#     success, img = cap.read()
#     cv.imshow("Video", img)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

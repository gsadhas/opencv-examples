import cv2
import numpy as np

# Gausian blur to smooth the images
image = cv2.imread("thresh.jpg")
cv2.imshow("Original", image)

# How much to blur on image axis; should be odd values;
# (5, 55)- blur little bit on x and lot more on y axis; Should be an odd values
blur = cv2.GaussianBlur(image, (5, 55), 0)
cv2.imshow("Blur", blur)

# Dilation and Erosion
# Dilation - expand the pixels - Trun black/background pixels into white pixels
# Erosion - contract the pixels - Trun white pixels into black pixels

kernel = np.ones((5, 5), 'uint8') # Odd values in both dimensions
dilate = cv2.dilate( image, kernel, iterations=1)
# High level iterations increase the effectiveness of the filters
# and it will continue to eat away the image more than the first pass
erode = cv2.erode(image, kernel, iterations=1)
cv2.imshow("Dilate", dilate)
cv2.imshow("Erode", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
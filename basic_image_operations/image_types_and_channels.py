import numpy as np
import cv2

color = cv2.imread("butterfly.jpg", 1)
cv2.imshow("Image", color)
cv2.moveWindow("Image", 0, 0)
print(color.shape)
height, width, channels = color.shape

b, g, r = cv2.split(color) # Split color channels into blue, green, red channel matrix

rgb_split = np.empty((height, width*3, 3), 'uint8')

rgb_split[:, 0:width] = cv2.merge((b, b, b)) # Place blue channel in the left side of the image
rgb_split[:, width:width*2] = cv2.merge((g, g, g))
rgb_split[:, width*2:width*3] = cv2.merge((r, r, r))

cv2.imshow("Channels", rgb_split)
cv2.moveWindow("Channels", 0, height)

# Hue, Saturation and Value space - If we want to isolate particular color HSV space is better that RGB space

hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
# Concatenate image channels using efficient numpy operator
hsv_split = np.concatenate((h, s, v), axis=1) # axis = 1, make three images appear side by side
cv2.imshow("Split HSV", hsv_split)


cv2.waitKey(0)
cv2.destroyAllWindows()
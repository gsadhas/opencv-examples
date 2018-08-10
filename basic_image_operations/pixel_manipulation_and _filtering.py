import numpy as np
import cv2

color = cv2.imread("butterfly.jpg", 1)

gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.jpg", gray)

# Channels split faster than cv2.split()
b = color[:, :, 0]
g = color[:, :, 1]
r = color[:, :, 2]

rgba = cv2.merge((b, g, r, g)) # g - non green parts of the image as transparent; anything low green value or zero, would appears as transparent
cv2.imwrite("rgba.png", rgba) # jpeg image does not support alpha channel



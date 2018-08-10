import numpy as np
import cv2

img = cv2.imread("players.jpg", 1)
# Scale
img_half = cv2.resize(img, (0,0), fx=0.5, fy=0.5) # Image, absolute size in pixels,relative size in x, relative size in y
img_stretch = cv2.resize(img,(600,600))
img_stretch_near = cv2.resize(img, (600,600), interpolation=cv2.INTER_NEAREST)

cv2.imshow("Half", img_half)
cv2.imshow("Stretch", img_stretch)
cv2.imshow("Strech near", img_stretch_near)

# Rotation
M = cv2.getRotationMatrix2D((0, 0), -30, 1) # origin - (0,0) rotate from top left corner
roated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Rotated", roated)

cv2.waitKey(0)
cv2.destroyAllWindows()



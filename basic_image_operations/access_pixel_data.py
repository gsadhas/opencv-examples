import numpy as np
import cv2

img = cv2.imread("opencv-logo.png", 1) # 1 - default colors # 0 - black and white
print(type(img))
print("Row ", len(img))
print("Columns ", len(img[0]))
print("Channels ", len(img[0][0]))
print("Shape: ", img.shape)
print("Image type ", img.dtype) # uint8 - Maximum of 2^8 values in each pixels; Range of value ranges from 0 to 255
print("Random Pixel ", img[10][10])
print("One channel image ", img[:, :, 1])
print("Total number of pixels ", img.size)
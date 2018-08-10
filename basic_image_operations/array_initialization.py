import numpy as np
import cv2

black = np.zeros((150, 200, 1), 'uint8')
cv2.imshow("Black", black)
print(black[0, 0, :])

ones = np.ones((150, 200, 3), 'uint8') # will show as black image though pixel value is 1
cv2.imshow("Ones", ones)
print(ones[0, 0, :])

white = np.ones((150, 200, 3), 'uint16') # 16 bit length image
white *= (2**16-1) # since the value starts at zero
cv2.imshow("White", white)
print(white[0, 0, :]) # Maximum size of an integer in a 16-bit length image - 65535

color = ones.copy() # Create deep copy of ones array
color[:, :] = (255, 0, 0) # Color image of all blue pixels
cv2.imshow("Blue", color)
print(color[0, 0, :])

cv2.waitKey(0)
cv2.destroyAllWindows()
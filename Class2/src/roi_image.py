import numpy as np
import cv2

img = cv2.imread('test.jpg')
# cut out a piece. [from_x:to_x, from_y:to_y]
piece = img[10:90, 10:300]
img2 = img.copy()
# put cutted piece into another place
img2[90:170, 10:300] = piece

while(1):
    cv2.imshow("Origianl", img)
    cv2.imshow("Cutted", piece)
    cv2.imshow("With piece", img2)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

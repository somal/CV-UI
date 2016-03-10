import numpy as np
import cv2

img = cv2.imread('test.jpg')

# access individual pixel at position (100,100)
px = img[100, 100]
print px
# acess only one color
blue = img[100,100,0]
green = img[100,100,1]
red = img[100,100,2]

print ("Blue:{}, green:{}, red:{}".format(blue,green,red))

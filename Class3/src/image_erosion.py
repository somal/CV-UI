import cv2
import numpy as np

if __name__ == '__main__':
    while(1):
        img = cv2.imread('test.jpg', 0)
        kernel = np.ones((10, 20), np.uint8)
        erosion = cv2.erode(img, kernel, iterations=1)
        cv2.imshow('Original image', img)
        cv2.imshow('Transformed image', erosion)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

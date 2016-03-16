import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if __name__ == '__main__':
    while (True):
        ret, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # x-axis and y-axis sobel images
        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
        
        cv2.imshow('Sobel x', sobelx)
        cv2.imshow('Sobel y', sobely)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

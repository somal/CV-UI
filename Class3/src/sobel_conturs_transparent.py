import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if __name__ == '__main__':
    while (True):
        ret, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # x-axis and y-axis sobel images
        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=9)
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=9)

        owerlayed = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

        cv2.imshow('Sobel x', sobelx)
        cv2.imshow('Sobel y', sobely)
        cv2.imshow('Owerlayed', owerlayed)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

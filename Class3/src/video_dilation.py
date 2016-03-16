import cv2
import numpy as np

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while(1):
        # get frame from camera
        ret, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # dilate image
        kernel = np.ones((10, 10), np.uint8)
        dilation = cv2.dilate(img, kernel, iterations=1)

        # show images
        cv2.imshow('Original image', img)
        cv2.imshow('Transformed image', dilation)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

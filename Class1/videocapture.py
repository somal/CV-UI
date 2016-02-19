import numpy as np
import cv2
import time

if __name__=="__main__":

    cap = cv2.VideoCapture(0)
    while(True):
        start=time.time()

        # Ca pture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the   frame come here
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1);
        print(1/(time.time()-start))

    cap.release()
    cv2.destroyAllWindows()

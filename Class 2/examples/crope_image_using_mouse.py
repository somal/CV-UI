import numpy as np
import cv2

if __name__ == '__main__':
    # Coordinates have form [y,x]
    first_coordinates = [0, 0]
    second_coordinates = [100, 100]
    mouse_down = False

    def get_x_y(event, x, y, flag, param):
        global first_coordinates, second_coordinates, mouse_down
        if event == cv2.EVENT_LBUTTONUP:
            second_coordinates[0] = x
            second_coordinates[1] = y
            mouse_down = False
        elif event == cv2.EVENT_LBUTTONDOWN:
            mouse_down = True
            first_coordinates[0] = x
            first_coordinates[1] = y

    img = cv2.imread('test2.jpg')
    img2 = img[0:10, 0:10]
    cv2.namedWindow('Original')
    cv2.setMouseCallback('Original', get_x_y)
    while(1):
        if not (mouse_down):
            if (first_coordinates[0] == second_coordinates[0]) or \
               (first_coordinates[1] == second_coordinates[1]):
                print ("Incorrect selection\n")
            else:
                img2 = img[min(first_coordinates[1], second_coordinates[1]):
                           max(first_coordinates[1], second_coordinates[1]),
                           min(first_coordinates[0], second_coordinates[0]):
                           max(first_coordinates[0], second_coordinates[0])]
        cv2.imshow('Cutted', img2)
        cv2.imshow('Original', img)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

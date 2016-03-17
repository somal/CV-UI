import cv2
import numpy as np


def find_edges(array):
    numrows = len(array)
    numcols = len(array[0])

    # find first white element starting from the top
    # main loop is rows from 0 to the last
    # inner loop is columns from 0 to the last
    top, _ = find_first(array, 0, numrows, 1, 0, numcols, 1, True)

    # find first white element starting from the bottom
    # main loop is rows from last to the first
    # inner loop is columns from 0 to the last
    bottom, _ = find_first(array, numrows-1, -1, -1, 0, numcols, 1, True)

    # find first white element starting from the left side
    # main loop is columns from 0 to the most right
    # inner loop is rows from 0 to the last
    _, left = find_first(array, 0, numcols, 1, 0, numrows, 1, False)

    # find first white element starting from the left side
    # main loop is columns from the last to thefirst
    # inner loop is rows from 0 to the last
    _, right = find_first(array, numcols-1, -1, -1, 0, numrows, 1, False)
    return top, bottom, left, right


def find_first(array, first_row, second_row, dest1,
               first_column, second_column, dest2, order):
    # look through array until finding first nonzero element
    for row in range(first_row, second_row, dest1):
        for column in range(first_column, second_column, dest2):
            if order and array[row, column] != 0:
                return (row, column)
                break
            elif (not order) and array[column, row] != 0:
                return (column, row)
                break
    # if find nothing, return zeros
    return (0, 0)

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while(1):
        # get frame
        ret, initial_frame = cap.read()
        # reduce size of image
        reduced_image = cv2.resize(initial_frame, None, fx=0.1, fy=0.1,
                                   interpolation=cv2.INTER_LINEAR)
        # convert from BGR to HSV
        hsv_image = cv2.cvtColor(reduced_image, cv2.COLOR_BGR2HSV)
        # boundaries of color to find
        lower_blue = np.array([110, 100, 100])
        upper_blue = np.array([150, 255, 255])
        # select only pixels with color in boundaries
        hsv_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
        # kernel for morphological transformations
        kernel = np.ones((3, 3), np.uint8)
        # erode mask, to reduce noise
        erosion = cv2.erode(hsv_mask, kernel, iterations=1)
        # if necessary, we can apply laplacian,
        # but in this example it works witout it
        # laplacian = cv2.Laplacian(erosion, cv2.CV_64F)

        # get boundary pixels and multiply them by 10
        # because we reduce original image in 10 times
        top, bottom, left, right = find_edges(erosion)
        top = top*10
        bottom = bottom*10
        left = left*10
        right = right*10

        # variable to check, if cropped image is nonzero
        required_piece_exists = True

        if (bottom == 0) or (right == 0):
            required_piece_exists = False
        if required_piece_exists:
            crop_image = initial_frame[top:bottom, left:right]
            cv2.imshow('Blue_object', crop_image)
        cv2.imshow('Original image', initial_frame)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

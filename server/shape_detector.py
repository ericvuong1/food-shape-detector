import cv2
import numpy as np
import imutils
from collections import Counter

AREA_ERR = 1000

def most_frequent(List):
    if not List:
        return "Undetectable!"
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

def detect_shape():
    img = cv2.imread("newImage.png")
    # img = cv2.imread("newImage.png")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # threshold the image, then perform a series of erosions +
    # dilations to remove any small regions of noise
    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    
    # find contours in thresholded image, then grab the largest
    # one
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # c = max(cnts, key=cv2.contourArea)
    contours = cnts

    # t = 200

    # _, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
    # _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    height, width, channels = img.shape 
    img_area = height * width

    shapes = []
    for cnt in contours:
        area = cv2.contourArea(cnt)

        # ignore noise
        if area < 1000:
            continue
        
        # avoid whole img contour
        if abs(img_area - area) < 2000:
            continue

        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        cv2.drawContours(img, [approx], 0, (0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if len(approx) == 3:
            shape = 'Triangle'
        elif len(approx) == 4:
            shape = 'Rectangle'
        elif len(approx) == 5:
            shape = 'Pentagon'
        elif 6 < len(approx) < 15:
            shape = 'Ellipse'
        else:
            shape = 'Circle'
        shapes.append(shape)

    # cv2.imshow('hi', img)
    # cv2.waitKey()
    print('Detected: ', most_frequent(shapes))
    return most_frequent(shapes)

# detect_shape()




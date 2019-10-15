import cv2
import numpy as np
from collections import Counter

AREA_ERR = 1000

def most_frequent(List):
    print('HI', List)
    if not List:
        return "Undetectable!"
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

def detect_shape():
    img = cv2.imread("newImage.png", cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread("newImage.png")

    t = 200

    # gray = cv2.cvtColor(src = img, code = cv2.COLOR_BGR2GRAY)
    # blur = cv2.GaussianBlur(src = gray, 
    #     ksize = (5, 5), 
    #     sigmaX = 0)
    # (t, binary) = cv2.threshold(src = blur,
    #     thresh = t, 
    #     maxval = 255, 
    #     type = cv2.THRESH_BINARY)
    # (_, contours, _) = cv2.findContours(image = binary, 
    #     mode = cv2.RETR_EXTERNAL,
    #     method = cv2.CHAIN_APPROX_SIMPLE)
    _, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    height, width = img.shape 
    img_area = height * width

    shapes = []
    print('contours', contours)
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
    print(most_frequent(shapes))
    return most_frequent(shapes)


''' 
Problem Statement : To build a Cartoonifier using Python
                    Using OpenCV - Open Source Computer Vision wrrite in C++
                    cv,cv2
Use Case - for real-time computer vision

Approach : 1. Convert to GrayScale
           2. Blur it
           3. Extract Edges
           4. Blur Colored IMage
           5. Add mask with edges
'''

import cv2
def make_cartoon(path):
    img = cv2.imread(path)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,9)
    edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,8)

    color = cv2.bilateralFilter(img,9,300,300)
    cartoon = cv2.bitwise_and(color,color,mask=edges)

    return cartoon
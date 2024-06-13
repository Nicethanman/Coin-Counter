import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def empty(a):
    pass

cv2.namedWindow("Settings")
cv2.createTrackbar("Threshold1", "Settings", 229, 255, empty)
cv2.createTrackbar("Threshold2", "Settings", 199, 255, empty)

def preProcessing(img):

    imgPre = cv2.GaussianBlur(img, (5,5), 3)

    # Uncomment to recalibrate thresholds
    thresh1 = cv2.getTrackbarPos("Threshold1", "Settings")
    thresh2 = cv2.getTrackbarPos("Threshold2", "Settings")
    imgPre = cv2.Canny(imgPre, thresh1, thresh2)
    kernel = np.ones((3,3), np.uint8)
    imgPre = cv2.dilate(imgPre, kernel, iterations=1)
    imgPre = cv2.morphologyEx(imgPre, cv2.MORPH_CLOSE, kernel)

    return imgPre


while True:  
    totalMoney = 0
    success, img = cap.read()
    imgPre = preProcessing(img)
    contours, hiearchy = cv2.findContours(imgPre, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0,255,0), 2)

    # dime: ~2000-2500, nickel: ~2900-3300, quarter 3600-4100, loonie: 4250-4950, toonie: 4950-5700

    if contours:
        for contour in contours:
            coinArea = cv2.contourArea(contour)
            # print(coinArea)
            if coinArea < 2500 and coinArea > 2000:
                totalMoney += 0.10
            elif coinArea < 3300 and coinArea > 2900:
                totalMoney += 0.05
            elif coinArea < 4100 and coinArea > 3600:
                totalMoney += 0.25
            elif coinArea < 4950 and coinArea > 4250:
                totalMoney += 1
            elif coinArea < 5700 and coinArea >= 4950:
                totalMoney += 2

    print(totalMoney)

    cv2.imshow("Image", img)
    cv2.imshow("Image Pre process", imgPre)
    cv2.waitKey(1)
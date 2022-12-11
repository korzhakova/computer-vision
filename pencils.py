import numpy as np
import cv2

pencils = 0
cv2.namedWindow('image', cv2.WINDOW_KEEPRATIO)
for i in range(1, 13):
    image = cv2.imread(f'Desktop/study/3/computer-vision/img/images/img ({i}).jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (15,15), 0)
    mask = np.ones((3, 3))
    ret, thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    thresh = cv2.erode(thresh, mask, iterations=3)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(1, len(contours)):
        perimeter = cv2.arcLength(contours[i], True)
        if perimeter > 5000:
            print(perimeter)
            pencils += 1
            cv2.drawContours(image, contours, i, (255, 0, 0), 6) 
    cv2.imshow('image', image)
    cv2.waitKey(0)
    
print(f"Количество карандашей: {pencils}")
cv2.destroyAllWindows()




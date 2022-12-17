import cv2
import numpy as np
import random

def center(hsv, lower, upper):
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
    if len(contours) == 3:
        c = max(contours, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)

        if radius > 10:
            return [x, y], radius
    
    return None

green_lower = np.array([50, 120, 155])
green_upper = np.array([70, 140, 190])

red_lower = np.array([0, 160, 140])
red_upper = np.array([10, 190, 160])

blue_lower = np.array([95, 170, 130])
blue_upper = np.array([117, 190, 150])

cam = cv2.VideoCapture(0)
cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)
cam.set(cv2.CAP_PROP_AUTO_EXPOSURE, -1)
cam.set(cv2.CAP_PROP_EXPOSURE, 0)

colors = ['blue', 'red', 'green']
sequence = random.sample(colors, 3)

balls = 0

print(sequence)

while cam.isOpened():
    balls = 0
    
    ret, frame = cam.read()
    blurred = cv2.GaussianBlur(frame, (21, 21), 0)
    
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    green = center(hsv, green_lower, green_upper)
    red = center(hsv, red_lower, red_upper)
    blue = center(hsv, blue_lower, blue_upper)
    
    if green:
        g_cy = int(green[0][1])
        g_cx = int(green[0][0])
        r = int(green[1])
        cv2.circle(frame, (g_cx, g_cy), r,(0, 255, 0), 3)
        balls += 1
        
    if red:
        r_cy = int(red[0][1])
        r_cx = int(red[0][0])
        r = int(red[1])
        cv2.circle(frame, (r_cx, r_cy), r,(0, 0, 255), 3)
        balls += 1
        
    if blue:
        b_cy = int(blue[0][1])
        b_cx = int(blue[0][0])
        r = int(blue[1])
        cv2.circle(frame, (b_cx, b_cy), r,(255, 0, 0), 3)
        balls += 1
    
    key = cv2.waitKey(1)
    if(key == ord('q')):
        break
    
    if balls == 3:
        order = []
        if r_cx > b_cx:
            if r_cx > g_cx:
                if b_cx > g_cx:
                    order = ['green', 'blue', 'red']
                else:
                    order = ['blue', 'green', 'red']
            else: 
                order = ['blue', 'red', 'green']
        
        elif r_cx > g_cx:
            order = ['blue', 'red', 'green']
        
        elif b_cx > g_cx:
            order = ['red', 'green', 'blue']
        
        else:
            order = ['red', 'blue', 'green']

        if order == colors:
            print('Правильно!')
        
        else:
            print('Неправильно!')
 
    cv2.imshow('frame', frame)
    
cam.release()
cv2.destroyAllWindows()

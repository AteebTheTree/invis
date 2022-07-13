import numpy as np
import cv2
import time
print('hi i just started')

cap = cv2.VideoCapture(0)
time.sleep(2)
background = 0
print('Just initialized stuff')

for i in range(50):
    ret, background = cap.read()
print('this loop is done')

while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])

    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2
    print('this second loop is going')

    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8), iterations = 2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE,np.ones((3,3),np.uint8), iterations = 1)
    print('just morphed feeling cool')

    mask2 =cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background, background, mask=mask1)
    print('mic check hoes')

    res2 = cv2.bitwise_and(img,img,mask=mask2)
    final_output = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow('Invisible Cloak',final_output)
    k = cv2.waitKey(10)
    if k==27:
        sys.exit()
cap.release()
cv2.destroyAllWindows()

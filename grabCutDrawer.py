import numpy as np
import cv2

rect = (0,0,0,0)
startPoint = False
endPoint = False
img_counter = 0

# function for mouse callback
def on_mouse(event,x,y,flags,params):
    global rect,startPoint,endPoint

    # get mouse click
    if event == cv2.EVENT_LBUTTONDOWN:

        if startPoint == True and endPoint == True:
            startPoint = False
            endPoint = False
            rect = (0, 0, 0, 0)

        if startPoint == False:
            rect = (x, y, 0, 0)
            startPoint = True
        elif endPoint == False:
            rect = (rect[0], rect[1], x, y)
            endPoint = True


#cap = cv2.VideoCapture("YourVideoFile.mp4")

#capturing the camera feed, '0' denotes the first camera connected to the computer
cap = cv2.VideoCapture(0)
waitTime = 50

#Reading the first frame
(grabbed, frame) = cap.read()

while(cap.isOpened()):

    (grabbed, frame) = cap.read()

    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame', on_mouse)

    #drawing rectangle
    if startPoint == True and endPoint == True:
        cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (255, 0, 255), 2)

    if not grabbed:
        break
    cv2.imshow('frame',frame)

    key = cv2.waitKey(waitTime)
    if key == 27:
        #esc pressed
        break

    elif key % 256 == 32:
        # SPACE pressed
        alpha = 1  # Transparency factor.

        img_name = "opencv_frame_{}.png".format(img_counter)

        imgCopy = frame.copy()
        img = frame

        mask = np.zeros(img.shape[:2], np.uint8)

        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)
        w = abs(rect[0]-rect[2]+10)
        h= abs(rect[1]-rect[3]+10)
        rect2 = (rect[0]+10, rect[1]+10,w ,h )

        cv2.grabCut(img, mask, rect2, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        img = img * mask2[:, :, np.newaxis]

        cv2.imwrite(img_name, img )
        print("{} written!".format(img_name))
        img_counter += 1

cap.release()
cv2.destroyAllWindows()






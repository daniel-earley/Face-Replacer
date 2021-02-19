import cv2
import os

# File Paths
xmlName = 'haarcascade_frontalface_default.xml'
resourcePath = os.path.dirname(__file__)
resourcePath = os.path.join(resourcePath, 'resources')
xmlPath = os.path.join(resourcePath, xmlName)
replaceImg = os.path.join(resourcePath, 'Red Ranger Green Cropped.png')
newImg = cv2.imread(replaceImg)

# Need cascade classifier to read the haarcascade xml
cascade = cv2.CascadeClassifier(xmlPath)

# Capture Webcam
webcam = cv2.VideoCapture(0)

# Loop to capture video
while True:
    # Capture and convert frames to grayscale
    unusedVar, img = webcam.read()
    grayscaleFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(grayscaleFrame, 1.1, 15)


    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    newImg = cv2.cvtColor(newImg, cv2.COLOR_BGR2BGRA)

    # Draw a rectangle over the detected face
    for (x,y,w,h) in faces:
        newImg = cv2.resize(newImg, (w,h))
        img[y:y+w, x:x+h] = newImg
        # cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
        
    

    # for i in range(0, w):
    #     for j in range(0, h):
    #         if newImg[i,j][2] != 0:
    #             img[y+i, x+j] = newImg[i, j]
    cv2.imshow('img', img)

    key = cv2.waitKey(30) & 0xff
    if key == ord(']'):
        break

webcam.release()

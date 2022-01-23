import pygame as pg
import sys
import cv2
from pygame.locals import *

# Inits
pg.init()

# File Paths
xmlName = './resources/haarcascade_frontalface_default.xml'

# Need cascade classifier to read the haarcascade xml
cascade = cv2.CascadeClassifier(xmlName)

# Setup pygame window and webcam
W, H = 640, 480
screen = pg.display.set_mode((W, H))
webcam = cv2.VideoCapture(0)

# Main Loop
while True:
    # Use Webcam to detect face
    unusedVar, cvImg = webcam.read()
    cv2.imwrite("./resources/frame.jpg", cvImg)
    grayscale = cv2.cvtColor(cvImg, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(grayscale, 1.1, 15)

    # Load webcam footage and replacement image
    camImg = pg.image.load("./resources/frame.jpg")
    newImg = pg.image.load("./resources/default.png")
    screen.blit(camImg, (0,0))

    # Draw a rectangle over detected face
    for (x,y,w,h) in faces:
        newImg = pg.transform.scale(newImg, (w*2, h*2))
        screen.blit(newImg, (x/2, y/2))

    # Update Display
    pg.display.update()

    # check for exit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            webcam.release()
            sys.exit()
    


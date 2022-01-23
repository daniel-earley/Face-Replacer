# Presenting Face-Replacer 
Have you ever seen a Vtuber and thought, "hey that looks cool I want to try that!". Then have you ever looked into the process and thought, "wow that's a lot of work". Well I present to you Face-Replacer! An easy to use program that will allow you to become a pngtuber! This python script will detect your face and place an image of your choosing over your face in real time! 

## Implementation
This program uses a combination of OpenCV and Pygame working in tandem. OpenCV allows us to use haar cascade facial detection with a webcam to constantly detect and output the coordinates of the user's face. Pygame allows us to show the webcam footage and overlay the respective image in a window. There is however, another reason for using pygame. Whilst OpenCV can output the webcam footage and overlay the respective image over the user's face in it's own window, the result is a slowly blurring image being overlayed over the webcam footage. Since pygame is primarily a game development tool, it allows for clean animation without blurry artifacts. Essentially, the program is animating the user's face as well as the respective image.

## Requirements
1. Python 3
2. Pygame
3. OpenCV
4. Webcam
5. A png 

## How to Use


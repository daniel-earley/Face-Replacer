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
1. Download or clone the repo using this link: https://github.com/daniel-earley/Face-Replacer.git or by clicking the green Code button.
    a. If you downloaded the repo, then you will need to unzip the files
2. Open the resources folder and replace *default.png* with any png file of your choice. Ensure that the file is named *default.png*

## Running the program
There are a couple of options for running the file.
1. Navigate to the folder that has replace_face.py. Next open your terminal and type "python replace_face.py" without the quotation marks.
2. Using a text editor or ide such as VSCode, navigate to the folder that has replace_face.py and open the file. Next press shift + f5 OR click the run button.

## Extra Notes
If your image doesn't properly line up on your face then there are a couple of ways you can try to fix this issue. For one thing you can feel free to edit the code to your heart's content, the program is pretty simple after all. If you're going to edit the code then you'll want to edit the w and h of this line ``newImg = pg.transform.scale(newImg, (w*2, h*2))``
Otherwise you can also manually edit your png image, centering or scaling as you please.

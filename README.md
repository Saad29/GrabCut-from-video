# GrabCut-from-video
GrabCut is an algorithm which removes the background in an image from a selected part of the image.In the OpenCV sample , the implementation works only for a single image and the area for selecting the foreground is fixed. This program allows you to select an area according to your wish from a video file or a camera feed.

The openCV implementation can be here : https://docs.opencv.org/3.4/d8/d83/tutorial_py_grabcut.html


So the steps are simple:
1. Either have a webcam or camera connected to your computer
2. OR have a video file in the same folder as this code (you have to include the file name in the code)
3. Run the code
4. Click on the video feed two times for drawing a reactangle. This will be the area of interest. The two points maybe the vertices of the rectangle.
5. Press space ,and an image with the grabcut algorithm applied on the video frame wil be saved. 
6. Continue steps 4 and 5 untill the video ends oryou have captured all areas of interest.

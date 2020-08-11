# hand_ai
### A program which can be implemented in online classes, to detect when a student is raising their hand.

This AI model was made in https://teachablemachine.withgoogle.com/ and then it was exported
into a .h5 file and then using [CV2](https://pypi.org/project/opencv-python/) it takes a photo
using your webcam. It saves it and then analyses it, prints what it thinks it is and deletes the photo.

# Credit

If you want to use this for something, open a issue describing what you want to use it for and I will review it.

# Usage

(It takes some time to load and initialize and this has been trained on me so it may not work for you)

![IMAGE](https://raw.githubusercontent.com/lepythoner/hand_ai/master/images/cv.jpg)
![IMAGE2](https://raw.githubusercontent.com/lepythoner/hand_ai/master/images/Capture.png)

Try to have a plain white background and a lightly lit place.

# Troubleshooting

If you get a error like this:

```
    cv2.imwrite("cv.jpg", image)
cv2.error: OpenCV(4.3.0) C:\opencv\modules\imgcodecs\src\loadsave.cpp:738: error: (-215:Assertion failed) !_img.empty() in function 'cv::imwrite'
```

Try running the program a few more times, and if that **doesn't work** open a issue with a bug label.

# Why isn't this in my_python_scripts?

I thought that this is a little bigger, and 
its not really a script and it's a thing on it's own, so I thought it deserves a repository of it's own.







Thanks for having a look at this,



_**By Sahal Mulki**_

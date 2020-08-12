# hand_ai
### A program which can be implemented in online classes, to detect when a student is raising their hand.

# How it was made:

### Summary:

This AI model was made in https://teachablemachine.withgoogle.com/ and then it was exported
into a .h5 file and then using [CV2](https://pypi.org/project/opencv-python/) it takes a photo
using your webcam. It saves it and then analyses it, prints what it thinks it is and deletes the photo.

### AI specifications:

**V1.00 has been trained on:**

50 Epochs  
Batch size : 16  
Learning rate : 0.001  

**V1.50 has been trained on:**

100 Epochs (for better performance)  
Batch size : 16  
Learning rate : 0.001  

### Libraries:

tensorflow  
Pillow  
numpy  
opencv-python  

# Credit

If you want to use this (for your own program not just for having a look at it or running it) for something, open a issue describing what you want to use it for and I will review it.

# Installation

Install all the needed packages by using

```
pip install requiremens.txt
```

in the folder in which requirements.txt is located in.
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

# I dont have Python !

There's a easier way to view the Model than python, you can also have a look at this link :

https://teachablemachine.withgoogle.com/models/8AXz2b2O1/
  
  



  
  
Thanks for having a look at this,



_**By Sahal Mulki**_

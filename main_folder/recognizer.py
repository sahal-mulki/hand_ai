print("Loading...")

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
from cv2 import *
import time
import os
import platform

print("Initializing...")

camera_port = 0
camera = cv2.VideoCapture(camera_port)
time.sleep(1)  # If you don't wait, the image will be dark
return_value, image = camera.read()
cv2.imwrite("cv.jpg", image)
del(camera)  # so that others can use the camera as soon as possible

np.set_printoptions(suppress=True)#Suppression of scientific notation

model = tensorflow.keras.models.load_model('keras_model.h5')

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

image = Image.open('cv.jpg')
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)
image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
data[0] = normalized_image_array

prediction = model.predict(data)

#Super complicated conversion and comparison process starts
predic_to_list = prediction.tolist()
predic2 = predic_to_list[0]

predic3 = str(predic2)
predic3 = predic3.replace("[", "")
predic3 = predic3.replace("]", "")
predic4 = predic3.replace(",", "") 
predic5 = predic4.split(" ")

result1 = float(predic5[0])
result2 = float(predic5[1])

list1 = [result1, result2]

if result1 < result2:
    FINAL = result2
elif result2 < result1:
    FINAL = result1
    
FINAL2 = FINAL * 100
#Super complicated conversion and comparison process ends

if FINAL == result1:
    name_of_pose = "neutral"
elif FINAL == result2:
    name_of_pose = "raising your hand"

if platform.system() == "Windows":
    os.system("del cv.jpg")

else:
    os.system("unlink test_photo.jpg")
print("I am " + str(FINAL2) + " percent sure that you are " + name_of_pose)

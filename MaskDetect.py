import cv2
import cvlib as cv
import tensorflow as tf
import numpy as np
from keras.applications.resnet import preprocess_input
from keras_preprocessing.image import load_img, img_to_array

img2 = cv2.imread('./static/tesla.jpg')

img = load_img('./static/tesla.jpg', target_size=(224, 224))
x = img_to_array(img)
print(x.shape)
x = np.expand_dims(x, axis=0)
print(x)
print(x.shape)
x = preprocess_input(x)
print(x)
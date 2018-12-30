import tensorflow as tf
import cv2
import pytesseract
from skimage.io import imread
from keras.preprocessing import image

def detect(frame):
    try:  
    img  = Image.open("imagetext.jpg")  
    except IOError: 
    pass
    #frame=cv2.imread("imagetext.jpg")
    data = detect(frame)
    print(data)
    

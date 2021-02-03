import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential, load_model
from PIL import Image
from numpy import asarray
import numpy as np
import imageio
import cv2
from tkinter import messagebox

class TModel():
    
    def __init__(self,model_path):
        self.model=tf.keras.models.load_model(model_path)
        self.Categories = ["no se encontraron autos","Se encontraron autos"]

    def prepare(self,filepath):
        img = Image.open(filepath)  
        img = img.resize((224,224))
        data = np.asarray(img)
        data = np.expand_dims(data,axis=0)
        data= tf.keras.applications.vgg16.preprocess_input(data)
        return data

    def PredictImg(self,filepath):
        self.prediction = self.model.predict([self.prepare(filepath)])
        print(self.prediction[0][0])
        print(self.Categories[int(self.prediction[0][0])])
        messagebox.showinfo(message=self.Categories[int(self.prediction[0][0])], title="Prediccion")

    def getPrecision(self):
        return self.prediction[0][0]
    
    def getResultado(self):
        return self.Categories[int(self.prediction[0][0])]
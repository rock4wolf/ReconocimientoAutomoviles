import numpy as numpy
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
import itertools
import os
import os.path
import shutil
import random
import glob
import matplotlib.pyplot as plt
import warnings
from tkinter import simpledialog
from tkinter import messagebox 


class TrainModel():
    def __init__(self,CTrainPath,CValPath,CTestPath,NCTrainPath,NCValPath,NCTestPath):
        self.CTrainPath=CTrainPath
        self.CValPath=CValPath
        self.CTestPath=CTestPath
        self.NCTrainPath=NCTrainPath
        self.NCValPath=NCValPath
        self.NCTestPath=NCTestPath
        self.moveImg()
    
    def moveImg(self):
        #carpeta de coches
        os.chdir(self.CTrainPath)
        for c in random.sample(glob.glob(os.getcwd()+'/*'), 100):
            shutil.move(c,self.CValPath)
        for c in random.sample(glob.glob(os.getcwd()+'/*'), 50):
            shutil.move(c,self.CTestPath)
        os.chdir(self.NCTrainPath)
        for c in random.sample(glob.glob(os.getcwd()+'/*'), 100):
            shutil.move(c,self.NCValPath)
        for c in random.sample(glob.glob(os.getcwd()+'/*'), 50):
            shutil.move(c,self.NCTestPath)
        os.chdir('../../')
        train_paths = 'cars_train'
        valid_Path = 'validation'
        test_path = 'test'

        self.train_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input)\
            .flow_from_directory(directory=train_paths,target_size=(224,224),classes=['cars_train','NoCar'],batch_size=10)
        self.valid_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input)\
            .flow_from_directory(directory=valid_Path,target_size=(224,224),classes=['Cars','NoCars'],batch_size=10)
        self.test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input)\
            .flow_from_directory(directory=test_path,target_size=(224,224),classes=['Cars','NoCars'],batch_size=10,shuffle=False)
        assert self.valid_batches.n==200
        assert self.test_batches.n==100
        assert self.valid_batches.num_classes == self.test_batches.num_classes == 2
        imgs, labels = next(self.train_batches)
        self.CreateModel()

#plotImages(imgs)
#print(labels)

    def CreateModel(self):
        #crear modelo
        model = Sequential([
        Conv2D(filters=32, kernel_size=(3, 3), activation='relu', padding = 'same', input_shape=(224,224,3)),
        MaxPool2D(pool_size=(2, 2), strides=2),
        Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding = 'same'),
        MaxPool2D(pool_size=(2, 2), strides=2),
        Flatten(),
        Dense(units=2, activation='softmax')
        ])
        model.summary()
        model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
        model.fit(x=self.train_batches,
        steps_per_epoch=len(self.train_batches),
        validation_data=self.valid_batches,
        validation_steps=len(self.valid_batches),
        epochs=10,
        verbose=2
        )
        #Predict
        test_imgs,test_labels=next(self.test_batches)
        #plotImages(test_imgs)
        print(test_labels)
        self.test_batches.classes
        predictions = model.predict(x=self.test_batches,verbose=0)
        numpy.round(predictions)
        self.cm = confusion_matrix(y_true=self.test_batches.classes, y_pred=numpy.argmax(predictions, axis=-1))
        respuesta=messagebox.askyesno(message="desea guardar el modelo creado?",title="guardar modelo")
        if respuesta == True:
            self.USER_INP = simpledialog.askstring(title="guardar modelo",prompt="nombre de modelo para guardar")
            self.SaveModel(self.USER_INP)



    def plot_confusion_matrix(self,cm, classes,
                            normalize=False,
                            title='confution matrix',
                            cmap=plt.cm.Blues):
        plt.imshow(cm,interpolation='nearest',cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks=numpy.arange(len(classes))
        plt.xticks(tick_marks,classes,rotation=45)
        plt.yticks(tick_marks,classes)
        
        if normalize:
            cm = cm.astype('float')/ cm.sum(axis=1)[:,numpy.newaxis]
            print("normalized confusion matrix")
        else:
            print('confusion matrix, without normalization')
        print(cm)
        thresh=cm.max()/2.
        for i,j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
            plt.text(j,i,cm[i,j],
                    horizontalalignment="center",
                    color="white" if cm[i,j]>thresh else "black")
        plt.tight_layout()
        plt.ylabel('true label')
        plt.xlabel('predicted label')

#test_batches.class_indices
    def TestplotCM(self):
        cm_plot_labels = ['autos','no autos']
        plot_confusion_matrix(cm=cm,classes=cm_plot_labels,title='confution matrix')

    def SaveModel(self,modelname):
        self.model.save(modelname+'.model')
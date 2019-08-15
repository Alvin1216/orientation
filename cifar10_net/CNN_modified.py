# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:12:37 2019

@author: user
"""

import numpy as np
#modified CNN
from matplotlib import pyplot as plt
from keras.models import Model
from keras.optimizers import Adam
from keras.layers import Input, Dense, Conv2D, AveragePooling2D, MaxPool2D, Flatten, Activation,Dropout
from keras.datasets import cifar10
from keras.utils import np_utils
from keras.layers import BatchNormalization as BN
%matplotlib inline

def show_data(data, label, rows=2, cols=5):
    fig,ax = plt.subplots()
    fig.set_size_inches(12, 4)
    fig.subplots_adjust(hspace=0.8, wspace=0.8)
    for idx in range(1, (rows*cols)+1):
        plt.subplot(rows, cols, idx)
        plt.imshow(data[idx-1])
        plt.title("Lable=%s"%label[idx-1])
        
def save_history(file_name,training_history):
     with open(file_name, 'wb') as file_pi:
        pickle.dump(training_history.history, file_pi)
        
def print_history(file_name):
    with open(file_name, 'rb') as file:
        a_dict1 =pickle.load(file)
        print(a_dict1)
        
        
def lenet():
    input_layer = Input(shape=(32,32,3))
    x = Conv2D(filters=6, kernel_size=(5,5))(input_layer)
    x = Activation('relu')(x)
    x = MaxPool2D()(x)
    x = Conv2D(filters=16, kernel_size=(5,5))(x)
    x = Activation('relu')(x)
    x = MaxPool2D()(x)
    x = Flatten()(x)
    x = Dense(128, activation='relu')(x)
    x = Dense(84, activation='relu')(x)
    output_layer = Dense(10, activation='softmax')(x)
    model = Model(input_layer, output_layer)
    model.compile(optimizer='Adagrad', loss='categorical_crossentropy', metrics=['accuracy'])
    model.summary()
    return model

def lenet3x3():
    input_layer = Input(shape=(32,32,3))
    x = Conv2D(filters=6, kernel_size=(3,3))(input_layer)
    x = Activation('relu')(x)
    x = MaxPool2D()(x)
    x = Conv2D(filters=16, kernel_size=(3,3))(x)
    x = Activation('relu')(x)
    x = MaxPool2D()(x)
    x = Flatten()(x)
    x = Dense(128, activation='relu')(x)
    x = Dense(84, activation='relu')(x)
    output_layer = Dense(10, activation='softmax')(x)
    model = Model(input_layer, output_layer)
    model.compile(optimizer='Adagrad', loss='categorical_crossentropy', metrics=['accuracy'])
    model.summary()
    return model

def lenet_modified_twoConv():
    input_layer = Input(shape=(32,32,3))
    x = Conv2D(filters=32, kernel_size=(3,3))(input_layer)
    x = Activation('relu')(x)
    x = Conv2D(filters=32, kernel_size=(3,3))(x)
    x = Activation('relu')(x)
    x = MaxPool2D()(x)
    x = Conv2D(filters=64, kernel_size=(3,3))(x)
    x = Activation('relu')(x)
    x = Conv2D(filters=64, kernel_size=(3,3))(x)
    x = Activation('relu')(x)
    x = MaxPool2D()(x)
    x = Flatten()(x)
    output_layer = Dense(10, activation='softmax')(x)
    model = Model(input_layer, output_layer)
    model.compile(optimizer='Adagrad', loss='categorical_crossentropy', metrics=['accuracy'])
    model.summary()
    return model

def lenet3x3_withBN():
    input_layer = Input(shape=(32,32,3))
    x = BN()(input_layer)
    x = Conv2D(filters=6, kernel_size=(3,3))(x)
    x = BN()(x)
    x = Activation('relu')(x)
    x = MaxPool2D()(x)
    x = Conv2D(filters=16, kernel_size=(3,3))(x)
    x = BN()(x)
    x = Activation('relu')(x)
    x = MaxPool2D()(x)
    x = Flatten()(x)
    x = Dense(128, activation='relu')(x)
    x = BN()(x)
    x = Dense(84, activation='relu')(x)
    x = BN()(x)
    output_layer = Dense(10, activation='softmax')(x)
    model = Model(input_layer, output_layer)
    model.compile(optimizer='Adagrad', loss='categorical_crossentropy', metrics=['accuracy'])
    model.summary()
    return model
    

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
idx = np.random.randint(0, x_train.shape[0], (10,))
show_data(x_train[idx], y_train[idx])


#pre_processing
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.


# 將y 轉換為One hot encoding
fit_y_train = np_utils.to_categorical(y_train)
pred_y_test = np_utils.to_categorical(y_test)

trianing_history = lenet3x3().fit(x=x_train, y=fit_y_train, validation_data=[x_test, pred_y_test], epochs=5, batch_size=64)
save_history("lenet3x3_result_5epochs",trianing_history)
trianing_history = lenet_modified_twoConv().fit(x=x_train, y=fit_y_train, validation_data=[x_test, pred_y_test], epochs=5, batch_size=64)
save_history("lenet_modified_twoConv_5epochs",trianing_history)
trianing_history = lenet().fit(x=x_train, y=fit_y_train, validation_data=[x_test, pred_y_test], epochs=5, batch_size=64)
save_history("lenet_5epochs",trianing_history)
trianing_history = lenet3x3_withBN().fit(x=x_train, y=fit_y_train, validation_data=[x_test, pred_y_test], epochs=5, batch_size=64)
save_history("lenet3x3_withBN_5epochs",trianing_history)




##lenet

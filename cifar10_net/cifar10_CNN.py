# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:13:03 2019

@author: user
"""

import numpy as np
from matplotlib import pyplot as plt
from keras.models import Model
from keras.optimizers import Adam
from keras.layers import Input, Dense, Conv2D, AveragePooling2D, MaxPool2D, Flatten, Activation
from keras.datasets import cifar10
from keras.utils import np_utils
%matplotlib inline

def show_data(data, label, rows=2, cols=5):
    fig, ax = plt.subplots()
    fig.set_size_inches(12, 4)
    fig.subplots_adjust(hspace=0.8, wspace=0.8)
    for idx in range(1, (rows*cols)+1):
        plt.subplot(rows, cols, idx)
        plt.imshow(data[idx-1])
        plt.title("Lable=%s"%label[idx-1])

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
idx = np.random.randint(0, x_train.shape[0], (10,))
show_data(x_train[idx], y_train[idx])

input_layer = Input(shape=(32,32,3))
conv1 = Conv2D(filters=6, kernel_size=(3,3))(input_layer)
conv1_activate = Activation('relu')(conv1)
cpool1 = AveragePooling2D()(conv1_activate)
conv2 = Conv2D(filters=16, kernel_size=(3,3))(cpool1)
conv2_activate = Activation('relu')(conv2)
cpool2 = AveragePooling2D()(conv2_activate)
conv3 = Conv2D(filters=16, kernel_size=(3,3))(cpool2)
conv3_activate = Activation('relu')(conv3)
cpool3 = AveragePooling2D()(conv3_activate)
flat_v = Flatten()(cpool3)
dense1 = Dense(64, activation='relu')(flat_v)
dense2 = Dense(32, activation='relu')(dense1)
output_layer = Dense(10, activation='softmax')(dense2)
model = Model(input_layer, output_layer)
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# 將y 轉換為One hot encoding
fit_y_train = np_utils.to_categorical(y_train)
pred_y_test = np_utils.to_categorical(y_test)

trianing_history = model.fit(x=x_train, y=fit_y_train, validation_data=[x_test, pred_y_test], epochs=30, batch_size=64)
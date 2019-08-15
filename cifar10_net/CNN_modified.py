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
x = BN()(input_layer)

x = Conv2D(filters=32, kernel_size=(3,3))(x)
x = Activation('relu')(x)

x = Conv2D(filters=32, kernel_size=(3,3))(x)
x = Activation('relu')(x)

x = MaxPool2D()(x)

x = Conv2D(filters=64, kernel_size=(3,3))(x)
x = Activation('relu')(x)

x = Conv2D(filters=64, kernel_size=(3,3))(x)
#x = BN()(x)
x = Activation('relu')(x)

x = MaxPool2D()(x)


x = Flatten()(x)
#x = Dense(512, activation='relu')(x)
#x = BN()(x)
#x = Dense(128, activation='relu')(x)
#x = BN()(x)
output_layer = Dense(10, activation='softmax')(x)
model = Model(input_layer, output_layer)
model.compile(optimizer='Adagrad', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# 將y 轉換為One hot encoding
fit_y_train = np_utils.to_categorical(y_train)
pred_y_test = np_utils.to_categorical(y_test)

trianing_history = model.fit(x=x_train, y=fit_y_train, validation_data=[x_test, pred_y_test], epochs=5, batch_size=64)


model.save("testacc_87_valacc_63.h5")
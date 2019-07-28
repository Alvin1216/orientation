# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 16:25:26 2019

Autoencoder
784>16>2>16>784
測試

@author: user
"""
#import mnist資料集
from keras.datasets import mnist
from keras.models import Model
from keras.layers import Input, Dense
import numpy as np
import matplotlib.pyplot as plt
#畫圖
from matplotlib.pyplot import imshow

#原本是28*28=784 dimension
#要降為2 dimension
#然後再升回去 784 dimension
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#留下原圖
x_train_ori=x_train
x_test_ori=x_test

#先來正規化 把它壓成介於0~1之間
#為什麼是255 因為圖裡面的值都是介於 0~255
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.

#壓平
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

#test
#784>32>16>2>16>32>784
input_img = Input(shape=(784,))
#encoding_layer1=Dense(512, activation='relu')(input_img)
#encoding_layer2=Dense(256, activation='relu')(encoding_layer1)
#encoding_layer3=Dense(128, activation='relu')(input_img)
encoding_layer4=Dense(64, activation='relu')(input_img)
#encoding_layer5=Dense(10, activation='relu')(encoding_layer4)
#encoding_layer=Dense(64, activation='selu')(input_img)
encode=Dense(2)(encoding_layer4)
#encode=Dense(2)(encoding_layer)

decoding_layer1=Dense(64, activation='relu')(encode)
#decoding_layer2=Dense(64, activation='relu')(decoding_layer1)
#decoding_layer=Dense(128, activation='relu')(decoding_layer2)
#decoding_layer4=Dense(256, activation='relu')(decoding_layer3)
#decoding_layer5=Dense(512, activation='relu')(decoding_layer4)
decode=Dense(784, activation='sigmoid')(decoding_layer1)

#進去input 出來decode(encoder和decoder對接)
autoencoder = Model(input_img, decode)

#中間層(encode出來的那一層)
encoder= Model(input_img, encode)

#autoencoder = Model(input_img, decoding_layer)
#autoencoder.compile(optimizer='adam', loss='mse')
autoencoder.compile(optimizer='Adagrad', loss='mse')
autoencoder.fit(x_train,x_train,epochs=10,shuffle=True,batch_size=128,validation_data=(x_test, x_test))

#中間層輸出
#dimension2_layer = Model(inputs=input_img, outputs=autoencoder.layers[2].output)
middle_output = encoder.predict(x_test)
autoencoder_out=autoencoder.predict(x_test)
#encoded_imgs = encoder.predict(x_test)

plt.figure(figsize=(20, 20))
plt.scatter(middle_output[:,0], middle_output[:,1], c=y_test,cmap='viridis')
plt.colorbar()
plt.title("middle_layer output_784-64-10-2-10-64-784")

plt.savefig("middle_layer output_784-64-2-64-784.png")
plt.show()
#plt.savefig("middle_layer output.png")


#把最後結果印出來
n = 10
plt.figure(figsize=(20, 4))
for i in range(n):
    # 原圖
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(x_test[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # 跑model 結果
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(autoencoder_out[i].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()
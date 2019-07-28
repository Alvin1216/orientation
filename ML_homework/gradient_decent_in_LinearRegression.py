# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 17:03:00 2019

@author: user
"""
import random
import matplotlib.pyplot as plt
import numpy as np

#y=ax+b
real_a=3
real_b=2

def produce_random_data(data_size=50):
    #random produce x(from 0~6)
    x=[]
    y=[]
    for i in range(data_size):
        now_x=round(random.uniform(0.5, 6),3)
        biasx=round(random.uniform(0, 1),3)
        biasy=round(random.uniform(0, 1),3)
        now_y=round(real_a*now_x+real_b,3)
        if i%4==0:
            #+-
            now_x=now_x+biasx
            now_y=now_y-biasy
        elif i%4==1:
            #-+
            now_x=now_x-biasx
            now_y=now_y+biasy
        elif i%4==2:
            #--
            now_x=now_x-biasx
            now_y=now_y-biasy
        else:
            #++
            now_x=now_x+biasx
            now_y=now_y+biasy
        x.append(round(now_x,3))
        y.append(round(now_y,3))
        
    #畫圖 draw a picture
    plt.scatter(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    
    return x,y
    
X,Y = np.asarray(produce_random_data())
# Building the model
predict_a = 0
predict_b = 1

learning_rate = 0.0001
epochs = 4000

n = len(X) # Number of elements in X

#loss function:mean of the squares
#loss_function=1/n*sum(math.pow(y_original-y_predict))
#y_orginal and y_predict are vector
#Gradient Descent  with mean squear error
for i in range(epochs):
    loss=0
    Y_ = predict_a*X + predict_b  # Y^ current value
    loss=(1/n)*sum((Y-Y_)**2) #算次方 用**
    D_predict_a = (-2/n) * sum(X * (Y - Y_))  # Derivative wrt predict_a
    D_predict_b = (-2/n) * sum(Y - Y_)  # Derivative wrt predict_b
    predict_a = predict_a - learning_rate * D_predict_a  # Update m
    predict_b = predict_b - learning_rate * D_predict_b  # Update c
    print('epochs='+str(i)+' loss='+str(loss))
    print('predict_a='+str(predict_a)+' predict_b='+str(predict_b))
    
print (m, c)


def numerical_diff(f,x):
    





    

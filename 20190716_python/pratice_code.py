# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 17:30:42 2019

@author: alvin
"""

import pandas as pd
iris = pd.read_csv('iris.csv', encoding='utf-8')
iris.to_csv('iris_output.csv',index=False)
iris_output=pd.read_csv('iris_output.csv', encoding='utf-8')


sample = iris.sample(n=10)
sample.assign(a_ten_times=sample['A']*10)
sample.iloc[:, 0:4].apply(sum)
sample.iloc[:, 0:4].apply(sum, axis=1)

%%timeit 
for row in iris.itertuples():
    print(row)
    
def text_function(row):
    print(row)


%%timeit    
iris.apply(text_function)


from contextlib import contextmanager
import numpy as np
import matplotlib.pyplot as plt

@contextmanager
def myplot(fig, subplot, size=5):
    #fig 大張底圖
    #axes 上面小圖
    #這裡是把大張的底圖都先畫出來，之
    #後要疊加其他的線或是點就比較方便
    ax = fig.add_subplot(subplot)
    ax.set_xlim(-1, 12)
    ax.set_ylim(0, 1)
    ax.set_xlabel('sec')
    ax.set_ylabel('signal')
    ax.grid(True)
    ax.set_xticks(range(10))
    
    
    # Plot the data
    yield ax
    
    title = ax.get_title()
    ax.set_title(title)

fig = plt.figure(figsize=(12, 3))
fig.suptitle('Demo', fontsize=15)

blue = np.random.rand(10) * 0.7 + 0.1
orange = np.random.rand(10) * 0.3 + 0.6

with myplot(fig, 121) as ax:
    ax.plot(blue, color='blue')
    ax.set_title('blue')
    
with myplot(fig, 122) as ax:
    ax.plot(blue, color='blue')
    ax.plot(orange, color='orange')
    ax.set_title('blue & orange')

import numpy as np
from contextlib import contextmanager
import matplotlib.pyplot as plt
@contextmanager
def prf_plot(fig, subplot, size=5):
    #這裡是把大張的底圖都先畫出來，之
    #後要疊加其他的線或是點就比較方便
    ax = fig.add_subplot(subplot)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel('Precision')
    ax.set_ylabel('Recall')
    ax.grid(True)
    
    #f1=Precision * Recall * 2 / (Precision + Recall)
    #從f1回推precision和recall
    #因為底圖給定的值是f1(f1=f)
    #回推得到(Precision=x,Recall=y)
    #f=x*y*2/(x+y)
    #fx+fy=2xy
    #fx=2xy-fy
    #fx=(2x-f)y
    #y=fx/(2x-f)

    ##test

    #f_scores = np.arange(0.1,1,0.1)#start,end,step
    f_scores = np.linspace(0.1, 0.9, num=10)
    for f_score in f_scores:
        x = np.linspace(0.01, 1)###########****
        y = f_score * x / (2 * x - f_score)
        ax.plot(x[y>0], y[y>0], color='gray', alpha=0.2)
    
    
    # Plot the data
    yield ax
    
    title = ax.get_title()
    ax.set_title(title)

# initialize a square figure
fig = plt.figure(figsize=(6, 6))

# using prf_plot as context manager
with prf_plot(fig, 111) as ax:

    # plot the data
    ax.scatter(x=[0.4, 0.6, 0.65, 0.8], 
               y=[0.44, 0.43, 0.5, 0.75], 
               s=[10, 20, 30, 40], # size
               c=[0.3, 0.6, 0.9, 1.0], # scores for colormap
               cmap='viridis')

    # set the title
    ax.set_title('Precision, Recall, and F1')
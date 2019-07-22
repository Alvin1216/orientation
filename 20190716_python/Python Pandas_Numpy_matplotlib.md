# Python Pandas/Numpy/matplotlib
#### 1.Tell the difference of the two files: iris.csv and iris_output.csv
Iris.csv是運用pandas之中的read_csv製作出來的而iris_output.csv是運用pandas.DataFrame中的to_csv製作出來的。兩者分屬不同的類別製造出來的，所以兩者會有不一樣的部分。
兩個file都用read_csv再讀一次之後會發現，iris_output.csv會比iris.csv多了一欄index

```python
import pandas as pd
iris = pd.read_csv('iris.csv', encoding='utf-8');
#iris.to_csv('iris_output.csv');
#上面這行是原本單純轉換csv，儲存之後會多出一欄index，下面的是沒有index的方法
iris.to_csv('iris_output.csv',index=False);
iris_output=pd.read_csv('iris_output.csv', encoding='utf-8')
```

##### 2.How to save the dataframe to iris_output.csv exactly the same with iris.csv
在儲存的時候把index這一欄刪除即可。在Parameters中加上index=False
```python
iris.to_csv('iris_output.csv',index=False)
```

##### 3.Design a simple function to work on one line Compare the difference in speed between applyyy and itertuples
方法1
```python
#itertuples
%%timeit 
for row in iris.itertuples():
    print(row)

#apply
#下方def為我們設計的用於apply的function    
def text_function(row):
    print(row)
%%timeit    
iris.apply(text_function)
```
方法2
```python
iris.columns = ['A', 'B', 'C', 'D', 'class'] 
def text_function(row):
    return 'class: {class}, A:{A},B:{B},C:{C},D:{D}'.format(**row.to_dict())

%%timeit 
print(iris.apply(text_function, axis=1))

%%timeit
for ir in iris.itertuples():
    print(ir)
```

apply用的function是傳入serier<br>
itertuples遞迴中的ir是dataframe<br>


利用上方程式碼跑出來的結果為：<br>
itertuples: 15.8 ms ± 165 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)<br>
apply: 8.15 ms ± 134 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)<br>
apply比iteruples快了將近快一半的時間

##### 4.Write a context manger named "prf_plot" to plot precision/recall/F1
```python
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
```




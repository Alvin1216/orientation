# ML HOMEWORK

### 1.linear regression
![](https://i.imgur.com/oOxDwQc.png)
4000 epoch

predict: Y=2.94433334258391X+1.9612568527701475
real: Y=3X2

### 2.autoencoder

**784-64-2-64-784**
中間層：
![](https://i.imgur.com/l9FVs25.png)

結果圖:
![](https://i.imgur.com/MJ6gT87.png)


**784-64-10-2-10-64-784**
中間層：
![](https://i.imgur.com/u9GnETq.png)

結果圖:
![](https://i.imgur.com/Xh0hSyd.png)

**784-128-64-10-2-10-64-128-784**
中間層：
![](https://i.imgur.com/DkTMA5f.png)

結果圖:
![](https://i.imgur.com/HbXcBcB.png)


#### 討論：
**784-64-32-64-784 vs 784-64-2-64-784**

784-64-32-64-784
![](https://i.imgur.com/majbW7i.png)

784-64-2-64-784
![](https://i.imgur.com/SURyzpA.png)

同樣都是訓練30 epoch，但是中間層的不同導致了不同的結果
中間層 為2 的在4 9 5 這三個數字上表現不太好
中間層 為32 的總體表現就還不錯

我是認為，中間層的神經元太少，導致一下子損失了太多資訊，要復原回來就會比較困難
所以才導致了不同的結果






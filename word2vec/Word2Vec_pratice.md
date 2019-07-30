## Word2Vec
##### Time used on your computer to train with text8
```
from gensim.models import word2vec
#print with log
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# load text8
sentences = word2vec.Text8Corpus("text8")
model = word2vec.Word2Vec(sentences, size=200)
# with skip-gram/embedding dimension=10
model = word2vec.Word2Vec(sentences, size=10,sg=0)
```
result：
It tooks 108.5 s for training 5 epoch
![](https://i.imgur.com/CoD4LYJ.png)


##### How to estimate the time used on your computer to train with full English Wikipedia

with skip-gram:
O=E x T x Q=E x T x (C x (D + D x log2V))
E:訓練epoch數 (不變)
T:word count in corpus(這一大堆文章裡面，單字的字數)
C:Maximum word distance (不變)
D:Dimension of P layer (不變)
V:Size of vocabulary(不重複的單字，用heap's law估算)
O:Training complexity

--->E、C、D不變
--->O只和T和V有正比關係


Heap's law:
VR(n)=Kn^beta
n:全部的字數
K,beta:常數(10<K<100,0.4<beta<0.6)
VR:這堆字裡面，不重複的單字

--->假設K=50 beta=0.5
--->text8 總字數：17005207
--->全部的wikipedia 總字數：3654*10^6
--->VR_text8=50*(17005207)^0.5=206186(約)
--->VR_wikipedia=50*(3654*10^6)^0.5=3022416(約)

因為O只和T和V有正比關係
所以3022416*3654*10^10/206186*17005207=3150(約)
3150*108.5s=341775s
341775/60=5696.25min=94.9375hr=3.96days






	





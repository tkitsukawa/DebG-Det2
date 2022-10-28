# DebG-Det2
Detectron2とDeblurGANを組み合わせ，ブレたマーカーの認識性能を上げる．

物体検出手法のFaster R-CNNで物体検出し、その後検出位置を切り出し正規化、さらにGANによるブレ除去を行ったのちにマーカーの認識を行うことで認識精度を向上させた。
<br> <br>  

## 処理結果
1［m］と2［m］の距離で縦3［cm］横3［cm］のマーカを0.25［m/s］で動かした結果。

![image](https://user-images.githubusercontent.com/64144764/196644677-91a28f5a-1017-4fd1-b9ab-600331fd6cbd.png)


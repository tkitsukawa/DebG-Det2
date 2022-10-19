# DebG-Det2
Detectron2とDeblurGANを組み合わせ，ブレたマーカーの認識性能を上げる．

物体検出手法のFaster R-CNNで物体検出し、その後検出位置を切り出し正規化、さらにGANによるブレ除去を行ったのちにマーカーの認識を行うことで認識精度を向上させた。

![image](https://user-images.githubusercontent.com/64144764/196644367-ae7d3c9e-077d-44d2-b3d2-a4278c204a68.png)

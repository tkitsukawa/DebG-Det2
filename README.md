# DebG-Det2
Detectron2とDeblurGANを組み合わせ，ブレたマーカーの認識性能を上げる．

物体検出手法のFaster R-CNNで物体検出し、その後検出位置を切り出し正規化、さらにGANによるブレ除去を行ったのちにマーカーの認識を行うことで認識精度を向上させた。
![image](https://user-images.githubusercontent.com/64144764/196644033-f599bdba-1747-46d6-a1df-469bea0d4b7e.png)

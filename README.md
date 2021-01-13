# DebG-Det2

# Windows10環境でのDetectron2のインストール方法
## Detectron2とは
FacceBook AI が開発したPytorchベースの物体検出のライブラリ．  
Faster R-CNN や Mask R-CNN といったような高精度なモデルを簡単に利用することができる．
基本的にはLinux環境がインストールの対象となっている．

## Windows10でのインストール方法
以下の順にコマンドプロンプトに打ち込んでいく．

```
$ conda create -n detectron_py36
```
アナコンダ上に仮想環境を作成（今回は仮想環境名を detectron_py36 に指定）

```
conda install pytorch=1.3.0 torchvision=0.4.1 cudatoolkit=10.1 -c pytorch
```
pytorchとtorchvisionのインストール．今回はアナコンダのバージョンが10.1

```
pip install opencv-contrib-python
```
OpenCVのインストール

```
pip install git+https://github.com/facebookresearch/fvcore
```

```
pip install cython
```
cythonのインストール

```
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
```

ファイルの編集，以下は最後でもよい
```
conda install -c anaconda jupyter
```
jupyter notebook を使えるようにする．（必要なら）

この仮想環境にほかのものもインストールすると，Detectron2などインストールしたものが壊れる可能性があるので，この仮想環境はDetectron2用としたほうがいい．

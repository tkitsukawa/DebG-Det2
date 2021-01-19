# DebG-Det2
detectron2をインストールする必要あり

# Windows10環境でのDetectron2のインストール方法
## Detectron2とは
FacceBook AI が開発したPytorchベースの物体検出のライブラリ．  
Faster R-CNN や Mask R-CNN といったような高精度なモデルを簡単に利用することができる．
基本的にはLinux環境がインストールの対象となっている．

## Windows10でのインストール方法
以下の順にコマンドプロンプトに打ち込んでいく．

アナコンダ上に仮想環境を作成（今回は仮想環境名を detectron_py36 に指定）
```
$ conda create -n detectron_py36
```

pytorchとtorchvisionのインストール．今回はアナコンダのバージョンが10.1
```
conda install pytorch=1.3.0 torchvision=0.4.1 cudatoolkit=10.1 -c pytorch
```

OpenCVのインストール
```
pip install opencv-contrib-python
```

fvcoreをインストール
```
pip install git+https://github.com/facebookresearch/fvcore
```

cythonのインストール
```
pip install cython
```

cocoAPIをインストール

```
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
```

以下を，windowsにインストールするために打つ
```
git clone https://github.com/conansherry/detectron2
```

最後にビルドするために以下を打つ
```
cd detectron2
```

```
python setup.py build develop
```



ーーエラーが出たらーー

model_zoo関係のエラーが出たらmodel.zooライブラリを新しくする必要あり．

公式のDetectron2
https://github.com/facebookresearch/detectron2
をダウンロードしてそこのmodel.zooをコピーしてwindows用detectron2のmodel_zooライブラリを置き換える．

その後もう一度ビルドをしたら完了．




ーーおまけーー

jupyter notebook を使えるようにする．（必要なら）
```
conda install -c anaconda jupyter
```



この仮想環境にほかのものもインストールすると，Detectron2などインストールしたものが壊れる可能性があるので，この仮想環境はDetectron2用としたほうがいい．

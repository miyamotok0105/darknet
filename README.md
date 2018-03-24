![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

# 環境

ubuntu    


```
nvcc -v
nvidia-smi
```

# インストール

```
git clone https://github.com/miyamotok0105/darknet.git
cd darknet
```

Makefileの修正    

```
GPU=1に変更
```

```
make
```

# 実行

```
wget https://pjreddie.com/media/files/yolo.weights
./darknet detect cfg/yolo.cfg yolo.weights data/dog.jpg
```

# 閾値を変更

閾値を変更すると、認識される率が変わる。

```
./darknet detect cfg/yolo.cfg yolo.weights data/dog.jpg -thresh 0
```

# voc形式で学習

```
wget https://pjreddie.com/media/files/VOCtrainval_11-May-2012.tar
wget https://pjreddie.com/media/files/VOCtrainval_06-Nov-2007.tar
wget https://pjreddie.com/media/files/VOCtest_06-Nov-2007.tar
tar xf VOCtrainval_11-May-2012.tar
tar xf VOCtrainval_06-Nov-2007.tar
tar xf VOCtest_06-Nov-2007.tar
wget https://pjreddie.com/media/files/voc_label.py
python voc_label.py
cat 2007_train.txt 2007_val.txt 2012_*.txt > train.txt
mkdir backup
wget https://pjreddie.com/media/files/darknet19_448.conv.23
#cfg/voc.dataとcfg/yolo-voc.cfgを環境に合わせて修正。
./darknet detector train cfg/voc.data cfg/yolo-voc.cfg darknet19_448.conv.23
```

# 学習データを作成する

toolを使用して学習データを作る    
https://github.com/miyamotok0105/BBox-Label-Tool    
下記のフォーマットへである必要がある。    

```
#class_num area1 area2 area3 area4
11 10 10 100 100
14 20 20 120 130
```

# 学習データを使って学習

voc_label.pyで正規化、output_label_list.pyで学習するファイル一覧を作成。    

```
mkdir data/sample1
mkdir data/sample1/images
mkdir data/sample1/labels
#imagesにjpg画像を、labelsにtxtを格納する。
#voc_label.pyとoutput_label_list.py内のパスを環境に合わせて修正。
python voc_label.py
python output_label_list.py
#cfg/voc_hoge.dataとcfg/yolo-voc_hoge.cfgを環境に合わせて修正。
./darknet detector train cfg/voc_hoge.data cfg/yolo-voc_hoge.cfg darknet19_448.conv.23
```


# 参照


https://pjreddie.com/darknet/



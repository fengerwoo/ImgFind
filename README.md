### 图中找图
> 基于Python2.7、OpenCV、GD、puzzle 的图片对比查找命令行工具，包含：图中找图、对比图片相似度功能

### 快速上手
* git clone 本项目到磁盘任意位置
* 安装Python2.7环境
* 执行命令安装以下库

```
pip install argparse
pip install aircv
pip install opencv-contrib-python==3.4.2.16

如果numpy出现问题报错，可能是版本太高，不影响情况下可以适当降降
pip install numpy==1.14.5

安装gd2、puzzle库
Ubuntu：apt-get install libgd-dev libpuzzle-dev
Mac：brew install libgd libpuzzle

pip install pypuzzle
```

### 命令行调用

图中找图
```
BigImgPath = 大图片路径
SmallImgPath = 小图片路径

python main.py -a bfs -big <BigImgPath> -small <SmallImgPath>

示例
python main.py -a bfs -big /user/big.png -small /user/small.png
```

获取图片指纹
```
cvevImgPath = 要获取指纹的图片路径

python main.py -acvev -evimg <cvevImgPath>

示例
python main.py -a cvev -evimg /user/big.png
```

比对图片指纹
```
cvevA = 第一个图片指纹字符串
cvevB = 第二个图片指纹字符串

python main.py -a match -eva <cvevA> -evb <cvevB>

示例
python main.py -a match -eva 35:66:22 -evb 35:66:22
```


返回结果
```
图中找图：
[{"confidence": [37, 48], "result": [63, 111], "rectangle": [[63, 111], [63, 110], [63, 111], [63, 110]]}]

返回格式为数组格式，里面是根据小图在大图里匹配到的所有的小图

confidence：下标1 = 查找图片匹配成功的特征点，下标2=总的特征点
注意：
下标1 / 下标2不能简单粗暴的理解为相似度，比如[5,7]总特征点7个成功了5个，就不能说明相似
一般总特征点30个以上成功80%，基本可以认为是匹配相似度很高的了
result：查找到的点x、y
rectangle：目标图像周围四个点的坐标



获取图片指纹：
220:87:68:92:63:93:87:68:92:63:93...

为图片指纹的字符串



比对图片指纹：
0.730110306421

对比2个签名的差距，范围在0-1之间 0完全吻合 1不吻合
0.6  = 比较相似
0.7  = 好像相似
0.3  = 差不多
0.2  = 基本一样

```


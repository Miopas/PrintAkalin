# PrintAkalin
在命令行打印一个阿卡林

娱乐用。

用python的图片处理库来打印线稿类型的图片。

线稿可以用这个工具提取：線稿提取器[https://github.com/FlandreDaisuki/Outline-Extractor]

# Need
Python 3

numpy

pillow

# Usage
python3 run.py image_file

# Example
`python3 run.sh big_akalin.png`

![img](https://github.com/Miopas/PrintAkalin/raw/master/example.gif)

# 记录下中途踩到的小坑
1. Image的size元组，第一个元素是width，第二个元素是height；
2. Shell的行和列的宽度不同，需要先把图片的宽拉伸一下，打印出来的效果会比较好；

# TODO
做的非常粗糙。有几个缺陷：

1.只能处理白色背景的线稿；

2.精度不够；

3.大小的缩放不成比例。

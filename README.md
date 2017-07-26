# PrintAkalin
在命令行打印一个阿卡林

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

# TODO
做的非常粗糙。
几个缺陷：
1.只能处理白色背景的线稿；
2.精度不够；
3.大小的缩放不成比例。

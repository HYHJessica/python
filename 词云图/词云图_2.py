

# -*- coding: utf-8 -*-
import jieba
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from matplotlib import colors
import collections


def chinese_jieba():
    # 读取目标文本
    with open(r'文本.txt', encoding='utf-8') as fp:
        txt = fp.read()
        fp.close()
    wordlist_jieba = jieba.lcut(txt)  # 将文本分割，返回列表
    txt_jieba = " ".join(wordlist_jieba)  # 将列表拼接为以空格为间断的字符串
    return txt_jieba


def stopwords_read():
    # 读取停用词，也可自己根据需求写入
    stopwords_ = ['里', '拍']
    with open('chinesestopwords.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if len(line) > 0:
                stopwords_.append(line.strip())
    return stopwords_


def wordcloud_generate():
    stopwords_ = stopwords_read()
    # 读取目标文本
    txt = chinese_jieba()
    background_image = np.array(Image.open('基本椭圆背景.jpg'))#
    colormaps = colors.ListedColormap(['#871A84', '#BC0F6A', '#BC0F60', '#CC5F6A', '#AC1F4A'])  # 蓝色
    wordcloud = WordCloud(font_path='simhei.ttf',  # 字体
                          prefer_horizontal=0.99,
                          background_color='white',  # 背景色
                          max_words=100,  # 显示单词数
                          max_font_size=400,  # 最大字号
                          stopwords=stopwords_,  # 过滤噪声词
                          mask=background_image,  # 背景轮廓
                          colormap=colormaps,  # 使用自定义颜色
                          collocations=False
                          ).generate(txt)
    image = wordcloud.to_image()
    image.show()  # 展示图片
    wordcloud.to_file('词云图2.jpg')  # 保存图片


if __name__ == '__main__':
    wordcloud_generate()

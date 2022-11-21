# coding:utf-8

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def del_symbol(stopwords):
    list = []
    for i in range(len(stopwords)):
        list.append(stopwords[i].replace('\r','').replace('\n',''))
    return list

def generate_wordcloud(text, filepath, stopwordpath):
    '''
    输入文本生成词云,如果是中文文本需要先进行分词处理
    '''
    # 设置显示方式
    d = path.dirname(__file__)
    alice_mask = np.array(Image.open(path.join(d, "Images//alice_mask.png")))
    font_path = path.join(d, "font//msyh.ttf")
    with open(stopwordpath, 'r') as f:
        stopwords = f.readlines() + list(STOPWORDS)
        stopwords = del_symbol(stopwords)
    # stopwords = set(STOPWORDS)
    # stopwords = ['护理','护士','和','了','的','有','等','是','都','也']+list(STOPWORDS)
    wc = WordCloud(background_color="white",  # 设置背景颜色
                   max_words=100,  # 词云显示的最大词数
                   # mask=alice_mask,# 设置背景图片
                   height=400,
                   width=400,
                   stopwords=stopwords,  # 设置停用词
                   font_path=font_path,  # 兼容中文字体，不然中文会显示乱码
                   collocations=False
                   )

    # 生成词云 
    wc.generate(text)

    # 生成的词云图像保存到本地
    wc.to_file(path.join(d, filepath))

    # 显示图像
    plt.imshow(wc, interpolation='bilinear')
    # interpolation='bilinear' 表示插值方法为双线性插值
    plt.axis("off")  # 关掉图像的坐标
    plt.show()

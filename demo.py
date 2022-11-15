# coding:utf-8
# import translate_context
from os import path
import chnSegment
import plotWordcloud
import youdaotranslate

if __name__=='__main__':

    # 读取文件
    d = path.dirname(__file__)
    # text = open(path.join(d, 'doc//十九大报告全文.txt')).read()
    text = open(path.join(d, 'doc//content.txt')).read()
    # text = open(path.join(d,'doc//alice.txt')).read()
    #  text="付求爱很帅并来到付求爱了网易研行大厦很帅 很帅 很帅"

    # 若是中文文本，则先进行分词操作
    chinese_text=chnSegment.word_segment(text)
    # print(chinese_text)
    # 生成词云
    # english_text = open(path.join(d, 'doc//content(译文).txt')).read()
    plotWordcloud.generate_wordcloud(chinese_text,"Images//chinese.png",'doc//stopword_chinese.txt')

    # plotWordcloud.generate_wordcloud(english_text,"Images//english.png",'doc//stopword_english.txt')

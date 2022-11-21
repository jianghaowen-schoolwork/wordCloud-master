# coding:utf-8
# import translate_context
from os import path
import chnSegment
import plotWordcloud
import youdaotranslate

if __name__=='__main__':

    # 读取文件
    d = path.dirname(__file__)
    text = open(path.join(d, 'doc/test.txt')).read()


    # 若是中文文本，则先进行分词操作
    # chinese_text=chnSegment.word_segment(text)
    text = chnSegment.getPseg(text)
    # print(chinese_text)
    # 生成词云
    # english_text = open(path.join(d, 'doc//content(译文).txt')).read()
    plotWordcloud.generate_wordcloud(text, "Images/chinese.png", 'doc//stopword_chinese.txt')

    # plotWordcloud.generate_wordcloud(english_text,"Images//english.png",'doc//stopword_english.txt')

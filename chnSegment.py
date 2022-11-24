# coding:utf-8

from collections import Counter
from os import path
import jieba
import jieba.posseg as pseg

# jieba.load_userdict(path.join(path.dirname(__file__), 'userdict//userdict.txt'))  # 导入用户自定义词典
jieba.load_userdict(path.join(path.dirname(__file__), 'userdict//new_dict.txt'))  # 导入用户自定义词典


def getPseg(text):
    data = []
    jieba.enable_parallel(4)
    # jieba.enable_paddle()
    seg_list = ''
    words = pseg.cut(text, HMM=False, use_paddle=True)

    for word in words:
        word = str(word)
        word_str = word.split('/')
        if word_str[0] != '':
            e = word_str[1]
            if e == 'a' or e == 'an' or e == 'n' or e == 'vn' or e == 'v':
                data.append(word_str[0])
    # 同义词替换
    with open('doc/synonym.txt', 'r') as f:
        new_list = data
        for txt_line in f:
            replace_list = txt_line.split(' ')
            replace_list[len(replace_list) - 1] = replace_list[len(replace_list) - 1].split('\n')[0]
            new_list = [replace_list[0] if i in replace_list else i for i in new_list]

    # 删除停用词
    new_data_list = delStopWord(new_list)

    # 词频统计
    getWordCount(new_data_list)

    for item in new_data_list:
        seg_list += item + ' '
    return seg_list


def getWordCount(data_list):
    dataDict = Counter(data_list)
    with open('doc//词频统计.txt', 'w') as fw:
        res_list = list(dataDict.items())
        res_list.sort(key=lambda x: x[1], reverse=True)
        fin_res_list = []
        for item in res_list:
            fin_res_list.append(item)
        for i in range(len(fin_res_list)):
            word, count = fin_res_list[i]
            fw.write("%s,%d\n" % (word, count))


def delStopWord(data_list):
    new_data_list = data_list.copy()
    del_list = []
    with open('doc/stopword_chinese.txt', 'r') as f:
        for line in f:
            del_list.append(line.split('\n')[0])
    for key in del_list:
        if key in new_data_list:
            for i in range(new_data_list.count(key)):
                new_data_list.remove(key)
    return new_data_list

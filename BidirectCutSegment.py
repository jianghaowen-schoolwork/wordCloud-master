from os import path
import datetime

def forwardCut(text, dict_list):
    word_list = []
    i = 0
    while i < len(text):
        longest_word = text[i]
        for j in range(i + 1, len(text) + 1):
            word = text[i:j]
            if word in dict_list:
                if len(word) > len(longest_word):
                    longest_word = word
        word_list.append(longest_word)
        i += len(longest_word)
    return word_list


def backCutSegment(text, dict_list):
    word_list = []
    i = len(text) - 1
    while i >= 0:
        longest_word = text[i]
        for j in range(0, i):
            word = text[j:i + 1]
            if word in dict_list:
                if len(word) > len(longest_word):
                    longest_word = word
        word_list.append(longest_word)
        i -= len(longest_word)
    word_list.reverse()
    return word_list


def count_single_char(word_list: list):
    return sum(1 for word in word_list if len(word) == 1)


def bidirectional_segment(text, dict_list):
    f = forwardCut(text, dict_list)
    b = backCutSegment(text, dict_list)
    # 词数更少优先
    if len(f) < len(b):
        return f
    elif len(f) > len(b):
        return b
    else:
        # 单词更少优先
        if count_single_char(f) < count_single_char(b):
            return f
        else:
            return b

if __name__ == '__main__':
    print(datetime.datetime.now())
    d = path.dirname(__file__)
    dict_list = []
    word_list = []
    with open('userdict/new_dict.txt', 'r') as f:
        for line in f:
            line = f.readline()
            if line != '':
                dict_list.append(line.split('\n')[0])
    print(dict_list)
    with open('doc/test.txt','r') as fp:
        for text in fp:
            if text != '':
                w_list = bidirectional_segment(text, dict_list)
                print(w_list)
                word_list += w_list
    print(word_list)
    print(datetime.datetime.now())

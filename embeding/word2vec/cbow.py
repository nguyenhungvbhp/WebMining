# -*- coding: utf-8 -*-
from gensim.models import Word2Vec, KeyedVectors, FastText
from sklearn.decomposition import PCA
import numpy as np
import sys
sys.path.append('/Users/manhhung/Documents/workspace/comment_segmentation/preprocessing_data/')
from read_data import read_data
sentences = read_data()
print(sentences[0])
# print(len(sentences))
# model = KeyedVectors.load('../model/word2vec_skipgram.model')
# ss = read_data()
# print(ss)
# path data
pathdata = './datatrain.txt'

def read_data(path):
    traindata = []
    sents = open(pathdata, 'r', encoding='utf-8', errors='ignore').readlines()
    # print(sents)
    for sent in sents:
        traindata.append(sent.split())
    return traindata


if __name__ == '__main__':
    train_data = sentences
    # train_data = read_data(pathdata)
    # print(train_data[0])
    # model = Word2Vec(train_data, size=100, window=10, min_count=2, workers=4, sg=0)
    # model.wv.save("word2vec.model")
    new_model = KeyedVectors.load("word2vec.model")
    print(new_model['ẩm_thực'])
    for word in new_model.most_similar("ăn"):
        print(word[0])

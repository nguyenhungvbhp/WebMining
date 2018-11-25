from remove_puncutation import clean_sentence
from word_segmentation import tokenize_sentences
import pandas as pd

path = '../../data/labeled_data.csv'

data = pd.read_csv(path)
# print(type(data))
# print(len(data['Review']))


# print(tokenize_sentences(clean_sentence(data['Review'][index])))

def read_data():
    sentences = []
    for sentence in data['Review']:
        sentences.append(tokenize_sentences(clean_sentence(sentence)).split())
    return sentences

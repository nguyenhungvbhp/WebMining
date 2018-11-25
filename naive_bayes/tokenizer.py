from pyvi import ViTokenizer
from remove_puncutation import clean_sentence
import pandas as pd


def tokenize_sentences(sentences):
    return remove_stopword(ViTokenizer.tokenize(clean_sentence(sentences)))
    # return ViTokenizer.tokenize(clean_sentence(sentences))

# list stopwords
filename = './dataset/stopwords.csv'
data = pd.read_csv(filename, sep="\t", encoding='utf-8')
list_stopwords = data['stopwords']
list_stopwords = list_stopwords.tolist()

def remove_stopword(sentence):
    pre_text = []
    words = sentence.split()
    for word in words:
        if word not in list_stopwords:
            pre_text.append(word)
    sentence = ' '.join(pre_text)
    return sentence



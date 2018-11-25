#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import re

# TODO: xóa các kí tự đặc biệt(@#$%)
def remove_puncutation(sentence):
    sentence = sentence.replace('_', ' ')
    sentence = sentence.replace('\\r', ' ')
    sentence = sentence.replace('\\n', ' ')
    sentence = sentence.replace('\\t', ' ')
    sentence = ' '.join(sentence.split())
    # re.sub( '\s+', ' ', sentence ).strip()
    no_punct = ""
    for char in sentence:
        if char not in string.punctuation:
            no_punct = no_punct + char
    sentence = no_punct

    return sentence

# TODO: Xóa số
def remove_digit(sentence):
    return ''.join([i for i in sentence if not i.isdigit()])


def clean_sentence(sentence):
    sentence = remove_digit(remove_puncutation(sentence)).lower()
    sentence = replace_char(sentence)
    sentence = convert_write_off(sentence)

    return sentence


# print(clean_sentence("Tôi thích @##"))

# TODO: thay thế các kí tự lặp ở cuối word(quaaaaa->qua)
def replace_char(sentences):
    sentences = re.sub(r'([q]+)', 'q', sentences)
    sentences = re.sub(r'([w]+)', 'w', sentences)
    sentences = re.sub(r'([e]+)', 'e', sentences)
    sentences = re.sub(r'([r]+)', 'r', sentences)
    sentences = re.sub(r'([t]+)', 't', sentences)
    sentences = re.sub(r'([y]+)', 'y', sentences)
    sentences = re.sub(r'([u]+)', 'u', sentences)
    sentences = re.sub(r'([i]+)', 'i', sentences)
    sentences = re.sub(r'([o]+)', 'o', sentences)
    sentences = re.sub(r'([p]+)', 'p', sentences)
    sentences = re.sub(r'([a]+)', 'a', sentences)
    sentences = re.sub(r'([s]+)', 's', sentences)
    sentences = re.sub(r'([d]+)', 'd', sentences)
    sentences = re.sub(r'([f]+)', 'f', sentences)
    sentences = re.sub(r'([g]+)', 'g', sentences)
    sentences = re.sub(r'([h]+)', 'h', sentences)
    sentences = re.sub(r'([j]+)', 'j', sentences)
    sentences = re.sub(r'([k]+)', 'k', sentences)
    sentences = re.sub(r'([l]+)', 'l', sentences)
    sentences = re.sub(r'([z]+)', 'z', sentences)
    sentences = re.sub(r'([x]+)', 'x', sentences)
    sentences = re.sub(r'([c]+)', 'c', sentences)
    sentences = re.sub(r'([v]+)', 'v', sentences)
    sentences = re.sub(r'([b]+)', 'b', sentences)
    sentences = re.sub(r'([n]+)', 'n', sentences)
    sentences = re.sub(r'([m]+)', 'm', sentences)

    return sentences


# TODO: chuyển các kí tự viết tắt về đầy đủ.
def convert_write_off(sentence):
    sentence = re.sub(r'(\sk\s)', ' không ', sentence)
    sentence = re.sub(r'(\sko\s)', ' không ', sentence)
    sentence = re.sub(r'(\sr\s)', ' rồi ', sentence)
    sentence = re.sub(r'(\sdc\s)', ' được ', sentence)
    sentence = re.sub(r'(\sđc\s)', ' được ', sentence)
    sentence = re.sub(r'(\snchung\s)', ' nói chung ', sentence)
    sentence = re.sub(r'(\snchung\s)', ' nói chung ', sentence)
    sentence = re.sub(r'(\snc\s)', ' nước ', sentence)
    sentence = re.sub(r'(\scx\s)', ' cũng ', sentence)
    sentence = re.sub(r'(\svs\s)', ' với ', sentence)
    sentence = re.sub(r'(\sm\s)', ' mình ', sentence)
    sentence = re.sub(r'(\strc\s)', ' trước ', sentence)
    sentence = re.sub(r'(\sh\s)', ' giờ ', sentence)
    sentence = re.sub(r'(\sqa\s)', ' qua ', sentence)
    sentence = re.sub(r'(\sbt\s)', ' bình thường ', sentence)
    sentence = re.sub(r'(\st\s)', ' tôi ', sentence)
    sentence = re.sub(r'(\sbh\s)', ' bao giờ ', sentence)
    sentence = re.sub(r'(\smn\s)', ' mọi người ', sentence)
    sentence = re.sub(r'(\sng\s)', ' người ', sentence)
    sentence = re.sub(r'(\snhg\s)', ' nhưng ', sentence)
    sentence = re.sub(r'(\snv\s)', ' nhân viên ', sentence)
    sentence = re.sub(r'(\sgt\s)', ' giới thiệu ', sentence)
    sentence = re.sub(r'(\sj\s)', ' gì ', sentence)
    sentence = re.sub(r'(\slq\s)', ' liên quan ', sentence)
    sentence = re.sub(r'(\slquan\s)', ' liên quan ', sentence)
    sentence = re.sub(r'(\sace\s)', ' anh chị em ', sentence)
    sentence = re.sub(r'(\sce\s)', ' chị em ', sentence)
    sentence = re.sub(r'(\stp\s)', ' thành phố ', sentence)
    sentence = re.sub(r'(\skm\s)', ' khuyến mại ', sentence)
    sentence = re.sub(r'(\ssz\s)', ' size ', sentence)

    return sentence

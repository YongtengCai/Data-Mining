#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date   : 
# @Author : 
# @Usage  : 

from textblob import TextBlob, Word
import nltk
import pandas as pd
import string

# tokenize
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# filter stopwords
stop_words = set(nltk.corpus.stopwords.words('english'))

def preprocess(text):
    # 词条化，按句子切分
	sents = tokenizer.tokenize(text.lower())
	words = []
    # 规范化，根据词性转换
	for sent in sents:
		words += lemmatize_with_postag(sent)
	words_s = []
	for w in words:
		# 移除标点
		w_s = w.translate(w.maketrans("", "", string.punctuation))
        # 去除停用词、数字串等噪音
		if check(w_s):
			words_s.append(w_s)
	return words_s

word_map = {}
def lemmatize_with_postag(sentence):
	sent = TextBlob(sentence)
	tag_dict = {'J': 'a', 'N': 'n', 'V': 'v', 'R': 'r'}
	lemmatized_list = []
	for w, pos in sent.tags:
		tag = tag_dict.get(pos[0], 'n')
		key = w + '+' + tag
		if key in word_map:
			lemmatized_list.append(word_map[key])
		else:
			w_tmp = w.lemmatize(tag)
			word_map[key] = w_tmp
			lemmatized_list.append(w_tmp)
	return lemmatized_list

word_check = {}
def check(word):
	if word in word_check:
		return word_check[word]
	if len(word) < 3:
		word_check[word] = False
		return False
	elif word.isdigit():
		word_check[word] = False
		return False
	elif word in stop_words:
		word_check[word] = False
		return False
	elif not word[0].isalpha():
		word_check[word] = False
		return False
	else:
		word_check[word] = True
		return True

if __name__ == '__main__':
	path = './'
	file_in = open(path + 'review_res_10%.txt')
	file_out = open(path + 'data_preprocessed_10%.csv', 'w')
	file_out.write(('review,sentiment\n') % ())
	file_in.readline()
	while 1:
		line = file_in.readline()
		if not line:
			break
		else:
			review_id, user_id, business_id, stars, date, useful, funny, cool, text = line.strip().split('\t')
			stars = float(stars)
			if stars >= 4:
				sentiment = 1
			else:
				sentiment = 0
			review_preprocessed = preprocess(text)
			if len(review_preprocessed) > 0:
				file_out.write(('%s,%d\n') % (' '.join(review_preprocessed), sentiment))
	file_in.close()
	file_out.close()

'''
CC coordinating conjunction
CD cardinal digit
DT determiner
EX existential there (like: “there is” … think of it like “there exists”)
FW foreign word
IN preposition/subordinating conjunction
JJ adjective ‘big’
JJR adjective, comparative ‘bigger’
JJS adjective, superlative ‘biggest’
LS list marker 1)
MD modal could, will
NN noun, singular ‘desk’
NNS noun plural ‘desks’
NNP proper noun, singular ‘Harrison’
NNPS proper noun, plural ‘Americans’
PDT predeterminer ‘all the kids’
POS possessive ending parent‘s
PRP personal pronoun I, he, she
PRP$ possessive pronoun my, his, hers
RB adverb very, silently,
RBR adverb, comparative better
RBS adverb, superlative best
RP particle give up
TO to go ‘to‘ the store.
UH interjection errrrrrrrm
VB verb, base form take
VBD verb, past tense took
VBG verb, gerund/present participle taking
VBN verb, past participle taken
VBP verb, sing. present, non-3d take
VBZ verb, 3rd person sing. present takes
WDT wh-determiner which
WP wh-pronoun who, what
WP$ possessive wh-pronoun whose
WRB wh-abverb where, when
'''

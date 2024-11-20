### 文本词条化
### 中文
text = '同一字符串可能有多种分词方式'
import jieba
seg_list = jieba.cut(text)
print(", ".join(seg_list))
# 同一, 字符串, 可能, 有, 多种, 分词, 方式
from snownlp import SnowNLP
s = SnowNLP(text)
print(', '.join(s.words))
# 同一, 字符, 串, 可能, 有, 多种, 分词, 方式

### 文本规范化
### 中文
#### 音似错字
from pycorrector import Corrector
m = Corrector()
text = '中文咎错工具'
print(m.correct(text))
# {'source': '中文咎错工具', 'target': '中文纠错工具', 'errors': [('咎错', '纠错', 2)]}

#### 形似错字
from pycorrector import Corrector
m = Corrector()
text = '中文纠措工具'
print(m.correct(text))
# {'source': '中文纠措工具', 'target': '中文纠错工具', 'errors': [('纠措', '纠错', 2)]}

#### 繁简体转换
import pycorrector
text_traditional = '繁簡體轉換'
text_simplified = pycorrector.traditional2simplified(text_traditional)
print(text_traditional, '=>', text_simplified)
# 繁簡體轉換 => 繁简体转换
text_simplified = '繁简体转换'
text_traditional = pycorrector.simplified2traditional(text_simplified)
print(text_simplified, '=>', text_traditional)
# 繁简体转换 => 繁簡體轉換

### 英文
### 拼写修正
from textblob import TextBlob
text = 'Buziness inteligance is a trendding topic.'
blob = TextBlob(text)
print(blob.correct())
# Business intelligence is a treading topic.

### 大小写
from textblob import TextBlob
text = 'Useful information is mined from text data.'
blob = TextBlob(text)
print(blob.lower())
# useful information is mined from text data.
print(blob.upper())
# USEFUL INFORMATION IS MINED FROM TEXT DATA.

### 字形还原 
from textblob import Word
word = 'ground'
w = Word(word)
print(w.lemmatize('n'))
# ground
print(w.lemmatize('v'))
# grind

from textblob import TextBlob
tag_dict = {'J': 'a', 'N': 'n', 'V': 'v', 'R': 'r'}
text = 'Useful information is mined from text data.'
blob = TextBlob(text.lower())
text_lemmatized = []
for w, tag in blob.tags:
	text_lemmatized.append(w.lemmatize(tag_dict.get(tag[0], 'n')))
print(' '.join(text_lemmatized))
# useful information be mine from text data

### 词根提取
import nltk
from nltk.stem import PorterStemmer
from textblob import TextBlob
ps = PorterStemmer()
text = 'Useful information is mined from text data.'
blob = TextBlob(text.lower())
text_stemmed = []
for w, tag in blob.tags:
	text_stemmed.append(ps.stem(w))
print(' '.join(text_stemmed))
# use inform is mine from text data


### 去除html标签
#### 正则表达式
import re
text = """<div>
<h1>标题</h1>
<p>内容1</p>
<a href="">内容2</a>
</div>"""
pattern = re.compile(r'<[^>]+>')
text_res = pattern.sub('', text)
print(text_res)
# 
# 标题
# 内容1
# 内容2
# 
#### BeautifulSoup
from bs4 import BeautifulSoup
text = """<div>
<h1>标题</h1>
<p>内容1</p>
<a href="">内容2</a>
</div>"""
soup = BeautifulSoup(text, 'html.parser')
print(soup.get_text())
# 
# 标题
# 内容1
# 内容2
# 

### 特殊字符
#### 中文
import re
text = '噪音去除，是识别***并清除@@文本中的各种干扰信息的过程。'
text_res = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]", "", text)
print(text_res)
# 噪音去除是识别并清除文本中的各种干扰信息的过程
#### 英文
text = "No;ise * Rem:ova;l!"
test_res = ''.join(letter for letter in text if letter.isalnum())
print(test_res)
# NoiseRemoval

### 非正式用语

### 停用词
#### 中文
#### 英文
from nltk.corpus import stopwords
words = stopwords.words('english')
print(words)
# ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
print(len(words))
# 179

from nltk.corpus import stopwords
print(stopwords.fileids())
# ['arabic', 'azerbaijani', 'basque', 'bengali', 'catalan', 'chinese', 'danish', 'dutch', 'english', 'finnish', 'french', 'german', 'greek', 'hebrew', 'hinglish', 'hungarian', 'indonesian', 'italian', 'kazakh', 'nepali', 'norwegian', 'portuguese', 'romanian', 'russian', 'slovene', 'spanish', 'swedish', 'tajik', 'turkish']
print(len(stopwords.fileids()))
# 29
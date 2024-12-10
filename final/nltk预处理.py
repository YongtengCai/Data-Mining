#nltk预处理
#载入IMDb数据
import pandas as pd
data = pd.read_csv('E:/本科/数据挖掘与商务分析/hw/final/IMDB Dataset.csv')
print(data.shape)

#将sentiment列中的positive和negative替换为1和0
data['sentiment'] = data['sentiment'].map({'positive': 1, 'negative': 0})
data.head()

#将评论分为token
import nltk
from collections import Counter, OrderedDict

#nltk.download('punkt')
#nltk.download('punkt_tab')

X = data['review']
y = data['sentiment']

from nltk.tokenize import word_tokenize
X = X.apply(word_tokenize)

print(X.head())

tokencounts = Counter()
for line in X:
    tokencounts.update(line)

print('vocab size:', len(tokencounts))

#将X与y保存为csv
processed_data = pd.DataFrame({'review': X, 'sentiment': y})
processed_data.to_csv('E:/本科/数据挖掘与商务分析/hw/final/IMDB Dataset_nltk.csv', index=False)


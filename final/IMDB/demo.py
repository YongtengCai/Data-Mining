import torch
import torch.nn as nn
from torchtext.vocab import vocab
from collections import Counter, OrderedDict

# 假设 train_dataset 是一个包含 'review' 和 'sentiment' 的字典
train_dataset = {
    'review': ["This movie was great!", "I did not like this movie."],
    'sentiment': ["positive", "negative"]
}

# 定义 tokenizer 和 token_counts
tokenizer = lambda x: x.split()
token_counts = Counter()

# 统计单词频率
for review in train_dataset['review']:
    tokens = tokenizer(review)
    token_counts.update(tokens)

print('Vocab-size:', len(token_counts))

# 利用 torchtext 的 vocab 将 token 转换为整数
sorted_by_freq_tuples = sorted(token_counts.items(), key=lambda x: x[1], reverse=True)
ordered_dict = OrderedDict(sorted_by_freq_tuples)

vocab = vocab(ordered_dict)
vocab.insert_token("<pad>", 0)
vocab.insert_token("<unk>", 1)
vocab.set_default_index(1)

print([vocab[token] for token in ['this', 'is', 'an', 'example']])

# 定义转换函数
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
review_pipeline = lambda x: [vocab[token] for token in tokenizer(x)]
sentiment_pipeline = lambda x: 1 if x == 'positive' else 0

def collate_batch(batch):
    sentiment_list, review_list, lengths = [], [], []
    for _sentiment, _review in batch:
        sentiment_list.append(sentiment_pipeline(_sentiment))
        processed_text = torch.tensor(review_pipeline(_review), dtype=torch.int64)
        review_list.append(processed_text)
        lengths.append(processed_text.size(0))
    sentiment_list = torch.tensor(sentiment_list)
    lengths = torch.tensor(lengths)
    padded_review_list = nn.utils.rnn.pad_sequence(review_list, batch_first=True)
    return padded_review_list.to(device), sentiment_list.to(device), lengths.to(device)

# 假设 train_dataset 是一个包含 (sentiment, review) 元组的列表
train_dataset = [("positive", "This movie was great!"), ("negative", "I did not like this movie.")]

from torch.utils.data import DataLoader
dataloader = DataLoader(train_dataset, batch_size=4, shuffle=False, collate_fn=collate_batch)
review_batch, sentiment_batch, length_batch = next(iter(dataloader))
print(review_batch)
print(sentiment_batch)
print(length_batch)
print(review_batch.shape)
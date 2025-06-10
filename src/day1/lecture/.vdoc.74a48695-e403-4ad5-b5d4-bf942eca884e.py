# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| eval: false
import gensim.downloader as api

# Load pre-trained Word2Vec embeddings
word_vectors = api.load("word2vec-google-news-300")

# Find words most similar to 'stock'
similar_words = word_vectors.most_similar("stock")
print(similar_words)

# Example output:
# [('stocks', 0.8756),
#  ('shares', 0.7878),
#  ('equity', 0.7231),
#  ('market', 0.6897),
#  ('NYSE', 0.6793),
#  ('exchange', 0.6346),
#  ('commodity', 0.6217),
#  ('investor', 0.6134),
#  ('trading', 0.6040),
#  ('markets', 0.5923)]

# Financial examples
finance_terms = word_vectors.most_similar(positive=['bank', 'loan'], negative=['deposit'])
print(finance_terms)
```
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

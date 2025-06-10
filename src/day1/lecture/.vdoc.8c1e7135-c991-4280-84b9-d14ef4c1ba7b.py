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

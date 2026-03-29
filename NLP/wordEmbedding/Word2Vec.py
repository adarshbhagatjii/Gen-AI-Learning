# Step 1: Install gensim
# Normally, you would run this in the terminal or add to requirements.txt:
# !pip install gensim

# Step 2: Import Word2Vec class from gensim.models
from gensim.models import Word2Vec

# Step 3: Define the training data
# 'sentences' is a list of sentences, where each sentence is a list of words.
# This is the format required by Word2Vec for training.
sentences = [
    ["king", "rules", "kingdom"],
    ["queen", "rules", "kingdom"],
    ["man", "is", "strong"],
    ["woman", "is", "strong"]
]

# Step 4: Create and train the Word2Vec model
# Parameters:
# - sentences: The training data
# - vector_size: Number of dimensions for each word vector (embedding size)
# - window: Maximum distance between current and predicted word in a sentence
# - min_count: Ignores words with total frequency lower than this
# - sg: 0 = CBOW (Continuous Bag of Words), 1 = Skip-gram
# CBOW predicts a word based on its context (other words around it)
model = Word2Vec(sentences, vector_size=50, window=2, min_count=1, sg=0)  # CBOW

# Step 5: Find words most similar to 'king' based on the trained vectors
# The model has learned word embeddings, now we can find similar words
print(model.wv.most_similar("king"))
# Output: List of tuples [(word, similarity_score), ...]
# Example: [('queen', 0.89), ('kingdom', 0.82), ...]

# ---------------------------------------
# Step 6: Load a pre-trained Word2Vec model
import gensim.downloader as api

# Load Google's pre-trained Word2Vec model trained on Google News dataset
# Size: ~1.6 GB, contains 3 million word vectors, 300 dimensions each
model = api.load("word2vec-google-news-300")

# Step 7: Find most similar words to 'king' using pre-trained embeddings
print("Most similar to 'king':")
print(model.most_similar("king", topn=5))
# Output: Top 5 words most similar to 'king' based on Google News embeddings

# Step 8: Perform analogy example: king - man + woman
# This finds a word vector that is closest to (king - man + woman)
# This is how Word2Vec captures semantic relationships
print("\nking - man + woman:")
print(model.most_similar(positive=["king", "woman"], negative=["man"], topn=5))
# Output: Usually returns 'queen' as the closest vector, then other related words

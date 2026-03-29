from sklearn.feature_extraction.text import TfidfVectorizer

# Sample corpus
corpus = [
    "i love Nlp",
    "NLP loves python",
    "python is great"
]

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform
tfidf_matrix = vectorizer.fit_transform(corpus)
print(tfidf_matrix)

# Show as DataFrame
import pandas as pd
df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
print(df)


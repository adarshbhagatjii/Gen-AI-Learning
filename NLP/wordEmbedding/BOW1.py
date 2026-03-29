from sklearn.feature_extraction.text import CountVectorizer

# Sample data
sentences = [
    "i love pizza and i love pasta",
    "The bread was fresh and soft",
    "i love pizza and i love pasta"
    #"Fresh cake and bread every day"
]

# Create BoW
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)
print(X)

# Convert to array
print(vectorizer.get_feature_names_out())
print(X.toarray())

##Term - Frequency 

# import pandas as pd
# import numpy as np

# # Convert to DataFrame
# df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# # Term frequency
# df_tf = df.div(df.sum(axis=1), axis=0)
# print(df_tf)
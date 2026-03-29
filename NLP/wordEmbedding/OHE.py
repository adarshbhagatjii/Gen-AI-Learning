import sklearn
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
text=['the food is good and good',
      'the food is bad',
      'i love pizza because that pizza is is is ammazing']

vectorizer=CountVectorizer(binary=True)

x=vectorizer.fit_transform(text)

print(x)

print(vectorizer.get_feature_names_out())

print(x.toarray())

# Nt=["the food is tasty"]
# k=vectorizer.transform(Nt)
# print(vectorizer.get_feature_names_out())
# print(k.toarray())

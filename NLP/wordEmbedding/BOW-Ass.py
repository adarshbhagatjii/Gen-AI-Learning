from sklearn.feature_extraction.text import CountVectorizer

reviews = []
for i in range(5):
    reviews.append(input("Enter review : "))

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)
print("Vocabulary:", vectorizer.get_feature_names_out())
print(len(vectorizer.get_feature_names_out()))
print("BoW Matrix:\n", X.toarray())


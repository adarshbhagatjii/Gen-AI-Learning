##COmaprision
# import sklearn
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
nltk.download('stopwords')

text= ["i love this AI sub,"
"i want to take this course"]

vectorizer=CountVectorizer()

x=vectorizer.fit_transform(text)

voac=vectorizer.get_feature_names_out()

print("VOACwith_stopwords:",voac)

print("matrixWithstopword:",x.toarray())

##for removing stopwords


filtervoac=[i for i in voac if  i  not in stopwords.words("english")]
y=vectorizer.fit_transform(text)

print("VOACwithOUt_stopwords:",filtervoac)
print("matrixWithOutstopword:",y.toarray())




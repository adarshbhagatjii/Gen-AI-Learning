# a=input("Enter the string")
# b=a.split()
# print(list(a.split()))

# import nltk
# # nltk.download('punkit')
# # nltk.download("punkt_tab")
# from nltk.tokenize import word_tokenize
# text = "hello! i am adarsh bhagat😉"
# print(word_tokenize(text))

# import spacy 
# nlp=spacy.load("en_core_web_sm")
# doc=nlp('Hello! i am adarsh bhagat 😉')
# print(doc)
# print(type(doc))

# token=[i.text for i in doc]
# print(token)


# import string 
# text = input("enter the string : ")
# cleaned=''.join ([chr for chr in text if chr not in string.punctuation and not chr.isdigit() ])
# print(cleaned)


# import re 
# text ='hello i have 2 pets!!!'
# cleaned= re.sub(r'[^a-zA-Z\s]','', text)
# print(cleaned)


import nltk 
from nltk.corpus import stopwords 
nltk.download ('stopwords')

words=['this','is','a', 'test','adarsh']
filtered= [word for word in words if word not in stopwords.words('english')]
print(filtered)

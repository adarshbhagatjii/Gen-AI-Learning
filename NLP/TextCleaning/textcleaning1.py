#Lowercasing

# text = "Natural Language Processing"
# print(text.lower())# "natural language processing"



# Removing Punctuation & Numbers

#1.USING String Module

# import string

# text=input("enter a text:")

# cleaned=''.join([char for char in text if char not in string.punctuation and not char.isdigit()])
# print(cleaned) ##joins will give me output in one string if we dont use join then we get o/p in list 
#i have 2 pets!!! ---->['i', ' ', 'h', 'a', 'v', 'e', ' ', ' ', 'p', 'e', 't', 's']

#2.Alternative using regex:

# import re
# text=input("enter a text:")
# cleaned =re.sub(r'[^a-zA-Z\s]','',text)##re.sub(pattern, replacement, text)
# print(cleaned)


# Removing Stopwords

#1.using corpus module.

# import nltk
# from nltk.corpus import stopwords
# nltk.download('stopwords')
# words=["this", "is", "a", "test"]
# filtered=[word for word in words if word not in stopwords.words("english")]
# print(filtered)

# 2.Regex-based Text Cleaning

import re
text = "Hello @user!!! Visit https://test.com 😊 "

cleaned = re.sub(r"http\S+|www\S+|@\S+|[^a-zA-Z\s]",'',  text) ##re.sub(pattern, replacement, text) #compulsary to pass 3 arguments
print(cleaned) # "Hello  Visit  "   
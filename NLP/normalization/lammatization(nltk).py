# # Using NLTK’s WordNetLemmatizer:
# # from nltk.stem import WordNetLemmatizer
# # from nltk.corpus import wordnet
# # import nltk
# # nltk.download('wordnet')
# # nltk.download('omw-1.4')

# # lemmatizer = WordNetLemmatizer()

# # print(lemmatizer.lemmatize("running", pos="v"))  # run
# # print(lemmatizer.lemmatize("eaten", pos="v"))   # eat

# ###more eg
# import nltk
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import wordnet

# # Download WordNet + OMW 1.4
# nltk.download('wordnet')

# lemmatizer = WordNetLemmatizer()
# words=["eating","eats","eaten","going","gone","goes","fairly","sportingly","running"]

# print(lemmatizer.lemmatize("running", pos="v"))   # run
# print(lemmatizer.lemmatize("better", pos="a"))    # good
# print(lemmatizer.lemmatize("eating", pos="a")) 
# print(lemmatizer.lemmatize("eats", pos="a")) 
# print(lemmatizer.lemmatize("going", pos="a")) 
# print(lemmatizer.lemmatize("gone", pos="a")) 
# print(lemmatizer.lemmatize("goes", pos="a")) 
# print(lemmatizer.lemmatize("fairly", pos="a")) 
# print(lemmatizer.lemmatize("sportingly", pos="a")) 

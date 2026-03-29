# from nltk.stem import PorterStemmer 
# words=["eating","eats","eaten","going","gone","goes","fairly","sportingly","running"]
# porter=PorterStemmer()
# for word in words:
#     print(f"{word}---> {porter.stem(word)}")

# print("*"*20)

# from nltk.stem import LancasterStemmer
# words=["eating","eats","eaten","going","gone","goes","fairly","sportingly","running"]
# lancaster=LancasterStemmer()
# for word in words:
#     print(f"{word}---> {lancaster.stem(word)}")

# print("*"*20)

# # ##Snowball stemmer
# from nltk.stem import SnowballStemmer
# words=["eating","eats","eaten","going","gone","goes","fairly","sportingly","running"]
# snowball=SnowballStemmer("english")
# for word in words:
#     print(f"{word}---> {snowball.stem(word)}")
# print("*"*20)

# from nltk.stem import RegexpStemmer
# regex=RegexpStemmer(r'ing$|s$|e$')
# words=["eating","eats","eaten","going","gone","goes","fairly","sportingly","running"]
# for word in words:
#     print(f"{word}---> {regex.stem(word)}")
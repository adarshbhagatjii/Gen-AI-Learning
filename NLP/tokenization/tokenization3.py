import spacy 
nlp=spacy.load("en_core_web_sm") #lg --larger,,md--medium### manually download --->> python -m spacy download "en_core_web_sm"
doc=nlp('hello! this is keerthi😊')#'i dont😊 know what to do'
print(doc)
token=[token.text for token in doc]
##List of token
print(token)
                                                                                     
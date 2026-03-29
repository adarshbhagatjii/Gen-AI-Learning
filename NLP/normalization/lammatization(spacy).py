
# import spacy
# nlp = spacy.load("en_core_web_sm")
# doc = nlp("The children are running to the playground.")
# print([token.lemma_ for token in doc])
import spacy
nlp = spacy.load("en_core_web_sm")
words=["eating","eats","eaten","going","gone","goes","fairly","sportingly","running"]
data=' '.join([i for i in words])
doc = nlp(data)
print([token.lemma_ for token in doc])


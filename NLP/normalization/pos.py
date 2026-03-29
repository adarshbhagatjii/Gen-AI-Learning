import nltk
# Download punkt (tokenizer) + POS tagger (English)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = " brave soldier fights bravely"
tokens = word_tokenize(text)

# POS tagging
pos_tags_nltk = pos_tag(tokens)
print(pos_tags_nltk)

# # Map Penn Treebank tags to simpler WordNet POS tags
def simplify(tag):
    if tag.startswith('J'):
        return 'ADJ'   # adjective
    elif tag.startswith('V'):
        return 'V'     # verb
    elif tag.startswith('N'):
        return 'N'     # noun
    elif tag.startswith('R'):
        return 'ADV'   # adverb
    else:
        return tag     # keep as is

simple_tags = [(word, simplify(tag)) for word, tag in pos_tags_nltk]
print(simple_tags)


# ##USING SPACY
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("brave soldier fights bravely")

spacy_pos_tags=[(tokens.text,tokens.pos_) for tokens in doc]
print(spacy_pos_tags)
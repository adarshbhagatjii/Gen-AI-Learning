
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('stopwords')

# Sample sentence
sentence = "Taj Mahal is a beautiful monument"

# Tokenize the sentence into words
words = word_tokenize(sentence)
# Remove stopwords (optional)
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Perform POS tagging
pos_tags = nltk.pos_tag(filtered_words)

# Print the output
print("POS Tags:", pos_tags)


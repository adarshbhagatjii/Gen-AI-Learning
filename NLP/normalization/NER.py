import spacy

# Load small English model
nlp = spacy.load("en_core_web_sm")

# Example text
text = "Barack Obama was born in Hawaii. He was the 44th President of the United States."

# Process text
doc = nlp(text)
print(doc)

# Extract named entities
for ent in doc.ents:
    print(ent)
    print(ent.text, " → ", ent.label_)
    print(doc.ents)
# Example output list of entity labels

result = [ent.label_ for ent in doc.ents]
print(result)
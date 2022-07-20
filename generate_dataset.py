import pandas as pd
import csv
import spacy
from spacy.tokens import DocBin

#listing_titles = pd.read_csv('./testset/Listing_Titles.tsv', sep='\t', on_bad_lines='skip', quoting=csv.QUOTE_NONE, encoding='utf8')


tagged_titles = pd.read_csv('./dataset/Train_Tagged_Titles.tsv', sep='\t', on_bad_lines='skip', quoting=csv.QUOTE_NONE, encoding='utf8')

tags = ['Accents', 'Brand', 'Character', 'Character Family', 'Closure', 'Color', 'Country/Region of Manufacture', 'Department', 'Fabric Type', 'Features', 'Handle Drop', 'Handle Style', 'Handle/Strap Material', 'Hardware Material', 'Lining Material', 'MPN', 'Material', 'Measurement, Dimension', 'Model', 'Occasion', 'Pattern', 'Pocket Type', 'Product Line', 'Season', 'Size', 'Strap Drop', 'Style', 'Theme', 'Trim Material', 'Type']

tokens = tagged_titles.groupby('Record Number')['Token'].apply(list).to_dict()
tags = tagged_titles.groupby('Record Number')['Tag'].apply(list).to_dict()

# print(tiddies[1])
# print("<3<3 wuwuwuwuuw I LOVE AMOURANTH DSLKFJSLDKFJSDLK:FJ")
# Loois vittidie amouranth vintage  fartfabric(tm) screw-on 
# Brand          Product Line Style Fabric Type    Closure
# print(ass[1])

tokenized_data = [[(tokens[i][tag], tags[i][tag]) for tag in range(0, len(tags[i]))] for i in range(1, len(tags) + 1)]

for i in range(0, len(tokenized_data)):
    for j in reversed(range(1, len(tokenized_data[i]))):
        if tokenized_data[i][j][1] != tokenized_data[i][j][1]: #python nan moment
            tokenized_data[i][j - 1] = (tokenized_data[i][j - 1][0] + " " + tokenized_data[i][j][0], tokenized_data[i][j - 1][1])

nanless_tokens = [[i for i in item if not i[1] != i[1]] for item in tokenized_data]

tokens = [' '.join([i[0] for i in item]) for item in nanless_tokens]
tags = [[i[1] for i in item] for item in nanless_tokens]

for i in range(0, len(tags)):
    curr = 0
    for j in range(0, len(tags[i])):
        tags[i][j] = (curr, curr + len(nanless_tokens[i][j][0]), tags[i][j])
        curr += len(nanless_tokens[i][j][0]) + 1

clean_tokens = [(tokens[i], tags[i]) for i in range(0, len(tokens))]

nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")
for tag in tags:
    ner.add_label(tag)
    
dev = clean_tokens[::10]
train = clean_tokens
del train[::10]

db = DocBin()
for text, annotations in train:
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annotations:
        span = doc.char_span(start, end, label=label)
        if(span is None):
            print("skipping entity")
        else:
            ents.append(span)
    doc.ents = ents
    db.add(doc)

db.to_disk("./train.spacy")
print("wrote " + str(len(train)) + " lines to ./train.spacy")

db = DocBin()
for text, annotations in dev:
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in annotations:
        span = doc.char_span(start, end, label=label)
        if(span is None):
            print("skipping entity")
        else:
            ents.append(span)
    doc.ents = ents
    db.add(doc)

db.to_disk("./dev.spacy")
print("wrote " + str(len(dev)) + " lines to ./dev.spacy")
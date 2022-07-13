from cmath import nan
import pandas as pd
import csv
import json
import string
import spacy
from spacy.tokens import DocBin

#listing_titles = pd.read_csv('./testset/Listing_Titles.tsv', sep='\t', on_bad_lines='skip', quoting=csv.QUOTE_NONE, encoding='utf8')

tagged_titles = pd.read_csv('./dataset/Train_Tagged_Titles.tsv', sep='\t', on_bad_lines='skip', quoting=csv.QUOTE_NONE, encoding='utf8')

tags = ['Accents', 'Brand', 'Character', 'Character Family', 'Closure', 'Color', 'Country/Region of Manufacture', 'Department', 'Fabric Type', 'Features', 'Handle Drop', 'Handle Style', 'Handle/Strap Material', 'Hardware Material', 'Lining Material', 'MPN', 'Material', 'Measurement, Dimension', 'Model', 'Occasion', 'Pattern', 'Pocket Type', 'Product Line', 'Season', 'Size', 'Strap Drop', 'Style', 'Theme', 'Trim Material', 'Type']

tiddies = tagged_titles.groupby('Record Number')['Token'].apply(list).to_dict()
ass = tagged_titles.groupby('Record Number')['Tag'].apply(list).to_dict()

# print(tiddies[1])
# print("<3<3 wuwuwuwuuw I LOVE AMOURANTH DSLKFJSLDKFJSDLK:FJ")
# print(ass[1])

kimk = [[(tiddies[i][tiddie], ass[i][tiddie]) for tiddie in range(0, len(ass[i]))] for i in range(1, len(ass) + 1)]

for i in range(0, len(kimk)):
    for j in reversed(range(1, len(kimk[i]))):
        if(kimk[i][j][1] != kimk[i][j][1]): #python nan moment
            kimk[i][j - 1] = (kimk[i][j - 1][0] + " " + kimk[i][j][0], kimk[i][j - 1][1])

delphine = [[i for i in item if not i[1] != i[1]] for item in kimk]

tiddies = [' '.join([i[0] for i in item]) for item in delphine]
ass = [[i[1] for i in item] for item in delphine]

for i in range(0, len(ass)):
    curr = 0
    for j in range(0, len(ass[i])):
        ass[i][j] = (curr, curr + len(delphine[i][j][0]), ass[i][j])
        curr += len(delphine[i][j][0]) + 1

amouranth = [(tiddies[i], ass[i]) for i in range(0, len(tiddies))]

nlp = spacy.blank("en")

# the DocBin will store the example documents
db = DocBin()
for text, annotations in amouranth:
    doc = nlp(text)
    ents = []
    for start, end, label in annotations:
        span = doc.char_span(start, end, label=label)
        ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("./amouranth.spacy")

# [(text , {"entities" : entities })]
# [[(LOUIS, Brand), (VITTON, Brand)],[(LOUIS, Brand), (VITTON, Brand)...

#print(tiddies) #SHOW ME THE TIDDIES
# print("amouranth")
# print(amouranth) #she's beeautiful



# ['LOUIS', 'VUITTON', 'M40096', 'Handbag', 'Priscilla', 'Multi-color', 'canvas', 'Multi-color', 'canvas']
# <3<3 wuwuwuwuuw I LOVE AMOURANTH DSLKFJSLDKFJSDLK:FJ
# ['Brand', nan, 'MPN', 'Type', 'Model', 'Color', 'Fabric Type', 'Color', 'Fabric Type']
# tiddies

#tokensntags = [(tokens[str(i)], tags[str(i)]) for i in range(0, len(tokens))]


quit()


clean_dic = {k: series[k] for k in ass if k in series}
#python moment
clean_dic = {item : list(set({x.lower() for x in value })) for (item, value) in clean_dic.items()}

def find_tag(token):
    for item in clean_dic.items():
        if(token in item[1]):
            return item[0]
    return "No Tag"


listing_titles = listing_titles.to_dict()
titles = listing_titles['Title']
#titles = {num : vals.split(" ") for (num, vals) in titles.items()}
delphine = {k : {find_tag(token.lower()) for token in title} for (k, title) in titles.items()}

print(delphine)
print(titles)

output = ""
for i in range(len(delphine)):
    for j in range(len(list(delphine.values())[i])):
        output += str(i) + " " + list(list(titles.values())[i])[j] + " " + list(list(delphine.values())[i])[j] + "\n"

f = open("output.txt", "w")
f.write(output)
f.close()
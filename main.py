import pandas as pd
import csv
import json
import string

listing_titles = pd.read_csv('./testset/Listing_Titles.tsv', sep='\t', on_bad_lines='skip', quoting=csv.QUOTE_NONE, encoding='utf8')

tagged_titles = pd.read_csv('./testset/Train_Tagged_Titles.tsv', sep='\t', on_bad_lines='skip', quoting=csv.QUOTE_NONE, encoding='utf8')

tags = ['Accents', 'Brand', 'Character', 'Character Family', 'Closure', 'Color', 'Country/Region of Manufacture', 'Department', 'Fabric Type', 'Features', 'Handle Drop', 'Handle Style', 'Handle/Strap Material', 'Hardware Material', 'Lining Material', 'MPN', 'Material', 'Measurement, Dimension', 'Model', 'Occasion', 'Pattern', 'Pocket Type', 'Product Line', 'Season', 'Size', 'Strap Drop', 'Style', 'Theme', 'Trim Material', 'Type']

tiddies = tagged_titles.groupby('Record Number')['Token'].apply(list).to_dict()
ass = tagged_titles.groupby('Record Number')['Tag'].apply(list).to_dict()

print(tiddies[1])
print("<3<3 wuwuwuwuuw I LOVE AMOURANTH DSLKFJSLDKFJSDLK:FJ")
print(ass[1])

amouranth = [[(tiddies[i][tiddie], ass[i][tiddie]) for tiddie in range(0, len(ass[i]))] for i in range(1, len(ass) + 1)]

# [[(LOUIS, Brand), (VITTON, Brand)],[(LOUIS, Brand), (VITTON, Brand)...

#print(tiddies) #SHOW ME THE TIDDIES
print("tiddies")
print(amouranth)

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
amouranth = {k : {find_tag(token.lower()) for token in title} for (k, title) in titles.items()}

print(amouranth)
print(titles)

output = ""
for i in range(len(amouranth)):
    for j in range(len(list(amouranth.values())[i])):
        output += str(i) + " " + list(list(titles.values())[i])[j] + " " + list(list(amouranth.values())[i])[j] + "\n"

f = open("output.txt", "w")
f.write(output)
f.close()
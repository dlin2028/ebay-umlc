import pandas as pd
import csv
import json
import string

listing_titles = pd.read_csv('./testset/Listing_Titles.tsv', sep='\t', on_bad_lines='skip', quoting=csv.QUOTE_NONE, encoding='utf8')

tagged_titles = pd.read_csv('./testset/Train_Tagged_Titles.tsv', sep='\t', on_bad_lines='skip', quoting=csv.QUOTE_NONE, encoding='utf8')

tags = ['Accents', 'Brand', 'Character', 'Character Family', 'Closure', 'Color', 'Country/Region of Manufacture', 'Department', 'Fabric Type', 'Features', 'Handle Drop', 'Handle Style', 'Handle/Strap Material', 'Hardware Material', 'Lining Material', 'MPN', 'Material', 'Measurement, Dimension', 'Model', 'Occasion', 'Pattern', 'Pocket Type', 'Product Line', 'Season', 'Size', 'Strap Drop', 'Style', 'Theme', 'Trim Material', 'Type']

series = tagged_titles.groupby('Record Number')['Token'].apply(list)

print(series)

quit()


clean_dic = {k: series[k] for k in tags if k in series}
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
iamagod = {k : {find_tag(token.lower()) for token in title} for (k, title) in titles.items()}

print(iamagod)
print(titles)

output = ""
for i in range(len(iamagod)):
    for j in range(len(list(iamagod.values())[i])):
        output += str(i) + " " + list(list(titles.values())[i])[j] + " " + list(list(iamagod.values())[i])[j] + "\n"

f = open("output.txt", "w")
f.write(output)
f.close()
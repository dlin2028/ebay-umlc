import pandas as pd
import csv
import json
import string

def strip(text):
    try:
        return text.strip()
    except AttributeError:
        return text

tagged_titles = pd.read_csv('./dataset/Train_Tagged_Titles.tsv', sep='\t', on_bad_lines='skip', quoting=csv.QUOTE_NONE, encoding='utf8')

tags = ['Accents', 'Brand', 'Character', 'Character Family', 'Closure', 'Color', 'Country/Region of Manufacture', 'Department', 'Fabric Type', 'Features', 'Handle Drop', 'Handle Style', 'Handle/Strap Material', 'Hardware Material', 'Lining Material', 'MPN', 'Material', 'Measurement, Dimension', 'Model', 'Occasion', 'Pattern', 'Pocket Type', 'Product Line', 'Season', 'Size', 'Strap Drop', 'Style', 'Theme', 'Trim Material', 'Type']

series = tagged_titles.groupby('Tag')['Token'].apply(list)
clean_dic = {k: series[k] for k in tags if k in series}
#python moment
clean_dic = {item.lower() : list(set({x.lower().translate(string.punctuation) for x in value })) for (item, value) in clean_dic.items()}

with open('models/clean_dic.json', 'w', encoding='utf-8') as f:
    json.dump(clean_dic, f, ensure_ascii=False, indent=4)

print("done")

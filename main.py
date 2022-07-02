import pandas as pd
import csv

def strip(text):
    try:
        return text.strip()
    except AttributeError:
        return text

listing_titles = pd.read_csv('./testset/Listing_Titles.tsv', sep='\t', on_bad_lines='skip', quoting=csv.QUOTE_NONE, encoding='utf8')

tagged_titles = pd.read_csv('./testset/Train_Tagged_Titles.tsv', sep='\t', on_bad_lines='skip', quoting=csv.QUOTE_NONE, encoding='utf8')

tags = {'accents', 'brand', 'character', 'character family', 'closure', 'color', 'country/region of manufacture', 'department', 'fabric type', 'features', 'handle drop', 'handle style', 'handle/strap material', 'hardware material', 'lining material', 'mpn', 'material', 'measurement, dimension', 'model', 'occasion', 'pattern', 'pocket type', 'product line', 'season', 'size', 'strap drop', 'style', 'theme', 'trim material', 'type'}

print(listing_titles)
print(tagged_titles)
print(tagged_titles.groupby('Tag')['Token'].apply(list)[0:10])

# quit

# df2 = tagged_titles[0:100].groupby(['Tag']).sum()


# print(tagged_titles[97:104])
# print("--------------------")
# print(df2[0:10])
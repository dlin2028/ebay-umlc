import pandas as pd

listing_titles = pd.read_csv('./dataset/Listing_Titles.tsv', sep='\t')
tagged_titles = pd.read_csv('./dataset/Train_Tagged_Titles.tsv', on_bad_lines='skip')

tags = {'accents', 'brand', 'character', 'character family', 'closure', 'color', 'country/region of manufacture', 'department', 'fabric type', 'features', 'handle drop', 'handle style', 'handle/strap material', 'hardware material', 'lining material', 'mpn', 'material', 'measurement, dimension', 'model', 'occasion', 'pattern', 'pocket type', 'product line', 'season', 'size', 'strap drop', 'style', 'theme', 'trim material', 'type'}



print(tagged_titles[97:104])
import pandas as pd

listing_titles = pd.read_csv('./dataset/Listing_Titles.tsv', sep='\t')
tagged_titles = pd.read_csv('./dataset/Train_Tagged_Titles.tsv', on_bad_lines='skip')

tags = {'accents', 'brand', 'character', }



print(tagged_titles[97:104])
import pandas as pd
listing_titles = pd.read_csv('./dataset/Listing_Titles.tsv', sep='\t')
print(listing_titles[0:10])
from cgitb import text
import spacy
import csv
import pandas as pd
import numpy as np
from tqdm import tqdm
from spacy.tokens import DocBin
from multiprocessing import Process, freeze_support, set_start_method

if __name__ == '__main__':
    freeze_support()
    spacy.require_gpu()
    nlp = spacy.load("./output/model-best")

    # for ent in doc.ents:
    #     print (ent.text, ent.label_)

    listing_titles = pd.read_csv('./dataset/Listing_Titles.tsv', sep='\t', on_bad_lines='skip', quoting=csv.QUOTE_NONE, encoding='utf8')

    outsize = 1024 * 1024 * 1024 # 1GB

    listing_titles = [(listing_titles["Title"][i], i) for i in range(0, len(listing_titles["Title"]))][5003:30002]

    result = []

    with tqdm(total = 25000) as pbar:
        buffer = ""
        for doc, i in nlp.pipe(listing_titles, as_tuples=True, batch_size=10000):
            for ent in doc.ents:
                result.append(str(i) + '\t' + ent.text + '\t' + ent.label_)
            pbar.update(1)
            
    output = open("output.txt", "w", encoding="utf-8")  # write mode
    output.write('\n'.join(result))
    output.close()

quit()









# outsize = 1024 * 1024 * 1024 # 1GB
# with tqdm(total = 19999921) as pbar:
#     buffer = ''
#     for i, title in tqdm(enumerate(listing_titles['Title'])):
#         doc = nlp(str(title))
#         for ent in doc.ents:
#             buffer += str(i) + ' ' + ent.text + ' ' + ent.label_ + '\n'
#         pbar.update(1)

#     if(len(buffer) > outsize):
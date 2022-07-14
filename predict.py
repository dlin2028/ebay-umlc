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
    output = open("output.txt", "w", encoding="utf-8")  # write mode

    with tqdm(total = 19999921) as pbar:
        buffer = ""
        for i, doc in enumerate(nlp.pipe(listing_titles["Title"].to_numpy())):
            for ent in doc.ents:
                buffer += str(i) + ' ' + ent.text + ' ' + ent.label_ + '\n'
            pbar.update(1)
            if(len(buffer) > outsize):
                output.write(buffer)
                buffer = ""
            
    output.write(buffer)
    output.close()


# outsize = 1024 * 1024 * 1024 # 1GB
# with tqdm(total = 19999921) as pbar:
#     buffer = ''
#     for i, title in tqdm(enumerate(listing_titles['Title'])):
#         doc = nlp(str(title))
#         for ent in doc.ents:
#             buffer += str(i) + ' ' + ent.text + ' ' + ent.label_ + '\n'
#         pbar.update(1)

#     if(len(buffer) > outsize):
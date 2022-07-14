import spacy

nlp = spacy.load("./output/model-best")

for ent in doc.ents:
    print (ent.text, ent.label_)
    
file1 = open("myfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()
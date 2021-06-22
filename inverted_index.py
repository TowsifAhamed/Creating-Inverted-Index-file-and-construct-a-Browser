import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
data = pd.read_csv("papers.csv")
# a set to check if a word is occuring again
s = set()
#words are for holding words, count is for how many times the word is occured and indexx represents where the word was taken from
words = []
count = [0]*99999
indexx = [""]*99999
#getting the data from the csv file to lists
title = data.title.tolist()
description = data.description.tolist()
authors = data.authors.tolist()
#seperately for titles, discriptions and authors
#check if the word occured before then check if it a stopword
#if occured before then just increase count and add index if not then firstly add the word to the list
for i in range(0, len(title)):
    ws = re.sub("[^\w]", " ", title[i]).split()
    for wds in ws:
        if not wds in stopwords.words():
            if (wds in s):
                count[words.index(wds)] += 1
                indexx[words.index(wds)] = indexx[words.index(wds)] + " " + str(i)
            else:
                s.add(wds)
                words.append(wds)
                count[words.index(wds)] += 1
                indexx[words.index(wds)] = indexx[words.index(wds)] + " " + str(i)
for i in range(0, len(description)):
    ws = re.sub("[^\w]", " ", description[i]).split()
    for wds in ws:
        if not wds in stopwords.words():
            if (wds in s):
                count[words.index(wds)] += 1
                indexx[words.index(wds)] = indexx[words.index(wds)] + " " + str(i)
            else:
                s.add(wds)
                words.append(wds)
                count[words.index(wds)] += 1
                indexx[words.index(wds)] = indexx[words.index(wds)] + " " + str(i)
for i in range(0, len(authors)):
    ws = re.sub("[^\w]", " ", authors[i]).split()
    for wds in ws:
        if not wds in stopwords.words():
            if (wds in s):
                count[words.index(wds)] += 1
                indexx[words.index(wds)] = indexx[words.index(wds)] + " " + str(i)
            else:
                s.add(wds)
                words.append(wds)
                count[words.index(wds)] += 1
                indexx[words.index(wds)] = indexx[words.index(wds)] + " " + str(i)
#then creating a inverted indexed csv
inverted = pd.DataFrame()
inverted['words']=words
del count[len(words):]
del indexx[len(words):]
inverted['count']=count
inverted['index']=indexx
inverted.to_csv("inverted.csv")
#for i in range(0, len(indexx)):
    #links=[int(s) for s in indexx[i].split() if s.isdigit()]
#python inverted_index.py